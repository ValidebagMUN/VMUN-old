from django.core.exceptions import BadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Caucus
# Create your views here.


@login_required(login_url='/login/')
def caucus_view(request, *args, **kwargs):
    caucus = Caucus.objects.get(id=id)
    context = {
        'id': id,
    }
    if caucus.type == 'MOD':
        return render(request, 'mod.html', context)
    elif caucus.type == 'UNM':
        return render(request, 'unmod.html', context)
    elif caucus.type == 'SMM':
        return render(request, 'semimod.html', context)
    else:
        raise BadRequest('Invalid Caucus Type')
    


@login_required(login_url='/login/')
def create_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'create.html', context)