# 🤖 Discord Onay Bot

Discord sunucunuzda kullanıcıların custom status'lerinde `discord.gg/onay` yazan kişilere otomatik rol veren bot.

## ✨ Özellikler

- ✅ Kullanıcı durumuna `discord.gg/onay` eklediğinde otomatik rol verir
- ❌ Durumdan `discord.gg/onay` kaldırıldığında rolü geri alır
- 📊 İki ayrı kanala log mesajları gönderir (ekleme/kaldırma)
- 💬 Kullanıcılara DM ile bildirim gönderir
- 🎨 Embed mesajlar ile profesyonel görünüm

## 🚀 Railway'e Deploy Etme

### 1. GitHub'a Yükle

```bash
cd onaybot
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADIN/onaybot.git
git push -u origin main
```

### 2. Railway'de Proje Oluştur

1. [Railway.app](https://railway.app/) sitesine git
2. GitHub ile giriş yap
3. "New Project" butonuna tıkla
4. "Deploy from GitHub repo" seç
5. `onaybot` repository'sini seç

### 3. Environment Variables Ekle

Railway dashboard'unda **Variables** sekmesine git ve şu değişkenleri ekle:

```
DISCORD_TOKEN=your_discord_bot_token_here
LOG_CHANNEL_ID=1500490932129103954
REMOVE_LOG_CHANNEL_ID=1500493256188760114
ROLE_ID=1500243793440673822
```

### 4. Deploy

Railway otomatik olarak deploy edecek. Logs sekmesinden durumu takip edebilirsin.

## 🔧 Yerel Kurulum

### Gereksinimler

- Python 3.11+
- Discord Bot Token

### Kurulum Adımları

1. Repository'yi klonla:
```bash
git clone https://github.com/KULLANICI_ADIN/onaybot.git
cd onaybot
```

2. Sanal ortam oluştur ve aktifleştir:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Bağımlılıkları yükle:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluştur:
```bash
cp .env.example .env
```

5. `.env` dosyasını düzenle ve bilgilerini gir:
```env
DISCORD_TOKEN=your_discord_bot_token_here
LOG_CHANNEL_ID=your_log_channel_id
REMOVE_LOG_CHANNEL_ID=your_remove_log_channel_id
ROLE_ID=your_role_id
```

6. Botu çalıştır:
```bash
python onaybot.py
```

## 📝 Discord Bot Oluşturma

1. [Discord Developer Portal](https://discord.com/developers/applications)'a git
2. "New Application" butonuna tıkla
3. Bot'a bir isim ver
4. Sol menüden "Bot" sekmesine git
5. "Add Bot" butonuna tıkla
6. "Reset Token" ile token'ı al (bu token'ı `.env` dosyasına ekle)
7. **Privileged Gateway Intents** bölümünden şunları aktif et:
   - ✅ PRESENCE INTENT
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT

### Bot'u Sunucuya Davet Etme

1. Sol menüden "OAuth2" > "URL Generator" sekmesine git
2. **SCOPES** bölümünden:
   - ✅ `bot`
3. **BOT PERMISSIONS** bölümünden:
   - ✅ Manage Roles
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
4. Oluşan URL'yi kopyala ve tarayıcıda aç
5. Bot'u sunucuna davet et

## ⚙️ Yapılandırma

Bot'u yapılandırmak için `.env` dosyasındaki değerleri değiştir:

- `DISCORD_TOKEN`: Discord bot token'ın
- `LOG_CHANNEL_ID`: Durum eklendiğinde log düşecek kanal ID'si
- `REMOVE_LOG_CHANNEL_ID`: Durum silindiğinde log düşecek kanal ID'si
- `ROLE_ID`: Verilecek rolün ID'si

### Kanal ve Rol ID'lerini Bulma

1. Discord'da Developer Mode'u aktif et (User Settings > Advanced > Developer Mode)
2. Kanala/Role sağ tıkla ve "Copy ID" seç

## 🐛 Sorun Giderme

### Bot çevrimiçi görünmüyor
- Discord token'ın doğru olduğundan emin ol
- Bot'un sunucuda olduğundan emin ol
- Railway logs'ları kontrol et

### Rol verilmiyor
- Bot'un rolü, verilecek rolden daha yukarıda olmalı
- Bot'un "Manage Roles" yetkisi olmalı
- Privileged Gateway Intents aktif olmalı

### Log mesajları gelmiyor
- Kanal ID'lerinin doğru olduğundan emin ol
- Bot'un kanala mesaj gönderme yetkisi olmalı

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🤝 Katkıda Bulunma

1. Fork'la
2. Feature branch oluştur (`git checkout -b feature/amazing-feature`)
3. Commit'le (`git commit -m 'Add some amazing feature'`)
4. Push'la (`git push origin feature/amazing-feature`)
5. Pull Request aç

## 📧 İletişim

Sorularınız için issue açabilirsiniz.

---

⭐ Projeyi beğendiysen yıldız vermeyi unutma!
