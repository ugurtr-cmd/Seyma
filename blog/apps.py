from django.apps import AppConfig
from django.db.models.signals import post_migrate

def setup_blog_data(sender, **kwargs):
    try:
        from .models import category
        
        # Kategoriler tablosu boşsa doldur
        if category.objects.count() == 0:
            kategoriler = [
                {'name': 'Kuran Eğitimi', 'slug': 'kuran-egitimi'},
                {'name': 'Hafızlık', 'slug': 'hafizlik'},
                {'name': 'Dini Bilgiler', 'slug': 'dini-bilgiler'},
                {'name': 'Dua ve İbadet', 'slug': 'dua-ve-ibadet'},
                {'name': 'Siyer ve Tarih', 'slug': 'siyer-ve-tarih'},
                {'name': 'Aile ve Toplum', 'slug': 'aile-ve-toplum'},
                {'name': 'Genel', 'slug': 'genel'},
            ]
            for kategori_data in kategoriler:
                category.objects.get_or_create(
                    slug=kategori_data['slug'],
                    defaults={'name': kategori_data['name']}
                )
            print("✅ Kategoriler tablosu başlangıç verileri ile dolduruldu.")
            
    except Exception as e:
        print(f"❌ Blog data loading failed: {e}")

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    def ready(self):
        post_migrate.connect(setup_blog_data, sender=self)
