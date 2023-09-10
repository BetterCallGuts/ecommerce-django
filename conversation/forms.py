from django import forms

from .models import ConvMessage

class ConvMessageForm(forms.ModelForm):
    class Meta:
        model = ConvMessage
        fields = ('content', )
        widgets = {
            'content' : forms.Textarea(attrs={
                'class' : 'w-full   my-[-40px] rounded-xl border focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all'
            })
        }