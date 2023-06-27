from django.shortcuts import render

# Create your views here.
from django.db.models.functions import Length
from django.db.models import Q



from app.models import *

def display_topics(request):
    topics = Topic.objects.all()
    topics = Topic.objects.filter(topic_name='cricket')
    topics = Topic.objects.get(topic_name='cricket')
    topics = Topic.objects.exclude(topic_name='cricket')
    topics = Topic.objects.all()[::-1]
    topics = Topic.objects.all()[2::3]
    topics = Topic.objects.all()
   



    d = {'topics':topics}
    return render(request,'display_topics.html',d)


def Webpages(request):
    Webpages=Webpage.objects.all()
    Webpages =Webpage.objects.filter(topic_name='cricket')
    # Webpages =Webpage.objects.get(topic_name='cricket')
    Webpages = Webpage.objects.exclude(topic_name='cricket')
    Webpages = Webpage.objects.exclude(topic_name='Football')
    Webpages = Webpage.objects.all()[::-1]
    Webpages = Webpage.objects.all()[2::3]
    Webpages = Webpage.objects.all().order_by('name')
    Webpages = Webpage.objects.all().order_by('-name')
    Webpages = Webpage.objects.all().order_by(Length('name'))
    Webpages = Webpage.objects.all().order_by(Length('name').desc())
    Webpages=Webpage.objects.all()
    Webpages= Webpage.objects.filter(Q(name='Dhoni')& Q(url__startswith='http'))
    Webpages= Webpage.objects.filter(Q(name='Virat')| Q(url__endswith='in'))
    Webpages= Webpage.objects.filter(name__in=['Akash','Virat'])
    Webpages= Webpage.objects.filter(name__regex='V/w+')
    

    # Webpages=Webpage.objects.all()

    
    


    
    d = {'Webpages':Webpages}
    return render(request,'webpages.html',d)

def AccessRecodes(request):
    AccessRecodes=AccessRecords.objects.all()
    AccessRecodes=AccessRecords.objects.filter(date__gt='1995-01-01')
    AccessRecodes=AccessRecords.objects.filter(date__year__gt='2022')
    AccessRecodes=AccessRecords.objects.filter(date__year__gte='2022')
    AccessRecodes=AccessRecords.objects.filter(date__gte='1995-10-01')
    AccessRecodes=AccessRecords.objects.filter(date__lt='1997-01-01')
    AccessRecodes=AccessRecords.objects.filter(date__lte='1995-10-10')
    AccessRecodes=AccessRecords.objects.filter(date__month='10')
    AccessRecodes=AccessRecords.objects.filter(date__month__gt='05')
    AccessRecodes=AccessRecords.objects.filter(date__month__lt='05')
    AccessRecodes=AccessRecords.objects.filter(date__month__lte='09')
    AccessRecodes=AccessRecords.objects.filter(date__month__gte='06')
    AccessRecodes=AccessRecords.objects.filter(date__day='01')
    AccessRecodes=AccessRecords.objects.filter(date__day__gt='05')
    AccessRecodes=AccessRecords.objects.filter(date__day__gte='10')
    AccessRecodes=AccessRecords.objects.filter(date__day__lt='15')
    AccessRecodes=AccessRecords.objects.filter(date__year__lte='20')
    
  
    d= {'AccessRecodes':AccessRecodes}
    return render(request,'AccessRecodes.html',d)

