from django.shortcuts import render
from .models import Actus,Question,Services,Evenement,membres

def Accueil(request):
    actus=Actus.objects.all()
    questions=Question.objects.all().order_by('IdQuest')[:5]
    services=Services.objects.all().order_by('Idservices')[:4]
    evenements=Evenement.objects.all()
    membre=membres.objects.all().order_by('id'[:4])
    return render(request, 'pages/index.html',
           {
               'Actus':actus,
               'questions':questions,
               'services':services,
               'evenements':evenements,
               'membres':membre
           })
def evenements(request):
    evenements=Evenement.objects.all()
    return render(request,'pages/Evenements.html',{'evenements':evenements})
def services(request):
    services=Services.objects.all()
    return render(request,'pages/Services.html',{'services':services})
def blog(request):
    actus=Actus.objects.all()
    return render(request,'pages/Blog.html',{'Actus':actus})
def Apropos(request):
    membre=membres.objects.all()
    return render(request,'pages/Apropos.html',{
        'membres':membre
    })
def carte(request):
    return render(request,'pages/carte.html') 
