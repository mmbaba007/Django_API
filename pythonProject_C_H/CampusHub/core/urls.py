from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import ItemsViewSet, SignupView, LoginView, CategoryView, LogoutView

router1 = routers.DefaultRouter()
router1.register(r'items/', ItemsViewSet) #this is the API to be refrenced in the frontend


urlpatterns = [
    path('', include(router1.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('category/', CategoryView.as_view(), name='categories'),
]

