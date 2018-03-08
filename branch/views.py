from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Writer,Book
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    return HttpResponse("Welcome to hotel transelvania")


def writers(request):
    writers = Writer.objects.all()
    return render(request, 'writers/list.html', {'writers': writers})


class WriterDetailView(generic.DetailView):
    model = Writer


class BookDetailView(generic.DetailView):
    model = Book

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
