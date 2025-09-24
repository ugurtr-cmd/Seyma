from django.apps import AppConfig
from django.db.models.signals import post_migrate

def setup_blog_data(sender, **kwargs):
    try:
        from .models import category
        
        kategoriler = [
            {'name': 'Genel', 'slug': 'genel'},
            {'name': 'Dini', 'slug': 'dini'},
            {'name': 'Edebi', 'slug': 'edebi'},
            {'name': 'Felsefi', 'slug': 'felsefi'},
            {'name': 'Şiir', 'slug': 'siir'},
            {'name': 'Motivasyon', 'slug': 'motivasyon'},
            {'name': 'Bilim', 'slug': 'bilim'},
        ]

        for kategori_data in kategoriler:
            category.objects.get_or_create(
                slug=kategori_data['slug'],
                defaults={'name': kategori_data['name']}
            )

        print("✅ Kategoriler tablosu başlangıç verileri güncellendi.")
            
    except Exception as e:
        print(f"❌ Blog data loading failed: {e}")


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    
    def ready(self):
        post_migrate.connect(setup_blog_data, sender=self)
