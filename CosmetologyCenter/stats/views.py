from django.shortcuts import render
from datetime import date
from main.models import Client
from appointments.models import Appointment
from statistics import mean, median
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

def report(request):
    clients = Client.objects.all().order_by('last_name')

    ages = [calculate_age(client.date_of_birth) for client in clients]

    average_age = mean(ages)
    median_age = median(ages)

    appointments = Appointment.objects.all()
    prices = [appointment.appointmentItem.service.price for appointment in appointments]
    sales_amounts = [appointment.appointmentItem.service.price for appointment in appointments]

    df = pd.DataFrame({'sale_amount': sales_amounts})

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Гистограмма распределения сумм продаж
    axes[0].hist(df['sale_amount'], bins=10, edgecolor='k')
    axes[0].set_xlabel('Сумма продаж')
    axes[0].set_ylabel('Количество заказов')
    axes[0].set_title('Распределение сумм продаж')

    # График зависимости Объема продаж относительно Цен
    axes[1].plot(sales_amounts, prices)
    axes[1].set_xlabel('Объем продаж')
    axes[1].set_ylabel('Цена')
    axes[1].set_title('График зависимости Объема продаж относительно Цен')

    # Сохранение графиков в байтовые объекты
    buffer1 = BytesIO()
    fig.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_base64_hist = base64.b64encode(buffer1.read()).decode('utf-8')
    plt.close(fig)

    context = {
        'average_age': average_age,
        'median_age': median_age,
        'image_base64_hist': image_base64_hist,
    }

    return render(request, 'statistics_report.html', context)

def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age
