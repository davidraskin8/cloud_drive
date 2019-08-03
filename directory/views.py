from django.shortcuts import render
from directory.models import Folder, File

def index(request):
    root_folder = Folder.objects.get(id=1)
    sub_folders = root_folder.folder_set.all()
    files = root_folder.file_set.all()
    file_id_name = [(f.id, f.name) for f in files]
    folder_id_name = [(f.id, f.name) for f in sub_folders]

    all_sub = file_id_name + folder_id_name

    context = {
        'files_folders':all_sub
    }

    return render(request, 'base_generic.html', context=context)
    