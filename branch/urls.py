from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('writers/', views.writers, name='writers'),
    path('writer/<int:pk>', views.WriterDetailView.as_view(), name='writer-detail'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

]
