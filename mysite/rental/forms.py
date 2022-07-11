from django import forms
from .models import putroom


class data(forms.ModelForm):    
    

    def __init__(self, *args, **kwargs):
       super(data, self).__init__(*args, **kwargs)
       self.fields['ownername'].widget.attrs['readonly'] = True
       self.fields['owneremail'].widget.attrs['readonly'] = True
       self.fields['ownerphone'].widget.attrs['readonly'] = True

    class Meta:
        model = putroom
        
        fields='__all__'
     