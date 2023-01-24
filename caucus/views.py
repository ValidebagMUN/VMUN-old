from django.conf.urls import handler404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Caucus
# Create your views here.


@login_required(login_url='/login/')
def mod_view(request, *args, **kwargs):
    caucus = Caucus.objects.get(id=id)
    if caucus.type != 'MOD':
        if caucus.type == 'UNM':
            return redirect('caucus:unmod', id=id)
        elif caucus.type == 'SMM':
            return redirect('caucus:semimod', id=id)
    else:
        exception = 'Caucus Type Error'
        handler404(request, exception)
    context = {
        'id': id,
    }
    return render(request, 'mod.html', context)


@login_required(login_url='/login/')
def unmod_view(request, *args, **kwargs):
    caucus = Caucus.objects.get(id=id)
    if caucus.type != 'UNM':
        if caucus.type == 'MOD':
            return redirect('caucus:mod', id=id)
        elif caucus.type == 'SMM':
            return redirect('caucus:semimod', id=id)
    else:
        exception = 'Caucus Type Error'
        handler404(request, exception)
    context = {

    }
    return render(request, 'unmod.html', context)


@login_required(login_url='/login/')
def semimod_view(request, *args, **kwargs):
    caucus = Caucus.objects.get(id=id)
    if caucus.type != 'SMM':
        if caucus.type == 'MOD':
            return redirect('caucus:mod', id=id)
        elif caucus.type == 'UNM':
            return redirect('caucus:unmod', id=id)
    else:
        exception = 'Caucus Type Error'
        handler404(request, exception)
    context = {
        'id': id,
    }
    return render(request, 'semimod.html', context)


@login_required(login_url='/login/')
def create_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'create.html', context)