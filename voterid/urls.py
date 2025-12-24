"""
URL configuration for voterid project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import detals,cards, lst_vote, fronhome, getvoter,st_del
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fronhome, name='home'),
    path('addvoter',detals, name='addvoter'),
    path('card',cards, name= 'card'),
    path('list',lst_vote, name='list'),
    path('getvoter/<int:id>/', getvoter, name='getvoter'),
    path('stu_del/<int:id>/',st_del, name='stu_del'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
