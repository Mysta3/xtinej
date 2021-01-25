from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'url', 'area', 'notes', 'aesthetic', 'country', 'state', 'wholesale', 'black_owned',
                  'minority_owned', 'woman_owned', 'small_business', 'sustainable', 'vegan', 'quarter_used', 'box_used',)
