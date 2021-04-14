from django.forms import ModelForm
from .models import RegisterUser


class UserRegisterForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
