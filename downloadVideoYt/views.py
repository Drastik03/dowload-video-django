from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from downloadVideoYt.forms import FormVideo
from downloadVideoYt.models import VideoModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from pytube import YouTube
def home(request):
  return render(request, 'home.html')

def signUp(request):
  if request.method == 'GET':
        return render(request, 'sign_up.html',{
        'form': UserCreationForm
  })
  else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('create_video')
            except IntegrityError:
                return render(request, 'sign_up.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya registrado'
                })    
        return render(request, 'sign_up.html',{
                    'form': UserCreationForm,
                    'error': 'no coincieden las contraseñas'
                })

def signin(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html',{
        'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, 
                            username=request.POST['username'],
                            password=request.POST['password'])
        if usuario is None:    
            return render(request, 'sign_in.html',{
            'form': AuthenticationForm,
            'error': 'Usuario y contraseña incorrectos'
            })
        else:
            login(request, usuario)
            return redirect('video')
          
@login_required
def close_logout(request):
    logout(request)
    return redirect('home')
  
@login_required
def createVideo(request):
  if request.method == 'GET':
    return render(request,'create_video.html',{
        'form': FormVideo 
    })
  else: 
      try:
        form = FormVideo(request.POST)
        video = form.save(commit=False)
        video.user = request.user
        try:
            video_download_yt = YouTube(video.videoLink)
            resolution = video_download_yt.streams.get_highest_resolution()
            resolution.download("C:/Users/User/Downloads/video.mp4")
            print("Se ha descargado el video de YouTube")
            video.save()  
            return redirect('video')
        except Exception as e:
            print(f"Error al descargar el video de YouTube: {e}")
            print("El enlace de video no es compatible")
            return render(request,'create_video.html',{
                'form': FormVideo 
            })

        
      except ValueError:
        return render(request, "create_video.html",{
          'form': FormVideo,
          'error':'Ingrese un link de Youtube valido'
        })
        
        
@login_required
def videos(request):  
    videos = VideoModel.objects.filter(user=request.user).order_by()
    return render(request, 'list_videos.html', {'videos': videos})



def about(request):
    return render(request, "about.html")