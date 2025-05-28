from django import forms


class UploadTextForm(forms.Form):
    file = forms.FileField()
