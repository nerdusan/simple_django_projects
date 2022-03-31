from django.forms import ModelForm
from bincom.models import MyModel

class PuChoiceForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['pu']