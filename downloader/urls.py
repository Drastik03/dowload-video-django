from django.urls import include, path
from django.contrib import admin
from downloadVideoYt import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sign_in/', views.signin, name="sign_in"),
    path('sign_up/', views.signUp,name="sign_up"),
    path('create_video/video/',views.createVideo, name='create_video'),
    path('video/', views.videos, name='video'),
    path('about/',views.about, name='aboutpage'),
    path('logout/', views.close_logout, name="logout")
]
