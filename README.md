# 📦 Stok Takip Sistemi

Modern ve kullanıcı dostu Python Flask tabanlı web stok takip uygulaması. Bu uygulama ile ürünlerinizi kolayca yönetebilir, stok durumlarını takip edebilir ve detaylı raporlar alabilirsiniz.

## ✨ Özellikler

### 🎯 Temel Özellikler
- **Ürün Yönetimi**: Ürün ekleme, düzenleme, silme ve listeleme
- **Stok Takibi**: Gerçek zamanlı stok durumu kontrolü
- **Arama Sistemi**: Ürün adı ve barkod numarasına göre hızlı arama
- **Kategori Yönetimi**: Ürünleri kategorilere ayırma
- **Toplam Değer Hesaplama**: Otomatik stok değeri hesaplama

### 🔍 Gelişmiş Özellikler
- **Çift Barkod Okuyucu Desteği**: 
  - 🖥️ Klavye girişi olarak çalışan USB barkod okuyucu
  - 📱 Mobil kamera ile barkod okuma (ZXing kütüphanesi)
- **Excel Dışa Aktarma**: Tüm stok listesini .xlsx formatında dışa aktarma
- **PDF Rapor Oluşturma**: Profesyonel PDF raporları
- **Düşük Stok Uyarısı**: Otomatik düşük stok bildirimleri
- **Modern Responsive Tasarım**: 
  - 🎨 Gradient renkler ve animasyonlar
  - 📱 Mobil-first yaklaşım
  - ✨ Hover efektleri ve geçişler

### 📊 Raporlama
- Günlük/haftalık/aylık stok raporları
- Excel ve PDF formatında dışa aktarma
- Düşük stok uyarı raporları
- Kategori bazlı analiz

## 🛠️ Teknoloji Stack

- **Backend**: Python 3.8+ & Flask 2.3.3
- **Veritabanı**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **JavaScript**: Vanilla JS + ZXing (Kamera barkod okuyucu)
- **Excel İşlemleri**: openpyxl
- **PDF Oluşturma**: ReportLab
- **İkonlar**: Font Awesome 6.0.0
- **Barkod Okuma**: ZXing-js kütüphanesi

## 📋 Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

## 🚀 Kurulum

### 1. Projeyi İndirin
```bash
git clone <repository-url>
cd stok-takip-uygulamasi
```

### 2. Sanal Ortam Oluşturun (Önerilen)
```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Uygulamayı Başlatın
```bash
python app.py
```

### 5. Tarayıcınızda Açın
```
http://localhost:5000
```

## 📁 Proje Yapısı

```
stok-takip-uygulamasi/
├── app.py                 # Ana Flask uygulaması
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
├── stok_takip.db         # SQLite veritabanı (otomatik oluşur)
├── templates/            # HTML şablonları
│   ├── base.html         # Ana şablon
│   ├── index.html        # Ana sayfa
│   ├── urun_ekle.html    # Ürün ekleme sayfası
│   ├── urun_duzenle.html # Ürün düzenleme sayfası
│   ├── arama_sonuclari.html # Arama sonuçları
│   └── dusuk_stok.html   # Düşük stok uyarısı
└── static/               # Statik dosyalar
    └── exports/          # Excel/PDF dışa aktarma klasörü
