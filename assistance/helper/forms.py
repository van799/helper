from django import forms
from .models import Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        #BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
        fields = ('last_name', 'data', 'month')
        #widgets = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

        labels = {
            'month': 'Месяц',
            'last_name': 'Фамилия',
            'data': 'Дата дежурства'
        }

