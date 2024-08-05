from django.urls import path
from page.views import *


urlpatterns = [
    path('',home_view,name='home'),#sayfa ismimizi yazarız home sayfası 
    #path('vizyonumuz/',vision_view,name='vision'),#sayfa ismimizi yazarız vision sayfası 
    #path('hakkimizda/',about_us_view,name='about_us'),#sayfa ismimizi yazarız hakkimizda sayfası 
    #path('iletisim/',contact_us_view,name='contact_us'),#sayfa ismimizi yazarız iletisim sayfası ,
    path('<slug:slug>/',page_view,)
]