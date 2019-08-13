from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from directory.models import Folder, File
from .forms import AddFolderForm, UploadFileForm
import json

def index(request):
    # context = retrieve_sub_dir(1)
    context = {}

    if request.method == 'GET':
        form = AddFolderForm()
        context['folder_form'] = form.as_p()

        form = UploadFileForm()
        context['file_form'] = form.as_p()

    # if request.method == 'POST':
    #     form = AddFolderForm(request.POST)

    return render(request, 'base_generic.html', context=context)

def get_sub_dir(request):
    context = retrieve_sub_dir(request.GET.get('id'))

    return HttpResponse(json.dumps(context))

def add_folder(request):
    if request.method == 'POST':
        form = AddFolderForm(request.POST)
        if form.is_valid():
            folder_name = form.cleaned_data['folder_name']
            parent_id = form.cleaned_data['folder_parent_id']

            parent_folder = Folder.objects.get(id=parent_id)
            full_path = parent_folder.full_path + folder_name + '/'
            new_folder = Folder(name=folder_name, parent=parent_folder, owner='davidraskin8', full_path=full_path)
            new_folder.save()
            return HttpResponseRedirect('/')

        else:
            context = {'folder_form' : form}
            print("NOT VALID")

            return render(request, 'base_generic.html', context=context)



def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['new_file']
            parent = Folder.objects.get(id=form.cleaned_data['file_parent_id'])
            file_name = form.cleaned_data['file_name']
        
            new_file = File(upload_path=file, parent=parent, name=file_name)
            new_file.save()
            return HttpResponseRedirect('/')
            
        else:
            context = {'file_form' : form}
            print("NOT VALID")

            return render(request, 'base_generic.html', context=context)

   
        

# Internal function used to retrieve the files and folders in a folder of id=fid
def retrieve_sub_dir(fid):
    root_folder = Folder.objects.get(id=fid)
    sub_folders = root_folder.folder_set.all()
    files = root_folder.file_set.all()
    file_id_name = [(f.id, f.name) for f in files]
    folder_id_name = [(f.id, f.name) for f in sub_folders]

    context = {
        'folders': folder_id_name,
        'files': file_id_name,
        'base_folder_path': root_folder.full_path
    }

    return context


    