#C:\Saurabh\HerokuProject\Project1>virtualenv venvtestdj
#C:\Saurabh\HerokuProject\Project1>venvtestdj\scripts\activate

from django.shortcuts import render

# Create your views here.
def home(request):
 return render(request, 'myapp1/home.html')