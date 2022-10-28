from django.shortcuts import render, redirect

from music_app_django.web.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
from music_app_django.web.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)
    context = {
        'albums': Album.objects.all(),
    }
    return render(request, 'home_page/home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects. \
        filter(pk=pk). \
        get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects. \
        filter(pk=pk). \
        get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    albums = Album.objects.count()
    context = {
        'profile': profile,
        'albums': albums,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-delete.html', context)


def add_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'home_page/home-no-profile.html', context)
