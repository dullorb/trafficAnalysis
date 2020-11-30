from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import UploadFileForm
from .imports.XLSX_reader import handle_file
from trafficAnalysis.settings import GOOGLE_MAPS_API_KEY

class UploadFile(View):
    form_class = UploadFileForm
    initial = {'key': 'value'}
    template_name = 'fileUploader/uploader.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class
        content = handle_file(request.FILES['file'])
        return render(request, self.template_name, {'form': form,  'content': content, 'key': GOOGLE_MAPS_API_KEY})
