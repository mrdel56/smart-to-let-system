from django.shortcuts import render, HttpResponse,redirect
from django.views import View
from .models import Property
def home (request):
    return render(request, 'home.html')



class CategoryView(View):
    def get(self,request,val):
        property = Property.objects.filter(category=val)
        return render(request, 'category.html',locals())
