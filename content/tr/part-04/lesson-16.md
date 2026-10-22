# Ders 16: Yalın Yönetim 2.0 (Lean Six Sigma in AI): Süreç Madenciliği (Process Mining) ile İsrafı Yok Etmek

> **Bölüm 4: Operasyonlar, Tedarik Zinciri & Yalın Süreçler (The Operations & Supply Chain Leader)** | *Seviye 4: Operasyon & Tedarik / Operations Director*

---

### 📌 Kısa Özet & Zihniyet Dönüşümü
Toyota'nın yalın üretim felsefesi (Kaizen ve Muda), yapay zeka çağında dijital süreç madenciliği (Process Mining) ile birleşiyor. Operasyon liderleri artık çalışanların hislerine göre değil, ERP ve CRM loglarını tarayan algoritmalarla şirket içindeki gizli darboğazları, tekrarlanan gereksiz onayları ve zaman israflarını milisaniye hassasiyetinde tespit edip yok ediyor.

---

### 💡 Aptala Anlatır Gibi (ELI5) & Eğlenceli Hikaye
> Eski usul operasyon yönetimi, bir su borusundaki tıkanıklığı bulmak için duvarı rastgele kırmaya benzer. Süreç madenciliği ise borunun içine küçük ışıklı bir kamera gönderip, tıkanıklığın tam olarak hangi dirsekte olduğunu ve oraya hangi paslı çivinin takıldığını ekranda net bir şekilde görmektir.

---

### ⚖️ Eski Usul vs. AI Destekli Yaklaşım
| Konu / Boyut | Eski Usul (Legacy Business) | AI Destekli Modern Yaklaşım |
|---|---|---|
| **Süreç Haritalama** | Çalışanlarla anket yapıp duvara idealize edilmiş sahte akış şemaları çizmek. | Sistem loglarını (SAP, Salesforce, Jira) okuyarak gerçekte ne yaşandığını gösteren canlı süreç ikizi çıkarmak. |
| **İsraf (Muda) Tespiti** | Yılda bir kez verimlilik toplantısı yapıp genel tasarruf çağrıları yapmak. | En çok bekletilen onay adımlarını ve mükerrer işleri yapay zekayla otomatik işaretlemek. |
| **İyileştirme Döngüsü** | Hantal 6 aylık danışmanlık projeleriyle küçük değişiklikler denemek. | Haftalık Kaizen döngüleriyle süreçleri otonom kurallarla sürekli optimize etmek. |

---

### 🚀 Adım Adım Eylem Çerçevesi (Actionable Framework)
- 1. 8 Büyük İsrafı (TIMWOODS) Dijitalleştir: Taşıma, Envanter, Hareket, Bekleme, Aşırı Üretim, Aşırı İşleme, Hatalar ve Kullanılmayan Yetenek.
- 2. Olay Günlüklerini (Event Logs) Birleştir: Bir siparişin açılışından faturanın kapanışına kadar tüm zaman damgalarını (Timestamp) topla.
- 3. Darboğaz Grafiği Çıkar: Hangi departman onayında ortalama bekleme süresi 48 saati aşıyor?
- 4. Otonom Eleme: Katma değeri olmayan onay mekanizmalarını kaldır; belirli limitin altındaki kararları AI kurallarına delege et.

---

### 🚨 Gerçek Hayat Vaka / Kriz Analizi (War Story)
Uluslararası bir üretim firmasında satın alma siparişlerinin onaylanması ortalama 18 gün sürüyordu ve fabrikada üretim aksıyordu. Yönetim 'daha çok personel alalım' diyordu. Yeni operasyon direktörü, son 6 aylık 14.000 satın alma sürecini AI süreç madenciliği yazılımına soktu. Şok edici gerçek ortaya çıktı: 500 TL'nin altındaki kırtasiye malzemeleri bile Genel Müdür Yardımcısı onayına gidiyor ve masasında ortalama 12 gün bekliyordu! Direktör 5.000 TL altındaki harcamaları otomatik onaylayan bir AI kuralı koydu. Sipariş süresi 18 günden 6 saate düştü ve şirket 2 milyon TL operasyonel maliyet tasarrufu sağladı.

---

### 🤖 Kullanıma Hazır AI Promptları & Şablonlar
#### 🛠️ Yalın Süreç Cerrahı ve Süreç Madenciliği Denetçisi
```text
Sen dünyanın en kıdemli Yalın Altı Sigma Kara Kuşağı (Master Black Belt) ve Operasyon Direktörüsün. Sana şirketimizin şu operasyonel akışını veriyorum: [SÜREÇ ADIMLARI VE SÜRELERİ]. 1) Bu akıştaki en büyük 3 'Muda' (israf) noktasını TIMWOODS çerçevesinde teşhis et, 2) Katma değeri sıfır olan ve derhal kaldırılması gereken onay adımlarını belirle, 3) Süreç süresini %60 kısaltacak yapay zeka destekli otonom bir akış mimarisi tasarla.
```

---

### 🎙️ NotebookLM Podcast Tartışma Komutu (Deep Dive Audio)
> **NotebookLM Audio Overview Komutu (Deep Dive 2-Speaker Script):**
> İki operasyon lideri: Biri her şeye imza atmak isteyen, masasında evrak dağları biriken hantal kurumsal müdür, diğeri süreç madenciliği ve yapay zekayla şirketteki tüm gereksiz bürokrasiyi tek gecede buharlaştıran yalın operasyon mimarı. 'Süreç madenciliği devrimi ve şirketlerdeki gizli zaman hırsızları' konusunu sürükleyici bir sohbetle ele alın.

---

### 🎓 Udemy Ders Özeti, Video Zaman Damgaları & Egzersiz
- 00:00 - Neden Şirketlerde İşler Bu Kadar Yavaş İlerler? Gizli İsraf
- 04:30 - Toyota'nın Kaizen Felsefesinden Yapay Zeka Süreç Madenciliğine
- 10:00 - TIMWOODS: Dijital Dünyanın 8 Büyük Zaman Hırsızı
- 16:15 - Canlı Uygulama: 18 Günlük Süreci 6 Saate İndiren Akıllı Onay Sistemi
- 22:30 - Eylem Görevi: Şirketindeki En Sıkıcı Onay Sürecini Haritala ve Yalınlaştır
