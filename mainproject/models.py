from django.db import models
from django.utils import timezone

class Ders(models.Model):
    DERS_TURU = [
        ('AKAID', 'Akaid (İtikad)'),
        ('FIKIH', 'Fıkıh (İbadet)'),
        ('SIYER', 'Siyer'),
        ('TECV', 'Tecvid'),
    ]
    
    ad = models.CharField(max_length=100)
    tur = models.CharField(max_length=5, choices=DERS_TURU, unique=True)
    aciklama = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Dersler"
    
    def __str__(self):
        return self.get_tur_display()
    
    def save(self, *args, **kwargs):
        if not self.ad:
            self.ad = self.get_tur_display()
        super().save(*args, **kwargs)

class EzberSuresi(models.Model):
    EZBER_SIRASI = [
        (1, '1. Mülk Suresi'),
        (2, '2. Cin Suresi'),
        (3, '3. Kıyame Suresi'),
        (4, '4. Cuma Suresi'),
        (5, '5. Saff Suresi'),
        (6, '6. Rahman Suresi'),
        (7, '7. Vakia Suresi'),
        (8, '8. Fetih Suresi'),
        (9, '9. Hucurat Suresi'),
        (10, '10. Yasin Suresi'),
        (11, '11. Enfal Suresi'),
        (12, '12. İsra Suresi'),
        (13, '13. 30. Cüz Tamamı'),
    ]
    
    ad = models.CharField(max_length=100)
    sira = models.PositiveSmallIntegerField(choices=EZBER_SIRASI, unique=True)
    tahmini_sure = models.PositiveSmallIntegerField(help_text="Tahmini ezber süresi (gün)", default=7)
    aciklama = models.TextField(blank=True)
    
    class Meta:
        ordering = ['sira']
        verbose_name = "Ezber Süresi"
        verbose_name_plural = "Ezber Süreleri"
    
    def __str__(self):
        return f"{self.get_sira_display()} - {self.ad}"

class Ogrenci(models.Model):
    SEVIYE_CHOICES = [
        ('HAZ1', 'Hazırlık 1. Seviye'),
        ('HAZ2', 'Hazırlık 2. Seviye'),
        ('HAZ3', 'Hazırlık 3. Seviye'),
        ('TEMEL', 'Temel Hafızlık'),
        ('ILERI', 'İleri Hafızlık'),
    ]
    
    ad_soyad = models.CharField(max_length=100)
    kayit_tarihi = models.DateField(default=timezone.now)
    seviye = models.CharField(max_length=5, choices=SEVIYE_CHOICES, default='HAZ1')
    profil_foto = models.ImageField(upload_to='ogrenci_profil/', blank=True, null=True)
    ozel_notlar = models.TextField(blank=True)
    son_guncelleme = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Öğrenciler"
    
    def __str__(self):
        return self.ad_soyad
    
    def tamamlanan_ezber_sayisi(self):
        return self.ezberkaydi_set.filter(durum='TAMAMLANDI').count()  # Bu satırı düzelt
    
    def ortalama_ders_notu(self):
        from django.db.models import Avg
        ortalama = self.dersnotu_set.aggregate(Avg('not_degeri'))['not_degeri__avg']
        return round(ortalama, 2) if ortalama else 0
    


class Alinti(models.Model):
    quote_text = models.TextField(verbose_name="Alıntı Metni")
    author = models.CharField(max_length=200, blank=True, null=True, verbose_name="Yazar")
    source = models.CharField(max_length=300, blank=True, null=True, verbose_name="Kaynak")
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kategori")
    isActive = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.quote_text[:50] + "..." if len(self.quote_text) > 50 else self.quote_text

    class Meta:
        verbose_name = "Alıntı"
        verbose_name_plural = "Alıntılar"

class DersNotu(models.Model):
    ogrenci = models.ForeignKey(Ogrenci, on_delete=models.CASCADE)
    ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
    not_degeri = models.PositiveSmallIntegerField(default=0)  # 0-100 arası
    yorum = models.TextField(blank=True)
    tarih = models.DateField(default=timezone.now)  # Yeni tarih alanı
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['ogrenci', 'ders', 'tarih']  # Benzersizlik kısıtını güncelle
        verbose_name = "Ders Notu"
        verbose_name_plural = "Ders Notları"
    
    def __str__(self):
        return f"{self.ogrenci} - {self.ders}: {self.not_degeri} ({self.tarih})"

class SinavSonucu(models.Model):
    SINAV_TIPLERI = [
        ('VIZE', 'Vize Sınavı'),
        ('FINAL', 'Final Sınavı'),
        ('QUIZ', 'Quiz'),
        ('PROJE', 'Proje'),
        ('SOZLU', 'Sözlü Sınavı'),
    ]
    
    ogrenci = models.ForeignKey(Ogrenci, on_delete=models.CASCADE)
    ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
    sinav_tipi = models.CharField(max_length=10, choices=SINAV_TIPLERI)
    puan = models.PositiveSmallIntegerField()  # 0-100 arası
    tarih = models.DateField(default=timezone.now)
    aciklama = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Sınav Sonucu"
        verbose_name_plural = "Sınav Sonuçları"
    
    def __str__(self):
        return f"{self.ogrenci} - {self.ders} {self.get_sinav_tipi_display()}: {self.puan}"

class EzberKaydi(models.Model):
    ZORLUK_SEVIYELERI = [
        (1, 'Kolay'),
        (2, 'Orta'),
        (3, 'Zor'),
    ]
    
    DURUM_SECENEKLERI = [
        ('BASLAMADI', 'Başlamadı'),
        ('DEVAM', 'Devam Ediyor'),
        ('TAMAMLANDI', 'Tamamlandı'),
    ]
    
    ogrenci = models.ForeignKey(Ogrenci, on_delete=models.CASCADE)
    sure = models.ForeignKey(EzberSuresi, on_delete=models.CASCADE)
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLERI, default='BASLAMADI')
    baslama_tarihi = models.DateField(null=True, blank=True)
    bitis_tarihi = models.DateField(null=True, blank=True)
    tahmini_bitis = models.DateField(null=True, blank=True)
    gunluk_calisma = models.PositiveSmallIntegerField(default=1, help_text="Günlük çalışma saati")
    zorluk = models.PositiveSmallIntegerField(choices=ZORLUK_SEVIYELERI, default=2)
    yorum = models.TextField(blank=True)
    ilerleme = models.IntegerField(default=0, verbose_name="İlerleme Yüzdesi")

    class Meta:
        unique_together = ['ogrenci', 'sure']
        verbose_name = "Ezber Kaydı"
        verbose_name_plural = "Ezber Kayıtları"
    
    def __str__(self):
        return f"{self.ogrenci} - {self.sure}"
    
    def save(self, *args, **kwargs):
        if self.durum == 'DEVAM' and not self.baslama_tarihi:
            self.baslama_tarihi = timezone.now().date()
        elif self.durum == 'TAMAMLANDI' and not self.bitis_tarihi:
            self.bitis_tarihi = timezone.now().date()
        super().save(*args, **kwargs)