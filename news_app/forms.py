from django import forms
from .models import Contact , Comment


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

class CommentFrom(forms.ModelForm) :
    
    body = forms.CharField(label="" , widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Comment Here' , 
            'rows' : 4,
            'cols' :50
        }
    ))
    
    class Meta :
        model  = Comment 
        fields = ['body']