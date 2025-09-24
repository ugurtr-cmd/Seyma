from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="home"),
    path('hakkimda', views.about, name="hakkimda"),
    path('iletisim', views.iletisim ,name="iletisim"),
    path('arama-motoru/', views.arama_motoru, name='arama_motoru'),
    path('admin-paneli/', views.admin_dashboard, name='admin-dashboard'),
    path('alintilar/', views.tum_alintilar, name='tum-alintilar'),

    path('admin-paneli/alinti-yaz/', views.alinti_yaz, name='alinti-yaz'),
    path('admin-paneli/alintilar/', views.alinti_listesi, name='alinti-listesi'),
    path('admin-paneli/alintilar/<int:id>/', views.alinti_duzenle, name='alinti-duzenle'),
    path('admin-paneli/alintilar/sil/<int:id>/', views.alinti_sil, name='alinti-sil'),


    path('admin-paneli/backup-data/', views.backup_data, name='backup_data'),
    path('admin-paneli/backup-list/', views.list_backups, name='list_backups'),
    path('admin-paneli/restore-data/', views.restore_data, name='restore_data'),
    path('admin-paneli/restore-progress/', views.restore_progress_api, name='restore_progress'),
    path('admin-paneli/download-backup/<str:filename>/', views.download_backup, name='download_backup'),
    path('admin-paneli/delete-backup/<str:filename>/', views.delete_backup, name='delete_backup'),
    

    path('admin-paneli/yazi-yaz/', views.yaziyaz, name='admin-paneli'),
    path('admin-paneli/yazilar/', views.admin_yazi_listesi, name='admin-yazi-listesi'),
    path('admin-paneli/yazilar/<int:id>', views.yazi_guncelle, name='yazi-guncelle'),
    path('admin-paneli/yazilar/sil/<int:id>/', views.admin_yazi_sil, name='yazi-sil'),
    path('admin-paneli/ogrenciler/', views.ogrenci_listesi, name='ogrenci_listesi'),
    path('admin-paneli/ogrenci/ekle/', views.ogrenci_ekle, name='yeni_ogrenci'),
    path('admin-paneli/ogrenci/duzenle/<int:id>/', views.ogrenci_duzenle, name='ogrenci_duzenle'),
    path('admin-paneli/ogrenci/<int:id>/not/', views.ogrenci_not_ekle, name='ogrenci_not_ekle'),
    path('ogrenci/sil/<int:ogrenci_id>/', views.ogrenci_sil, name='ogrenci_sil'),
    path('ogrenci/<int:id>/ezber-ekle/', views.ezber_ekle, name='ezber_ekle'),
    path('ogrenci/<int:id>/ders-notu-ekle/', views.ders_notu_ekle, name='ders_notu_ekle'),
    path('ogrenci/<int:id>/sinav-sonucu-ekle/', views.sinav_sonucu_ekle, name='sinav_sonucu_ekle'),
    path('ogrenci/export/excel/', views.export_ogrenci_listesi_excel, name='export_ogrenci_listesi_excel'),
    path('ogrenci/<int:id>/export/excel/', views.export_ogrenci_detay_excel, name='export_ogrenci_detay_excel'),
    path('ezber-tamamla/<int:id>/<int:ezber_id>/', views.ezber_tamamla, name='ezber_tamamla'),
    path('admin-paneli/ogrenci/detay/<int:id>/', views.ogrenci_detay, name='ogrenci_detay'),
    path('giris', views.login,name="login"),
    path('admin-paneli/parola_guncelle', views.change_password,name="parola_guncelle"),
    path('cikis', views.user_logout, name="cikis"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