```

## 🎮 Kullanım Kılavuzu

### Ürün Ekleme
1. Ana sayfada "Yeni Ürün" butonuna tıklayın
2. Ürün bilgilerini doldurun:
   - Ürün adı (zorunlu)
   - Barkod numarası (zorunlu, benzersiz olmalı)
   - Stok adedi
   - Birim fiyat
   - Kategori
   - Açıklama (opsiyonel)
3. "Ürünü Kaydet" butonuna tıklayın

### Barkod Okuyucu Kullanımı

#### 🖥️ USB Barkod Okuyucu
- Barkod okuyucunuzu bilgisayara bağlayın
- Ürün ekleme sayfasında barkod alanına odaklanın
- Barkodu okutun - bilgiler otomatik doldurulacak

#### 📱 Mobil Kamera Barkod Okuyucu
- Mobil cihazlarda sağ alt köşedeki kamera butonuna tıklayın
- Masaüstünde barkod alanının yanındaki kamera butonunu kullanın
- Kamera izni verin ve barkodu kamera görüntüsünde ortalayın
- Barkod otomatik algılanacak ve 3 saniye sonra kullanılacak
- Birden fazla kamera varsa "Kamera Değiştir" butonu görünür

### Arama Yapma
- Üst menüdeki arama kutusunu kullanın
- Ürün adı veya barkod numarası ile arama yapabilirsiniz
- Sonuçlar vurgulanarak gösterilir

### Rapor Alma
1. **Excel Raporu**: "Raporlar" > "Excel Dışa Aktar"
2. **PDF Raporu**: "Raporlar" > "PDF Rapor"
3. **Düşük Stok Raporu**: "Düşük Stok" menüsünden

## ⚙️ Yapılandırma

### Veritabanı
Uygulama ilk çalıştırıldığında `stok_takip.db` dosyası otomatik oluşturulur. Bu dosya tüm ürün bilgilerinizi içerir.

### Güvenlik
Üretim ortamında kullanım için:
1. `app.py` dosyasındaki `SECRET_KEY`'i değiştirin
2. `debug=False` yapın
3. Güvenli bir web sunucusu (nginx, Apache) kullanın

## 🔧 Özelleştirme

### Kategoriler
`urun_ekle.html` ve `urun_duzenle.html` dosyalarındaki kategori listesini ihtiyaçlarınıza göre düzenleyebilirsiniz.

### Düşük Stok Limiti
Varsayılan düşük stok limiti 10'dur. `app.py` dosyasında `dusuk_stok` fonksiyonunu düzenleyerek değiştirebilirsiniz.

### Tema ve Renkler
`base.html` dosyasındaki CSS stillerini düzenleyerek uygulamanın görünümünü özelleştirebilirsiniz.

## 📱 Mobil Uyumluluk

Uygulama Bootstrap 5 kullanılarak geliştirilmiştir ve tüm cihazlarda responsive olarak çalışır:
- 📱 Mobil telefonlar
- 📱 Tabletler  
- 💻 Masaüstü bilgisayarlar

## 🐛 Sorun Giderme

### Yaygın Sorunlar

**1. Modül bulunamadı hatası**
```bash
pip install -r requirements.txt
```

**2. Veritabanı hatası**
`stok_takip.db` dosyasını silin, uygulama yeniden oluşturacaktır.

**3. Port zaten kullanımda**
`app.py` dosyasındaki port numarasını değiştirin:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

**4. Barkod okuyucu çalışmıyor**
- Barkod okuyucunuzun "klavye emülasyonu" modunda çalıştığından emin olun
- Barkod okuyucu ayarlarını kontrol edin

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

## 📞 Destek

Herhangi bir sorun yaşarsanız veya öneriniz varsa:
- GitHub Issues kullanın
- E-posta ile iletişime geçin

## 🔄 Güncellemeler

### v1.1.0 (2024-10-19)
- ✅ Modern gradient tasarım
- ✅ Mobil kamera barkod okuyucu (ZXing)
- ✅ Animasyonlar ve hover efektleri
- ✅ Toast bildirimleri
- ✅ Gelişmiş responsive tasarım
- ✅ Floating kamera butonu (mobil)

### v1.0.0 (2024-10-19)
- ✅ İlk sürüm yayınlandı
- ✅ Temel CRUD işlemleri
- ✅ USB barkod okuyucu desteği
- ✅ Excel/PDF dışa aktarma
- ✅ Düşük stok uyarısı
- ✅ Temel responsive tasarım

## 🎯 Gelecek Özellikler

- [ ] Kullanıcı yetkilendirme sistemi
- [ ] Tedarikçi yönetimi
- [ ] Stok giriş/çıkış geçmişi
- [ ] Grafik ve istatistikler
- [ ] E-posta bildirimleri
- [ ] API desteği
- [ ] Çoklu dil desteği

---

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!**

*Geliştirici: [Adınız] - 2024*
