from django.apps import AppConfig
from django.db.models.signals import post_migrate

def setup_initial_data(sender, **kwargs):
    from .models import Ders, EzberSuresi, ElifBaEzberi
    
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
            {'sira': 1, 'ad': '30. Cüz Tamamı', 'tahmini_sure': 14},
            {'sira': 2, 'ad': 'Mülk Suresi', 'tahmini_sure': 7},
            {'sira': 3, 'ad': 'Cin Suresi', 'tahmini_sure': 7},
            {'sira': 4, 'ad': 'Kıyame Suresi', 'tahmini_sure': 7},
            {'sira': 5, 'ad': 'Cuma Suresi', 'tahmini_sure': 7},
            {'sira': 6, 'ad': 'Saff Suresi', 'tahmini_sure': 7},
            {'sira': 7, 'ad': 'Rahman Suresi', 'tahmini_sure': 7},
            {'sira': 8, 'ad': 'Vakia Suresi', 'tahmini_sure': 7},
            {'sira': 9, 'ad': 'Fetih Suresi', 'tahmini_sure': 7},
            {'sira': 10, 'ad': 'Hucurat Suresi', 'tahmini_sure': 7},
            {'sira': 11, 'ad': 'Yasin Suresi', 'tahmini_sure': 7},
            {'sira': 12, 'ad': 'Enfal Suresi', 'tahmini_sure': 7},
            {'sira': 13, 'ad': 'İsra Suresi', 'tahmini_sure': 7},
        ]
        for ezber_data in ezber_sureleri:
            EzberSuresi.objects.get_or_create(**ezber_data)
        print("EzberSuresi tablosu başlangıç verileri ile dolduruldu.")

    if ElifBaEzberi.objects.count() == 0:
        elif_ba_ezberleri = [
            {'sira': 1, 'ad': 'Fatiha Suresi', 'tahmini_sure': 3},
            {'sira': 2, 'ad': 'Bakara 1-5', 'tahmini_sure': 5},
            {'sira': 3, 'ad': 'Rabbena Duaları', 'tahmini_sure': 2},
            {'sira': 4, 'ad': 'Ezan Duası', 'tahmini_sure': 2},
            {'sira': 5, 'ad': 'Kamet', 'tahmini_sure': 2},
            {'sira': 6, 'ad': 'Tesbihat', 'tahmini_sure': 3},
            {'sira': 7, 'ad': 'Amentü Duası', 'tahmini_sure': 2},
            {'sira': 8, 'ad': 'İftitah Duası', 'tahmini_sure': 2},
            {'sira': 9, 'ad': 'Tahiyyat Duası', 'tahmini_sure': 2},
            {'sira': 10, 'ad': 'Salli-barik Duaları', 'tahmini_sure': 3},
            {'sira': 11, 'ad': 'Kunut Duası', 'tahmini_sure': 3},
            {'sira': 12, 'ad': 'Yemek Duası', 'tahmini_sure': 1},
            {'sira': 13, 'ad': 'Başlangıç Duası', 'tahmini_sure': 1},
            {'sira': 14, 'ad': 'İstiğfar Duası', 'tahmini_sure': 1},
            {'sira': 15, 'ad': 'Ayetel Kürsi', 'tahmini_sure': 2},
            {'sira': 16, 'ad': 'Amenerrasülü', 'tahmini_sure': 3},
            {'sira': 17, 'ad': 'La yestevi', 'tahmini_sure': 2},
        ]
        for ezber_data in elif_ba_ezberleri:
            ElifBaEzberi.objects.get_or_create(**ezber_data)
        print("ElifBaEzberi tablosu başlangıç verileri ile dolduruldu.")

class MainprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainproject'
    
    def ready(self):
        # Uygulama hazır olduğunda sinyali bağla
        post_migrate.connect(setup_initial_data, sender=self)