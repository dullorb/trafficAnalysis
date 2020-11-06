from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .imports.XLSX_reader import handle_file


def index():
    pass


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'])
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/model_form_upload.html', {'form': form})
