from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewForm(forms.ModelForm):
    author = forms.CharField(max_length=20, initial='Anonym')
    text = forms.CharField(label='text', widget= forms.TextInput(attrs={'class':'form-input'}), required=False)
    rating = forms.IntegerField(label='rating', widget= forms.NumberInput(attrs={'class': 'form-input', 'min': 0, 'max': 10}),  validators=[
        MinValueValidator(0, message="The number cannot be less than 0"),
        MaxValueValidator(10, message="The number cannot be more than 10")
    ])

    class Meta:
      model = Review
      fields = ['author', 'rating', 'rating'] 