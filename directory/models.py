from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=100, help_text='Enter name of the folder')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=100, help_text='Enter username of creator of folder')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    full_path = models.CharField(max_length=100, blank=True, default='')


    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=100, help_text='Enter name of the file')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=100, help_text='Enter username of creator of file')
    parent = models.ForeignKey(to=Folder, on_delete=models.PROTECT)

    def get_path(instance, filename):
        return '{0}{1}'.format(instance.parent.full_path, filename)

    upload_path = models.FileField(upload_to=get_path)


    def __str__(self):
        return self.name