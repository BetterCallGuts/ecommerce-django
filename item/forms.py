from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border  '

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
    
        widgets  = {
            'category' :  forms.Select(attrs={
                'class' : INPUT_CLASSES +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            
            'name' :  forms.TextInput(attrs={
                'class' : INPUT_CLASSES  +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            
            'description' :  forms.Textarea(attrs={
                'class' : INPUT_CLASSES +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            'price' :  forms.TextInput(attrs={
                'class' : INPUT_CLASSES + "focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            'image' :  forms.FileInput(attrs={
                'class' : INPUT_CLASSES + "focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
        }
        
        

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'category','name', 'description', 'price', 'image', 'is_sold')
    
        widgets  = {

            'category' :  forms.Select(attrs={
                'class' : INPUT_CLASSES +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            'name' :  forms.TextInput(attrs={
                'class' : INPUT_CLASSES  +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            
            'description' :  forms.Textarea(attrs={
                'class' : INPUT_CLASSES +"focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            'price' :  forms.TextInput(attrs={
                'class' : INPUT_CLASSES + "focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
            'image' :  forms.FileInput(attrs={
                'class' : INPUT_CLASSES + "focus:bg-gray-100 focus:shadow-[0_9px_9px_-4px_#3b71ca] focus:p-7 transition-all"
            }),
        }