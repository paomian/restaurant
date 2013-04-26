from django import forms
from models import *
import itertools

def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)
def endswith(s,*endings):
    return anyTrue(s.endswith, endings)
class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
    def __init__(self, *args, **kwargs):
        super(DishForm,self).__init__(*args, **kwargs)
