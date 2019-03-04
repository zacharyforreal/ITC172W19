from django.shortcuts import render, get_object_or_404
from .models import GameType, Game
from .forms import GameForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'reviewapp/index.html')

def reviewapptypes (request):
    type_list=GameType.objects.all()
    return render (request, 'reviewapp/types.html', {'type_list': type_list})

def getgames (request):
    game_list= Game.objects.all()
    return render (request, 'reviewapp/games.html', {'game_list': game_list})

def gamedetails (request, id):
    detail=get_objects_or_404(Game, pk=id)
    context = { 'detail': detail}
    return render (request, 'reviewapp/details.html', context=context)
#form view
@login_required
def newGame(request):
    form=GameForm
    if request.method=='POST':
        form=GameForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GameForm()
    else: 
        form=GameForm()
    return render(request, 'reviewapp/newgame.html', {'form': form})

def loginmessage(request):
    return render(request, 'reviewapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'reviewapp/logoutmessage.html')