from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import yazi,category
from django.core.paginator import Paginator
import math
from django.utils.html import strip_tags
from django.db.models import F

# Create your views here.

def home(request):
    yazilar = yazi.objects.filter(isActive=True).order_by('-id')
    kategoriler = category.objects.all()
    return render(request, 'blog.html', {
        'yazilar':yazilar,
        'kategoriler':kategoriler
    })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        yazilar = yazi.objects.filter(isActive=True,title__contains=q)
    
    return render(request, 'search.html', {
        'yazilar':yazilar,
        'q':q
    })

def details(request, slug):
    yazilar = get_object_or_404(yazi, slug=slug)
    
    # Görüntüleme sayısını artır
    
    # Okuma süresini hesapla (200 kelime/dk varsayımı)
    kelime_sayisi = len(strip_tags(yazilar.description).split())
    okuma_suresi = max(1, math.ceil(kelime_sayisi / 200))
    
    # Benzer yazıları getir (aynı kategorideki son 3 yazı)
    benzer_yazilar = yazi.objects.filter(
        isActive=True
    ).exclude(slug=slug).order_by('-id')[:3]
    
    return render(request, 'details.html', {
        'yazilar': yazilar,
        'benzer_yazilar': benzer_yazilar,
        'okuma_suresi': okuma_suresi
    })


def getBlogByCategory(request, categorys):
    yazilar = yazi.objects.filter(category__slug=categorys, isActive=True)
    kategoriler = category.objects.all()
    paginator = Paginator(yazilar, 6)
    page = request.GET.get('page', 1)
    text = paginator.get_page(page)
    return render(request, 'blog.html', {
        'yazilar':text,
        'kategoriler':kategoriler,
        'selectCategory': categorys,
    })