from django.apps import AppConfig
from django.db.models.signals import post_migrate

def setup_initial_data(sender, **kwargs):
    from .models import Ders, EzberSuresi
    
    # Dersler tablosu boşsa doldur
    if Ders.objects.count() == 0:
        dersler = [
            {'tur': 'AKAID', 'ad': 'Akaid (İtikad)'},
            {'tur': 'FIKIH', 'ad': 'Fıkıh (İbadet)'},
            {'tur': 'SIYER', 'ad': 'Siyer'},
            {'tur': 'TECV', 'ad': 'Tecvid'},
        ]
        for ders_data in dersler:
            Ders.objects.get_or_create(**ders_data)
        print("Dersler tablosu başlangıç verileri ile dolduruldu.")
    
    # EzberSuresi tablosu boşsa doldur
    if EzberSuresi.objects.count() == 0:
        ezber_sureleri = [
            {'sira': 1, 'ad': 'Mülk Suresi', 'tahmini_sure': 7},
            {'sira': 2, 'ad': 'Cin Suresi', 'tahmini_sure': 7},
            {'sira': 3, 'ad': 'Kıyame Suresi', 'tahmini_sure': 7},
            {'sira': 4, 'ad': 'Cuma Suresi', 'tahmini_sure': 7},
            {'sira': 5, 'ad': 'Saff Suresi', 'tahmini_sure': 7},
            {'sira': 6, 'ad': 'Rahman Suresi', 'tahmini_sure': 7},
            {'sira': 7, 'ad': 'Vakia Suresi', 'tahmini_sure': 7},
            {'sira': 8, 'ad': 'Fetih Suresi', 'tahmini_sure': 7},
            {'sira': 9, 'ad': 'Hucurat Suresi', 'tahmini_sure': 7},
            {'sira': 10, 'ad': 'Yasin Suresi', 'tahmini_sure': 7},
            {'sira': 11, 'ad': 'Enfal Suresi', 'tahmini_sure': 7},
            {'sira': 12, 'ad': 'İsra Suresi', 'tahmini_sure': 7},
            {'sira': 13, 'ad': '30. Cüz Tamamı', 'tahmini_sure': 14},
        ]
        for ezber_data in ezber_sureleri:
            EzberSuresi.objects.get_or_create(**ezber_data)
        print("EzberSuresi tablosu başlangıç verileri ile dolduruldu.")

class MainprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainproject'
    
    def ready(self):
        # Uygulama hazır olduğunda sinyali bağla
        post_migrate.connect(setup_initial_data, sender=self)