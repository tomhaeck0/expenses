from django import forms


class TransferUploadForm(forms.Form):
    transfer_file = forms.FileField(label='Choose a file containing bank transfers')
