from django.shortcuts import render
from django.http import HttpResponse
from .models import Writer,Book
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("Welcome to hotel transelvania")

def writers(request):
    writers=Writer.objects.all();
    return render(request,'writers/list.html',{'writers':writers}); 

class WriterDetailView(generic.DetailView):
    model = Writer
