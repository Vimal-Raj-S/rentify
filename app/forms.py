
from django import forms
from .models import House, Login

class HouseForm(forms.ModelForm):
    class Meta:
        model=House
        fields =('bhk','photo','email','owner_name','mobile_number','address', 'place', 'area')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('email', 'password')
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'