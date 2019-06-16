from django import forms
from .models import Journal
from django.forms import ModelForm




class registerForm(ModelForm):
    class Meta:
    	model = Journal
    	fields = ('Particulars', 'Debit','Credit','date','Accounthead' )
class EditForm(ModelForm):
    class Meta:
    	model = Journal
    	fields = ('Particulars', 'Debit','Credit','date','Accounthead' )