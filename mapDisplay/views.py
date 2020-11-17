from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from trafficAnalysis.settings import GOOGLE_MAPS_API_KEY

class MapView(View):
    API_KEY = GOOGLE_MAPS_API_KEY
    def get(self,request):
        return render(request, 'mapDisplay/google_map.html', {'API_KEY': self.API_KEY})
