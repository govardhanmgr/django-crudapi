"""
URL configuration for djangoAuth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet,PostModelViewSet



router = DefaultRouter()
router.register("",PostViewSet,"posts")
model_router=DefaultRouter()
model_router.register("",PostModelViewSet,"posts-model-viewset")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('post-viewsets/',include(router.urls)),
    path('post-model-viewsets/',include(model_router.urls)),
    path('auth/',include('accounts.urls')),

    
]
