from django import forms

class Add_Friend_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
    }
    title_attrs = {
        'type': 'text',
        'class': 'friend-name',
        'placeholder':'Masukkan Nama'
    }
    description_attrs = {
        'type': 'url',
        'class': 'friend-url',
        'placeholder':'Masukkan url'
    }

    name = forms.CharField(label='', required=True, max_length=32, widget=forms.TextInput(attrs=title_attrs))
    url = forms.URLField(label='', required=True, widget=forms.Textarea(attrs=description_attrs))
