# Ders 18: Otonom İş Akışları ve Robotik Süreç Otomasyonu (RPA & Agentic Workflows): Rutin Operasyonları Devretmek

> **Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)** | *Seviye 4: Operasyon & Tedarik / Operations Director*

---

### 📌 Kısa Özet & Zihniyet Dönüşümü
Eski nesil Robotik Süreç Otomasyonu (RPA), ekranda bir butonun yeri 2 piksel değiştiğinde bozulan kırılgan kural tabanlı robotlardan ibaretti. Yeni nesil Agentic Workflows ise; algılayan, akıl yürüten, API'ları dinamik çağıran ve beklenmedik hatalarla karşılaştığında kendi kendine çözüm üreten otonom yapay zeka çalışanlarıdır.

---

### 💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye
> Eski RPA, gözleri bağlı olarak ezbere yürüyen bir robota benzer; önüne küçük bir sandalye koysan takılıp düşer ve kalkamaz. Ajan tabanlı yapay zeka ise gözleri açık, düşünen ve yoluna bir taş çıktığında 'Dur, ben bu taşın etrafından dolaşayım ya da vinç çağırıp taşı kaldırayım' diyen akıllı bir saha mühendisidir.

---

### ⚖️ Eski Usul vs. AI Destekli Yaklaşım
| Konu / Boyut | Eski Usul (Legacy Business) | AI Destekli Modern Yaklaşım |
|---|---|---|
| **Otomasyon Mimarisi** | Kırılgan kural tabanlı RPA: 'A hücresini kopyala, B formuna yapıştır.' | Hedef odaklı Ajan Akışı: 'Şu faturayı incele, vergi numarasını doğrula ve ödemeyi yap.' |
| **Hata ve İstisna Yönetimi** | En ufak format değişikliğinde akışın patlaması ve teknik destek çağrılması. | Semantik anlama: Veri formatı bozuk olsa bile içeriği anlayıp düzelten yapay zeka. |
| **İnsan Müdahalesi (HITL)** | İnsanın ya sürecin başında ya da sonunda amelelik yapmaya devam etmesi. | İnsanın sadece stratejik denetçi ve nihai onaylayıcı (Supervisor) olarak konumlanması. |

---

### 🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)
- 1. Görev Ayrıştırması Yap: İşi Deterministik (Kurala bağlı) vs. Bilişsel (Muhakeme gerektiren) parçalara böl.
- 2. Tool-Calling Mimarisi Kur: Yapay zekaya ERP'yi okuma, e-posta atma ve veritabanı sorgulama gibi spesifik 'araçlar' (Tools) ver.
- 3. Güven Eşiği (Confidence Threshold): Ajanın doğruluğundan %95 emin olduğu işleri otomatik bitirmesini, %95 altındakileri insan onayına göndermesini sağla.
- 4. Kendi Kendini Denetleyen Döngü (Self-Reflective Loop): Ajanın işlem yapmadan önce 'Bu çıktı şirket politikalarına ve bütçeye uygun mu?' kontrolü yapmasını sağla.

---

### 🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)
Büyük bir hukuk ve denetim şirketinde 15 kişilik bir stajyer ekibi, her gün gelen 800 farklı tedarikçi sözleşmesini okuyup 'cezai şartlar ve gizlilik maddelerini' Excel'e işliyordu. Hata oranı %14'tü ve haftalar sürüyordu. Operasyon lideri, açık kaynaklı bir Agentic Workflow (LangGraph / n8n tabanlı) kurdu. Birinci ajan sözleşmeyi tarayıp maddeleri ayıklıyor, ikinci ajan bunları şirketin yasal risk politikasıyla karşılaştırıyor, üçüncü ajan ise bulunan anomalileri avukata tek tıkla onaylanacak bir Slack mesajı olarak atıyordu. İşlem süresi 15 günden 4 dakikaya indi, hata oranı sıfırlandı ve 15 çalışan stratejik danışmanlık rollerine kaydırıldı.

---

### 🤖 Kullanıma Hazır AI Promptları & Şablonlar
#### 🛠️ Otonom İş Akışı ve Agentic Tool-Calling Mimarı
```text
Sen dünyanın en iyi Kurumsal Otomasyon Mimarı ve CTO Danışmanısın. Şu manuel iş akışını ele al: [MANUEL SÜRECİ VE ARAÇLARI YAZ]. 1) Bu süreci otonom hale getirecek çoklu ajan mimarisini (Orchestrator, Worker ve Critic ajanları) tasarla, 2) Ajanların kullanacağı 3 temel API fonksiyonunu (Tool-calling şeması) tanımla, 3) Sürecin kontrolden çıkmasını ve şirket kasasını boşaltmasını önleyecek 'Human-in-the-Loop' güvenlik bariyerlerini yaz.
```

---

### 🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> İki teknoloji yöneticisi: Biri eski usul RPA robotlarının sürekli bozulmasından bıkmış bezgin bir IT müdürü, diğeri kendi kendini iyileştiren (self-healing) agentic sistemlerle şirketteki tüm rutin evrak işlerini sıfırlayan modern operasyon lideri. 'Robotik Süreç Otomasyonunun sonu ve düşünen yapay zeka ajanlarının iş dünyasını fethi' konusunu nefes kesici bir sohbetle dinleyin.

---

### 🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz
- 00:00 - Neden Eski Nesil RPA Projelerinin %70'i Başarısız Oldu?
- 04:40 - Agentic Workflows Nedir? Algıla -> Düşün -> Harekete Geç Döngüsü
- 10:15 - Çoklu Ajan Sistemleri: Görev Dağıtımı ve Karşılıklı Denetim (Critic)
- 16:20 - Canlı Uygulama: Fatura ve Sözleşmeleri 3 Dakikada İşleyen Otonom Akış
- 22:45 - Eylem Görevi: Kendi Departmanındaki En Çok Zaman Alan İşi Ajan Akışına Çevir
