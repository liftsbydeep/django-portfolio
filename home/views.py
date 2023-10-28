from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
   context={'name':'"CODE WITH HARRY"','course':'django'}
   return render(request,'home.html',context)
def about(request):
   
     return render(request,'about.html')
def contact(request):
   return render(request,'contact.html')
def projects(request):
   return render(request,'projects.html')