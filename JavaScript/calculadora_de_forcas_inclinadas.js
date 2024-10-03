let Inclinacao_Plano = 62.2;
let AtritoC = 0.3;
let AtritoE = 0.6;
let Massa = 52.8;
let Forca = 168.8;
let Inclinacao_Forca = 112.2;
const gravidade = 9.8;

let Px = Massa * gravidade * Math.sin((Inclinacao_Plano * Math.PI)/180);
let Py = Massa * gravidade * Math.cos((Inclinacao_Plano * Math.PI)/180);
let Fx = Forca * Math.cos(((Inclinacao_Forca - Inclinacao_Plano) * Math.PI)/180);
let Fy = Forca * Math.sin(((Inclinacao_Forca - Inclinacao_Plano) * Math.PI)/180);
let N = Py - Fy;
let FatMax = AtritoE * N;
let FatCin = AtritoC * N;
console.log(`Peso: ${(Massa * gravidade).toFixed(2)}`);
console.log(`Peso X: ${Px.toFixed(2)} N`);
console.log(`Peso Y: ${Py.toFixed(2)} N`);
console.log(`Força X: ${Fx.toFixed(2)} N`);
console.log(`Força Y: ${Fy.toFixed(2)} N`);
console.log(`Normal: ${N.toFixed(2)} N`);
console.log(`Força de atrito máximo: ${FatMax.toFixed(2)} N`);
console.log(`Força de atrito cinético: ${FatCin.toFixed(2)} N`);
if(Math.abs(Fx) > FatMax){
    let a = (Fx - FatCin - Px)/ Massa;
    console.log(`Aceleração: ${a.toFixed(2)} m/s^2`);
}else{
    console.log("Aceleração: 0 m/s^2");
}