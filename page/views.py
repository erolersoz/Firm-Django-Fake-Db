from django.shortcuts import render
from django.http import Http404
from random import randint
from .fake_db.pages import FAKE_DB_PAGES


# FAKE_DB_PROJECTS=[
#     f"http://picsum.photos/id/{id}/100/80" for id in range(21,29)
# ]
FAKE_DB_CAROUSEL=[
    f"http://picsum.photos/id/{id}/1200/400" for id in range(24,28)
]

def home_view(request):
    #print(request)sorguyu belirtiyor
    #context={"platform":f"Django platformu kullanildi ve  randint ile dönen veri: {randint(1,50)}"}#html dosyamızı döndürdük
    context=dict(
                # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
                FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL)#html dosyamızı döndürdük
    return render(request,"page/home_page.html",context)

def about_us_view(request):
    page_title="Hakkimizda"
    hero_content="lorem ipsum color abset parasa sjahahjsa"
    context={
        "page_title":page_title
    }
    context['hero_content']=page_title
                #   FAKE_DB_PROJECTS=FAKE_DB_PROJECTS)
    return render(request,"page/about_us.html",context)

def contact_us_view(request):
    page_title="iletisim"
    hero_content="lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor lorem ipsum dolor"
    context=dict(page_title=page_title,
                 hero_content=hero_content,)
                #  FAKE_DB_PROJECTS=FAKE_DB_PROJECTS)#tanımlama
    return render(request,"page/contact_us.html",context)

def vision_view(request):
    page_title="vizyonumuz"
    context=dict(page_title=page_title,)
                #   FAKE_DB_PROJECTS=FAKE_DB_PROJECTS)
    return render(request,"page/vision.html",context)

def page_view(request,slug):
    result=list(filter(lambda x: (x['url'] == slug), FAKE_DB_PAGES))
  
   
   
    if result:
        context=dict(
            page_title=result[0]['title'],
            # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
            detail=result[0]['detail'],
        )
        return render(request,"page/page_detail.html",context)#projenin bulunmadaığını dönderdi
    raise Http404
