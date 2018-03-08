"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
from branch import views
from django.views.generic.base import RedirectView

login_forbidden = user_passes_test(lambda u: u.is_anonymous,'/branch/index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('branch/', include('branch.urls')),
    path('', RedirectView.as_view(url='/branch/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', login_forbidden(views.SignUp.as_view()), name='signup'),

]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
