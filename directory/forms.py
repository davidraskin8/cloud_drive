from django import forms
from directory.models import File

class AddFolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=100)
    folder_parent_id = forms.CharField(widget=forms.HiddenInput)

class UploadFileForm(forms.Form):
    file_name = forms.CharField(label='File Name', max_length=100)
    file_parent_id = forms.CharField(widget=forms.HiddenInput)
    new_file = forms.FileField(label='New File')
