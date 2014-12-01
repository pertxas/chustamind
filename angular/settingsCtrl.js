app.controller("settingsCtrl", function($scope) {
    $scope.cantidadesColores = [2,3,4,5,6,7];
    $scope.cantidadColores  = $scope.cantidadesColores[3];
    $scope.cantidadesTurnos = [5,8,10,12,15,18,20,25];
    $scope.cantidadTurnos  = $scope.cantidadesTurnos[3];
    $scope.longitudesClave = [2,3,4,5,6,7];
    $scope.longitudClave  = $scope.longitudesClave[3];
    $scope.end = true;
    $scope.showSettings = true;
    $scope.start  = function() {
        $scope.showSettings = false;
        $scope.listaColores = [];
        for (var i=1;i<=$scope.cantidadColores;i++)
            {
            $scope.listaColores.push(i)
            }
        $scope.tablero = []
        for (var k=0;k<$scope.cantidadTurnos;k++)
            {
            var fila = {"huecos":[],"pegs":[]}
            for (var l=0;l<$scope.longitudClave;l++)
                {
                fila.huecos.push(0);
                fila.pegs.push(0);
                }
            $scope.tablero.push(fila);
            }
        $scope.turno = 0;
        $scope.end = false;
        $scope.resultado = '';
        $scope.clave = [];
        for (var j=0;j<$scope.longitudClave;j++)
            {
            $scope.clave.push(Math.floor((Math.random() * $scope.cantidadColores) + 1));
            }
    };
    $scope.press = function(color) {
        $scope.click = color;
        var lineaAct = $scope.tablero[$scope.turno];
        var primerHueco = lineaAct.huecos.indexOf(0);
        $scope.tablero[$scope.turno].huecos[primerHueco] = color;
        if (primerHueco == lineaAct.huecos.length-1)
            {
            var usrinput = JSON.parse(JSON.stringify(lineaAct.huecos));
            var clavetmp = JSON.parse(JSON.stringify($scope.clave));
            var negros = 0;
            for (var key=0;key<usrinput.length;key++)
                {
                if (clavetmp[key] == usrinput[key])
                    {
                    negros += 1;
                    clavetmp[key] = 0;
                    usrinput[key] = 0;
                    }
                }
            for (var n=0;n<negros;n++)
                {
                $scope.tablero[$scope.turno].pegs[n] = 1;
                }
            var blancos=0;
            for (var key=0;key<usrinput.length;key++)
                {
                if (usrinput[key] > 0 && clavetmp.indexOf(usrinput[key]) > -1)
                    {
                    blancos += 1;
                    clavetmp[clavetmp.indexOf(usrinput[key])] = 0;
                    }
                }
            for (var p=negros;p<negros+blancos;p++)
                {
                $scope.tablero[$scope.turno].pegs[p] = 2;
                }
            if (negros == $scope.longitudClave)
                {
                $scope.resultado = "WIN";
                $scope.end = true;
                }
            else if ($scope.turno == $scope.cantidadTurnos-1)
                {
                $scope.resultado = "LOSE";
                $scope.end = true;
                }
            else
                {
                $scope.turno += 1;
                }
            }
    };
    $scope.undo  = function() {
        var primerHueco = $scope.tablero[$scope.turno].huecos.indexOf(0);
        if (primerHueco > 0)
            {
            $scope.tablero[$scope.turno].huecos[primerHueco-1] = 0;
            }
    };
    $scope.restart = function() {
        $scope.end = true;
        $scope.showSettings = true;
    };
});
