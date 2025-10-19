from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import io

# Flask uygulaması oluştur
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Veritabanı konfigürasyonu - Vercel için geçici dosya sistemi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/stok_takip.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy başlat
db = SQLAlchemy(app)

# Ürün modeli
class Urun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.String(100), nullable=False)
    barkod = db.Column(db.String(50), unique=True, nullable=False)
    stok_adedi = db.Column(db.Integer, nullable=False, default=0)
    birim_fiyat = db.Column(db.Float, nullable=False, default=0.0)
    kategori = db.Column(db.String(50), nullable=True)
    aciklama = db.Column(db.Text, nullable=True)
    olusturma_tarihi = db.Column(db.DateTime, default=datetime.utcnow)
    guncelleme_tarihi = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def toplam_deger(self):
        return self.stok_adedi * self.birim_fiyat
    
    def __repr__(self):
        return f'<Urun {self.ad}>'

# Veritabanını oluştur
with app.app_context():
    db.create_all()

# Ana sayfa
@app.route('/')
def index():
    # İstatistikler
    toplam_urun = Urun.query.count()
    toplam_stok = db.session.query(db.func.sum(Urun.stok_adedi)).scalar() or 0
    toplam_deger = db.session.query(db.func.sum(Urun.stok_adedi * Urun.birim_fiyat)).scalar() or 0
    dusuk_stoklu_urunler = Urun.query.filter(Urun.stok_adedi <= 10).count()
    
    # Son eklenen ürünler
    son_urunler = Urun.query.order_by(Urun.olusturma_tarihi.desc()).limit(5).all()
    
    istatistikler = {
        'toplam_urun': toplam_urun,
        'toplam_stok': toplam_stok,
        'toplam_deger': toplam_deger,
        'dusuk_stoklu_urunler': dusuk_stoklu_urunler
    }
    
    return render_template('index.html', istatistikler=istatistikler, son_urunler=son_urunler)

# Ürün ekleme
@app.route('/urun_ekle', methods=['GET', 'POST'])
def urun_ekle():
    if request.method == 'POST':
        try:
            # Barkod kontrolü
            barkod = request.form['barkod'].strip()
            mevcut_urun = Urun.query.filter_by(barkod=barkod).first()
            
            if mevcut_urun:
                flash('Bu barkod numarası zaten kullanılıyor!', 'error')
                return redirect(url_for('urun_ekle'))
            
            # Yeni ürün oluştur
            yeni_urun = Urun(
                ad=request.form['ad'].strip(),
                barkod=barkod,
                stok_adedi=int(request.form['stok_adedi']),
                birim_fiyat=float(request.form['birim_fiyat']),
                kategori=request.form.get('kategori', '').strip(),
                aciklama=request.form.get('aciklama', '').strip()
            )
            
            db.session.add(yeni_urun)
            db.session.commit()
            
            flash(f'Ürün "{yeni_urun.ad}" başarıyla eklendi!', 'success')
            return redirect(url_for('index'))
            
        except ValueError as e:
            flash('Lütfen sayısal değerleri doğru formatta girin!', 'error')
        except Exception as e:
            flash(f'Ürün eklenirken hata oluştu: {str(e)}', 'error')
            db.session.rollback()
    
    return render_template('urun_ekle.html')

# Vercel serverless function handler
def handler(request):
    return app(request.environ, lambda status, headers: None)

# Vercel için export
app = app
