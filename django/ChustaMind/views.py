from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from PIL import Image, ImageDraw
import chustamind

def home(request):
    return render_to_response('home.html', {},
                               context_instance=RequestContext(request))

def newgame(request):
    chustamind.process_newgame(request)
    return render_to_response('game.html', {},
                               context_instance=RequestContext(request))

def game(request):
    return render_to_response('game.html', {},
                               context_instance=RequestContext(request))

def usrinput(request, n):
    chustamind.process_usrinput(request,n)
    return render_to_response('game.html', {},
                               context_instance=RequestContext(request))

def btn(request,n):
    paleta = [
        (128,128,128),
        (255,0,0),
        (255,128,0),
        (255,255,0),
        (0,255,0),
        (0,255,255),
        (0,0,255),
        (255,0,255)
    ]
    im = Image.new("RGBA",(30,30),(0,0,0,0))
    draw = ImageDraw.Draw(im)
    draw.ellipse((5,5,25,25), outline=(0,0,0), fill=paleta[int(n)])
    del draw
    response = HttpResponse(mimetype="image/png")
    im.save(response, "PNG")
    return response

def tst(request):
    return render_to_response('tst.html', {},
                               context_instance=RequestContext(request))

def undo(request):
    chustamind.process_undo(request)
    return render_to_response('game.html', {},
                               context_instance=RequestContext(request))


