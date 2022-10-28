from django.shortcuts import render, redirect

from games_app.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditeForm, \
    ProfileDeleteForm
from games_app.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    if profile is None:
        return index(request)

    context = {
        'games': games,
    }
    return render(request, 'core/dashboard.html', context)


def index(request):
    hide_nav_links = False

    if get_profile() is not None:
        hide_nav_links = True

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'hide_nav_links': hide_nav_links,

    }
    return render(request, 'core/home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    all_games_rating = [game.rating for game in games]
    if games:
        average_rating = sum(all_games_rating) / games.count()
    else:
        average_rating = 0.0

    context = {
        'profile': profile,
        'games': games.count(),
        'average_rating': average_rating,
        
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):

    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditeForm(instance=profile)
    else:
        form = ProfileEditeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


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

    return render(request, 'profile/delete-profile.html', context)


def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'game/edit-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }

    return render(request, 'game/details-game.html', context)


def delete_game(request, pk):

    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/delete-game.html', context)
