from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Writer,Book
from django.views import generic
from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('/login/?next=%s' % request.path)
    writers=Writer.objects.all()
    books=Book.objects.all().order_by('-id')
    paginator = Paginator(books, 4)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request,'layout/index.html',{'writers':writers,'books':books})

class WriterDetailView(generic.DetailView):
    model = Writer

class BookDetailView(generic.DetailView):
    model = Book

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

