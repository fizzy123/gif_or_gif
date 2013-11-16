import pdb
import logging
import random
import math

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils import timezone

from gif.models import Gif

def display(request):
    gif_num = Gif.objects.count()
    if request.META['REQUEST_METHOD'] == 'GET':
        gif1 = Gif.objects.all()[random.randint(0, gif_num-1)]
        gif2 = Gif.objects.all()[random.randint(0, gif_num-1)]
        while gif1 == gif2:
            gif2 = Gif.objects.all()[random.randint(0, gif_num-1)]
        context = {}
        context['gif1_name'] = gif1.image.name
        context['gif2_name'] = gif2.image.name
        return render(request, 'gif/display.html', context)
    elif request.META['REQUEST_METHOD'] == 'POST':
        win_gif=Gif.objects.get(image=request.POST['win_gif_name'])
        lose_gif=Gif.objects.get(image=request.POST['lose_gif_name'])
        
        #Calculate new RD    
        c = 0.45
        t = 600000
        temp_win_rd = math.sqrt(math.pow(win_gif.rating_deviation,2) + math.pow(c,2)*(timezone.now()-win_gif.last_updated).seconds)
        if temp_win_rd >350:
            temp_win_rd = 350
        temp_lose_rd = math.sqrt(math.pow(lose_gif.rating_deviation,2) + math.pow(c,2)*(timezone.now()-lose_gif.last_updated).seconds)
        if temp_lose_rd > 350:
            temp_lose_rd = 350
        
        #Calculate new rating
        q = math.log(10)/400
        g_win = 1/(math.sqrt(1+3*math.pow(q,2)*math.pow(temp_win_rd,2)/math.pow(math.pi,2)))
        g_lose = 1/(math.sqrt(1+3*math.pow(q,2)*math.pow(temp_lose_rd,2)/math.pow(math.pi,2)))
        e_win = 1/(1+math.pow(10,g_win*(float(win_gif.rating)-float(lose_gif.rating))/(-400)))
        e_lose = 1/(1+math.pow(10,g_lose*(float(lose_gif.rating)-float(win_gif.rating))/(-400)))
        d2_win = 1/(math.pow(q,2)*math.pow(g_win,2)*e_win*(1-e_win))
        d2_lose = 1/(math.pow(q,2)*math.pow(g_lose,2)*e_win*(1-e_lose))
        win_gif.rating = str(float(win_gif.rating) + q/(math.pow(temp_win_rd,-2)+1/d2_win)*g_win*(1-e_win))
        lose_gif.rating = str(float(lose_gif.rating) + q/(math.pow(temp_lose_rd,-2)+1/d2_lose)*g_lose*(0-e_lose))

        #Calculate final RD
        win_gif.rating_deviation = str(math.pow((math.pow(temp_win_rd,-2)+1/d2_win),-0.5))
        lose_gif.rating_deviation = str(math.pow((math.pow(temp_lose_rd,-2)+1/d2_lose),-0.5))
        
        #save
        win_gif.save()
        lose_gif.save()

        return HttpResponseRedirect(reverse('gif:index'))

def rankings(request):
    gifs = Gif.objects.order_by('-rating')
    context = {'gifs':gifs}
    return render(request, 'gif/rankings.html', context)
