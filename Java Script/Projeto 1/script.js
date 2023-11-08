const calculo = {
    //alert("Eu sou um alerta");
    //window.alert("Hello World");
    Numero1: 1,
    Numero2: 2,
    Resultado: function(){
        return this.Numero1 + this.Numero2;
    }
}

documento.getElementById("id").innerHTML = calculo.Resultado()
