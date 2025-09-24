from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="blog"),
    path('search', views.search, name="search"),
    path('<slug:slug>', views.details, name="detay"),
    path('kategori/<str:categorys>', views.getBlogByCategory, name="kategori"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
