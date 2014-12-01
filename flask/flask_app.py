from flask import Flask, request, url_for, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'regulardesecret'

def buscaNegros():
    negros = 0
    for key,value in enumerate(session["usrinput"]):
        if session["clavetmp"][key] == value:
            negros += 1
            session["clavetmp"][key] = 0
            session["usrinput"][key] = 0
    for n in range(0,negros):
        session["tablero"][session["turno"]]["pegs"][n] = 1
    return negros

def buscaBlancos():
    blancos=0
    for value in session["usrinput"]:
        if value > 0 and value in session["clavetmp"]:
            blancos += 1
    if blancos > 0:
        primerHueco = session["tablero"][session["turno"]]["pegs"].index(0)
        for n in range(0,blancos):
            session["tablero"][session["turno"]]["pegs"][primerHueco+n]=2
    return blancos

def initTablero():
    tab =[]
    for i in range(0,session["cantidadTurnos"]):
        row = {}
        huecos = []
        pegs = []
        for j in range (0,session["longitudClave"]):
            huecos.append(0)
            pegs.append(0)
        row["huecos"] = huecos
        row["pegs"] = pegs
        tab.append(row)
    return tab

def printLinea(data):
    linea = ""
    for n in range(0,len(data["huecos"])):
        linea += '<img class="btn" src="%s" />' % url_for('static',filename='btn%s.png' % data["huecos"][n])
    for n in range(0,len(data["pegs"])):
        linea += '<img class="peg" src="%s" />' % url_for('static',filename='peg%s.png' % data["pegs"][n])
    linea += '<br/>'
    return linea

def printClave():
    linea = ""
    for n in range(0,len(session["clave"])):
        linea += '<img class="btn" src="%s" />' % url_for('static',filename='btn%s.png' % session["clave"][n])
    linea += '<br/>'
    return linea

def lineaEntradaUsuario():
    linea = ""
    for n in range(0,len(entradaUsuario)):
        linea += '<img class="btn" src="%s" />' % url_for('static',filename='btn%s.png' % entradaUsuario[n])
    for n in range(0,session["longitudClave"]-len(entradaUsuario)):
        linea += '<img class="btn" src="%s" />' % url_for('static',filename='btn0.png')
    for n in range(0,session["longitudClave"]):
        linea += '<img class="peg" src="%s" />' % url_for('static',filename='peg0.png')
    linea += '<br/>'
    return linea

def printTablero():
    retorno = ""
    for i in range(0,len(session["tablero"])):
        retorno += printLinea(session["tablero"][i])
    if not session["end"]:
        retorno += botones()
    return retorno

def botones():
    botonera = ""
    for n in range(1,session["cantidadColores"]+1):
        filen = 'btn%s.png' % n
        boton = '<a href="%s" ><img class="btn" src="%s" /></a>' % (url_for('usrinput', n=n),url_for('static',filename=filen))
        botonera += boton
    return botonera

@app.route('/')
def init():
    return render_template('home.html')

@app.route('/newgame', methods=['POST'])
def newgame():
    global session
    session["clave"] = []
    session["longitudClave"] = int(request.form["longitudClave"])
    session["cantidadColores"] = int(request.form["cantidadColores"])
    session["cantidadTurnos"] = int(request.form["cantidadTurnos"])
    session["tablero"] = initTablero()
    session["turno"] = 0
    session["end"] = False
    for digito in range(0,session["longitudClave"]):
        session["clave"].append(random.randint(1,session["cantidadColores"]))
    return render_template('game.html', output=printTablero())

@app.route('/usrinput/<n>')
def usrinput(n):
    global session
    output = ""
    lineaAct = session["tablero"][session["turno"]]
    output += "tabini:"
    for row in session["tablero"]:
        output += str(row)+"\n"
    primerHueco = lineaAct["huecos"].index(0)
    session["tablero"][session["turno"]]["huecos"][primerHueco] = int(n)
    output += "tabfin:"
    for row in session["tablero"]:
        output += str(row)+"\n"
    if primerHueco == len(lineaAct["huecos"])-1:
        output += "OJITO QUE BUSCO"
        session["usrinput"] = list(lineaAct["huecos"])
        session["clavetmp"] = list(session["clave"])
        negros = buscaNegros()
        blancos = buscaBlancos()
        if negros == session["longitudClave"]:
            output = "<h1>WIN"+printClave()+"</h1>"
            session["end"] = True
        elif session["turno"] == session["cantidadTurnos"]-1:
            output = "<h1>LOSE"+printClave()+"</h1>"
            session["end"] = True
        else:
            session["turno"] += 1
    output += printTablero()
    return render_template('game.html', output=output)

@app.route('/debug')
def debug():
    output = "<pre>"
    for row in session["tablero"]:
        output += str(row)+"\n"
    output += "Clave:"+str(session["clave"])+"\n"
    #output += "ClaveTmp:"+str(session["clavetmp"])+"\n"
    #output += "UsrInput:"+str(session["usrinput"])+"\n"
    output += "Turno:"+str(session["turno"])+"\n"
    output += "</pre>"
    return output

