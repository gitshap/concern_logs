from django.db.models.base import Model
from django.forms import ModelForm
from concerns.models import Concerns


class ConcernCreationForm(ModelForm):

    class Meta:
        model = Concerns
        fields = '__all__'
