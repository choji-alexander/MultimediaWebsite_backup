from django.shortcuts import render, get_object_or_404, redirect
from .models import Image, Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import ImageForm, VideoForm


def home(request):
    return render(request, 'multimedia/home.html')


def image_list(request):
    images = Image.objects.all()
    return render(request, 'multimedia/image_list.html', {'images': images})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'multimedia/video_list.html', {'videos': videos})


def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'multimedia/image_detail.html', {'image': image})


def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'multimedia/video_detail.html', {'video': video})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to home or another view
    else:
        form = UserCreationForm()
    return render(request, 'multimedia/register.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('multimedia:image_list')
    else:
        form = ImageForm()
    return render(request, 'multimedia/upload_image.html', {'form': form})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('multimedia:video_list')
    else:
        form = VideoForm()
    return render(request, 'multimedia/upload_video.html', {'form': form})

