function sumar(n1,n2) {
    return n1+n2;
}
function restar(n1,n2) {
    return n1-n2;
}
function multiplicar(n1,n2) {
    return n1*n2;
}
function dividir(n1,n2) {
    if(n2===0){
        console.log("NO se puede devidir entre 0");
    }else{
        return n1/n2;
    }
}

const objetoOperaciones={}

// exports.sumar=sumar;
// exports.restar=restar;
// exports.multiplicar=multiplicar;
// exports.dividir=dividir;

objetoOperaciones.sumar=sumar;
objetoOperaciones.restar=restar;
objetoOperaciones.dividir=dividir;
objetoOperaciones.multiplicar=multiplicar;

module.exports=objetoOperaciones;