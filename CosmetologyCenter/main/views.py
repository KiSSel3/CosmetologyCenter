from django.shortcuts import render, redirect
from services.models import Service, ServiceType
from .models import News, FAQ, Review
from .form import ReviewForm
import requests

# Create your views here.
def home(request):
    services = Service.objects.all()[:2]
    news = News.objects.first()

    return render(request, 'main/home.html', context={'services': services, 'news': news})

def about(request):
    return render(request, 'main/about.html')

def price_list(request):
    service_types = ServiceType.objects.all()
    services_by_type = {}
    
    for service_type in service_types:
        services = Service.objects.filter(service_type=service_type)
        services_by_type[service_type] = services

    return render(request, 'main/price-list.html', {'services_by_type': services_by_type, 'service_types': service_types})


def news(request):
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})


def faq(request):
    faq = FAQ.objects.all()
    return render(request, 'main/FAQ.html', {'faq': faq})


def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(text=request.POST.get('text'),
                                           rating=request.POST.get('rating'),
                                           author=request.POST.get('author'),
                                           ),

            return redirect('main:reviews')

    else:
        form = ReviewForm()
        return render(request, "create_review.html", {"form": form})
    return redirect('main:home')


def sandbox(request):
    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    dog = requests.get('https://dog.ceo/api/breeds/image/random').json()

    return render(request, 'main/sandbox.html',context={'joke': joke['setup'] + joke['punchline'], 
                                                  'dog': dog['message']})
