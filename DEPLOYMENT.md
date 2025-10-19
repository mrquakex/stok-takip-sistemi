# 🚀 Deployment Rehberi - 7/24 Hosting

Bu rehber, Stok Takip Sisteminizi sunucunuz olmadan 7/24 çalıştırmanız için adım adım talimatlar içerir.

## 🆓 Render.com ile Ücretsiz Deployment (Önerilen)

### 📋 Gereksinimler
- GitHub hesabı
- Git kurulu bilgisayar

### 🔧 Adım 1: GitHub'a Yükleme

1. **GitHub'da yeni repository oluşturun:**
   - GitHub.com'a gidin
   - "New repository" tıklayın
   - Repository adı: `stok-takip-sistemi`
   - Public seçin (ücretsiz plan için)

2. **Projeyi GitHub'a yükleyin:**
   ```bash
   cd C:\Users\mustafa\CascadeProjects\stok-takip-uygulamasi
   git init
   git add .
   git commit -m "İlk commit - Stok Takip Sistemi"
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADINIZ/stok-takip-sistemi.git
   git push -u origin main
   ```

### 🌐 Adım 2: Render.com'da Deployment

1. **Render.com hesabı oluşturun:**
   - [render.com](https://render.com) adresine gidin
   - "Get Started for Free" tıklayın
   - GitHub ile giriş yapın

2. **Web Service oluşturun:**
   - Dashboard'da "New +" tıklayın
   - "Web Service" seçin
   - GitHub repository'nizi seçin
   - Ayarları yapın:
     - **Name**: `stok-takip-sistemi`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python app.py`
     - **Plan**: `Free` seçin

3. **Environment Variables ekleyin:**
   - "Environment" sekmesine gidin
   - Şu değişkenleri ekleyin:
     ```
     FLASK_ENV=production
     PYTHON_VERSION=3.11.0
     ```

4. **Deploy edin:**
   - "Create Web Service" tıklayın
   - 5-10 dakika bekleyin
   - Deploy tamamlandığında URL'niz hazır!

### 🎯 Sonuç
- Uygulamanız `https://stok-takip-sistemi-XXXX.onrender.com` adresinde çalışacak
- SSL sertifikası otomatik dahil
- 15 dakika inaktivite sonrası uyku modu (ilk erişimde 30 saniye gecikme)

---

## 🚂 Railway.app ile Deployment

### 🔧 Adım Adım

1. **Railway hesabı:**
   - [railway.app](https://railway.app) adresine gidin
   - GitHub ile giriş yapın

2. **Proje oluşturun:**
   - "New Project" tıklayın
   - "Deploy from GitHub repo" seçin
   - Repository'nizi seçin

3. **Ayarları yapın:**
   - Otomatik olarak Python algılanacak
   - Environment variables:
     ```
     FLASK_ENV=production
     PORT=8080
     ```

4. **Deploy:**
   - Otomatik deploy başlayacak
   - URL'niz hazır: `https://PROJE-ADI.up.railway.app`

### 💰 Maliyet
- $5 ücretsiz kredi/ay
- Sonrasında kullanım bazlı ücretlendirme

---

## ✈️ Fly.io ile Deployment

### 🔧 Kurulum

1. **Fly CLI kurulumu:**
   ```bash
   # Windows için
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Fly.io hesabı:**
   ```bash
   fly auth signup
   ```

3. **Uygulama oluşturma:**
   ```bash
   cd C:\Users\mustafa\CascadeProjects\stok-takip-uygulamasi
   fly launch
   ```

4. **Deploy:**
   ```bash
   fly deploy
   ```

### 🎯 Sonuç
- Global CDN ile hızlı erişim
- Otomatik SSL
- URL: `https://APP-NAME.fly.dev`

---

## 🐍 PythonAnywhere ile Deployment

### 📋 Adım Adım

1. **Hesap oluşturun:**
   - [pythonanywhere.com](https://www.pythonanywhere.com) adresine gidin
   - Ücretsiz hesap oluşturun

2. **Dosyaları yükleyin:**
   - Files sekmesinden dosyalarınızı yükleyin
   - Veya Git ile clone edin

3. **Web app oluşturun:**
   - Web sekmesine gidin
   - "Add a new web app" tıklayın
   - Flask seçin
   - `app.py` dosyanızı seçin

4. **Ayarları yapın:**
   - Static files ayarlarını yapın
   - Virtual environment kurun

### 🎯 Sonuç
- URL: `https://KULLANICI-ADI.pythonanywhere.com`
- Günlük CPU limiti var

---

## 💡 Hangi Seçeneği Seçmeli?

### 🏆 **Render.com** (En Kolay)
- ✅ Tamamen ücretsiz başlangıç
- ✅ Kolay setup
- ✅ GitHub entegrasyonu
- ❌ 15 dk sonra uyku modu

### 🚀 **Railway.app** (En Hızlı)
- ✅ Çok hızlı deployment
- ✅ $5 ücretsiz kredi
- ✅ Veritabanı desteği
- ❌ Kredi bitince ücretli

### ⚡ **Fly.io** (En Performanslı)
- ✅ Global CDN
- ✅ Hızlı erişim
- ✅ Ücretsiz plan
- ❌ Teknik bilgi gerekir

### 🐍 **PythonAnywhere** (Python Odaklı)
- ✅ Python uzmanı
- ✅ Web konsol
- ✅ Kolay yönetim
- ❌ Günlük limit

---

## 🔧 Deployment Sonrası Ayarlar

### 📊 Veritabanı Yedekleme
Ücretsiz planlar veritabanı yedeklemez. Önemli veriler için:
- Düzenli Excel export yapın
- Veritabanı dosyasını indirin

### 🔒 Güvenlik
Production ortamında:
```python
app.config['SECRET_KEY'] = 'GÜÇLÜ-GİZLİ-ANAHTAR-BURAYA'
```

### 📈 Monitoring
- Render.com: Otomatik log takibi
- Railway: Metrics dashboard
- Fly.io: Monitoring araçları

---

## 🆘 Sorun Giderme

### ❌ Build Hatası
```bash
# requirements.txt kontrol edin
pip freeze > requirements.txt
```

### ❌ Port Hatası
```python
# app.py'de port ayarını kontrol edin
port = int(os.environ.get('PORT', 5000))
```

### ❌ Database Hatası
```python
# SQLite dosya yolu kontrol edin
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stok_takip.db'
```

---

## 📞 Destek

Deployment sırasında sorun yaşarsanız:
1. Platform dokümantasyonunu kontrol edin
2. Log dosyalarını inceleyin
3. GitHub Issues'a sorun bildirin

**🎉 Başarılar! Uygulamanız artık 7/24 çalışacak!**
