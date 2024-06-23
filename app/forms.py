from django import forms
from django.forms import fields
from .models import Contacto, Producto, Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    # nombre= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # correo=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    
    class Meta:
        model = Contacto
        # fields = ["nombre","correo","mensaje"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FeedbacksForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name", "last_name","email","password1","password2"]

# ----------------------------------
#             Chuly
#     GitHub: https://github.com/victoryanezn
#     Discord: chuly2005#0
# ---------------------------------- 