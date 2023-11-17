from django.shortcuts import render, redirect
from services.models import Service, ServiceType
from .models import News, FAQ, Review, Banner, Promotional_code, Job
from .form import ReviewForm
import requests
import logging


logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info('Method home')

    services = Service.objects.all()[:2]
    news = News.objects.first()
    banners = Banner.objects.all()

    return render(request, 'main/home.html', context={'services': services, 'news': news, 'banners': banners})

def about(request):
    return render(request, 'main/about.html')

def price_list(request):
    logger.info('Method price_list')

    service_types = ServiceType.objects.all()
    services_by_type = {}
    
    for service_type in service_types:
        services = Service.objects.filter(service_type=service_type)
        services_by_type[service_type] = services

    return render(request, 'main/price-list.html', {'services_by_type': services_by_type, 'service_types': service_types})


def news(request):
    logger.info('Method news')
    
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})


def faq(request):
    logger.info('Method faq')

    faq = FAQ.objects.all()
    return render(request, 'main/FAQ.html', {'faq': faq})


def privacy_policy(request):
    logger.info('Method privacy_policy')

    return render(request, 'main/privacy_policy.html')


def js_sandbox(request):
    return render(request, 'main/js_sandbox.html')


def reviews(request):
    logger.info('Method reviews')

    reviews = Review.objects.all()
    return render(request, 'main/reviews.html', {'reviews': reviews})


def create_review(request):
    logger.info('Method create_review')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(text=request.POST.get('text'),
                                           rating=request.POST.get('rating'),
                                           author=request.POST.get('author'),
                                           ),

            return redirect('main:rewiews')

    else:
        form = ReviewForm()
        return render(request, "main/create_review.html", {"form": form})
    return redirect('main:home')


def sandbox(request):
    logger.info('Method sandbox')

    joke = requests.get('https://official-joke-api.appspot.com/jokes/random').json()
    dog = requests.get('https://dog.ceo/api/breeds/image/random').json()

    return render(request, 'main/sandbox.html',context={'joke': joke['setup'] + joke['punchline'], 
                                                  'dog': dog['message']})


def promotional_code(request):
    actual_promotional_code = Promotional_code.objects.filter(is_actual=True)
    archive_promotional_code = Promotional_code.objects.filter(is_actual=False)
    return render(request, 'main/promotional_code.html', {'actual_promotional_code': actual_promotional_code, 'archive_promotional_code': archive_promotional_code})


def vacancies(request):
    vacancies = Job.objects.filter(is_actual=True)
    return render(request, 'main/job.html', {'vacancies': vacancies})


def my_view(request):
    logger.debug('Это сообщение с уровнем DEBUG')
    logger.info('Это сообщение с уровнем INFO')
    logger.warning('Это сообщение с уровнем WARNING')
    logger.error('Это сообщение с уровнем ERROR')
    logger.critical('Это сообщение с уровнем CRITICAL')