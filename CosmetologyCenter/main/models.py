from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=20, help_text='Enter first name')
    last_name = models.CharField(max_length=20, help_text='Enter last name')
    date_of_birth = models.DateField(help_text="Enter date of birth")
    email = models.EmailField(help_text="Enter email")
    town = models.CharField(help_text="Enter town", max_length=30, default='Minsk')
    phone_number = models.CharField(max_length=25, help_text='Enter phone number', validators=[RegexValidator(
        regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
        message='Format +375 (29) XXX-XX-XX')])

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class News(models.Model):
    title = models.CharField(max_length=200, help_text="Enter title")
    essence = models.CharField(max_length=200, help_text="Enter essence")
    photo = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(help_text="Enter description")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('main:news', args=[str(self.id)])


class FAQ(models.Model):
    question = models.CharField(max_length=150, help_text="Enter question")
    answer = models.TextField(help_text="Enter answer")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('main:FAQ', args=[str(self.question)])


class Review(models.Model):
    text = models.TextField(help_text="Enter review")
    rating = models.IntegerField(help_text="Enter rating from 0 to 10",  validators=[
        MinValueValidator(0, message="The number cannot be less than 0"),
        MaxValueValidator(10, message="The number cannot be more than 10")
    ])
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, default='')
    def get_absolute_url(self):
        return reverse('main:reviews', args=[str(self.text)])

    def __str__(self):
        return f'{self.text}'