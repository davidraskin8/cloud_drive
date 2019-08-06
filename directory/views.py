from django.shortcuts import render
from django.http import HttpResponse
from directory.models import Folder, File
import json

def index(request):
    context = retrieve_sub_dir(1)

    return render(request, 'base_generic.html', context=context)

def get_sub_dir(request):
    context = retrieve_sub_dir(request.GET.get('id'))

    return HttpResponse(json.dumps(context))

# Internal function used to retrieve the files and folders in a folder of id=fid
def retrieve_sub_dir(fid):
    root_folder = Folder.objects.get(id=fid)
    sub_folders = root_folder.folder_set.all()
    files = root_folder.file_set.all()
    file_id_name = [(f.id, f.name) for f in files]
    folder_id_name = [(f.id, f.name) for f in sub_folders]

    context = {
        'folders': folder_id_name,
        'files': file_id_name
    }

    return context

    