from django import forms

class AddFolderForm(forms.Form):
    folder_name = forms.CharField(label='Folder Name', max_length=100)
    parent_id = forms.CharField(widget=forms.HiddenInput)
