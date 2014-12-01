import random

def initTablero(request):
    tab =[]
    for i in range(0,request.session["cantidadTurnos"]):
        row = {}
        huecos = []
        pegs = []
        for j in range (0,request.session["longitudClave"]):
            huecos.append(0)
            pegs.append(0)
        row["huecos"] = huecos
        row["pegs"] = pegs
        tab.append(row)
    return tab

def buscaNegros(request):
    negros = 0
    for key,value in enumerate(request.session["usrinput"]):
        if request.session["clavetmp"][key] == value:
            negros += 1
            request.session["clavetmp"][key] = 0
            request.session["usrinput"][key] = 0
    for n in range(0,negros):
        request.session["tablero"][request.session["turno"]]["pegs"][n] = 1
        request.session.modified = True
    return negros

def buscaBlancos(request):
    blancos=0
    for value in request.session["usrinput"]:
        if value > 0 and value in request.session["clavetmp"]:
            blancos += 1
            primerHueco = request.session["clavetmp"].index(value)
            request.session["clavetmp"][primerHueco] = 0
    if blancos > 0:
        primerHueco = request.session["tablero"][request.session["turno"]]["pegs"].index(0)
        for n in range(0,blancos):
            request.session["tablero"][request.session["turno"]]["pegs"][primerHueco+n]=2
            request.session.modified = True
    return blancos

def process_newgame(request):
    request.session['clave'] = []
    request.session['longitudClave'] = int(request.POST['longitudClave'])
    cantidadColores = int(request.POST['cantidadColores'])
    request.session['listaColores'] = list(xrange(1,cantidadColores+1))
    request.session["cantidadTurnos"] = int(request.POST["cantidadTurnos"])
    request.session["tablero"] = initTablero(request)
    request.session["turno"] = 0
    request.session["end"] = False
    request.session["resultado"] = ''
    request.session["huecowidth"] = (((90*2)/3)/request.session['longitudClave'])
    request.session["pegwidth"] = request.session["huecowidth"]/2
    request.session["btnheight"] = 100/request.session['longitudClave']
    for digito in range(0,request.session["longitudClave"]):
        request.session["clave"].append(random.randint(1,cantidadColores))

def process_usrinput(request,n):
    lineaAct = request.session["tablero"][request.session["turno"]]
    primerHueco = lineaAct["huecos"].index(0)
    request.session["tablero"][request.session["turno"]]["huecos"][primerHueco] = int(n)
    request.session.modified = True
    if primerHueco == len(lineaAct["huecos"])-1:
        request.session["usrinput"] = list(lineaAct["huecos"])
        request.session["clavetmp"] = list(request.session["clave"])
        negros = buscaNegros(request)
        blancos = buscaBlancos(request)
        if negros == request.session["longitudClave"]:
            request.session["resultado"] = "WIN"
            request.session["end"] = True
        elif request.session["turno"] == request.session["cantidadTurnos"]-1:
            request.session["resultado"] = "LOSE"
            request.session["end"] = True
        else:
            request.session["turno"] += 1

def process_undo(request):
    primerHueco = request.session["tablero"][request.session["turno"]]["huecos"].index(0)
    if primerHueco > 0:
        request.session["tablero"][request.session["turno"]]["huecos"][primerHueco-1] = 0
        request.session.modified = True
