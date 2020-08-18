from django.forms import ModelForm
from registration_app.models import RegisterUser

class UserRegisterForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'