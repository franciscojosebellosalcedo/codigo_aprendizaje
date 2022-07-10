// //METODO CONCAT


// let array1=[3,2,3,4,5];

// let listaAdicional=[5,6,7,8];

// array1=array1.concat(listaAdicional);


// //METODO EVERY


// function fn(numero) {
//     return numero >1;
// }

// let afirmacion=array1.every(fn)
// if(afirmacion){
//     console.log("true")
// }else{
//     console.log("false");
// }

// //METODO ESTRIES

// let iteracion=array1.entries();
// for (let i = 0; i < array1.length; i++) {
//     console.log(iteracion.next().value);
// }
// 
// 


//METODO FILL


// let array2=[1,2,3,4,5,6];
// array2.fill("hola",1,4);
// console.log(array2)

//METODO FILTER

// let array3=[0,2,3,4,5,6];
// let resultado=array3.filter((numeros)=>{
//     if(numeros>1){
//         return numeros;
//     }
// })
// console.log(resultado)


//METODO FIND

// let array4=[1,2,3,4,5,6];
// let resultado=array4.find((numeros)=>{if(numeros>3){return numeros}});
// console.log(resultado)

//METODO findIndex

// let array5=[1,2,3,4,5,6];
// let resultado=array5.findIndex(numero=> numero>5);
// console.log(resultado)

//METODO FLAT

// let array6=[1,[4,5,6,7,8]];
// let resultado=array6.flat()
// console.log(resultado)


//METODO forEach

// let array7=[1,2,3,4,5,6,7,8];
// array7.forEach((n)=>{
//     if(n%2===0){
//         console.log(n,"hola dario")
//     }else{
//         console.log(n,"hola pacho")
//     }
// })


//METODO includes

// let array8=[1,0,2,3,4,5];
// if(array8.includes("dario")){
//     console.log("dario si esta en la lista")
// }else{
//     console.log("dario no esta en la lista")
// }


//METODO indexOf


// let array9=[1,2,3,4,5];
// let resultado=array9.indexOf(1);
// console.log(resultado)


//METODO join


// let array=[1,2,3,4,5];
// let resultado=array.join()
// console.log(resultado);


//METODO keys


// let array=[1,2,3,4,5];
// let resultado=array.keys()
// for (const key of resultado) {
//     console.log(key);
// }


//METODO lastIndexOf


// let array=[1,2,5,3,4,5,5];
// let resultado=array.lastIndexOf(5)
// console.log(resultado);


//METODO pop


// let array=[1,2,3,4,5];
// let resultado=array.pop()
// console.log(resultado);
// console.log(array);


//METODO reduce


// let array=[1,2,9];
// let acumulador=0;
// let resultado=array.reduce(
//     (acumulador,n)=> { return acumulador + n}
// );
// console.log(resultado);


//METODO reduceRight


// let array=[1,2,9];
// let acumulador=0;
// let resultado=array.reduceRight((acumulador,n)=>(acumulador+n))
// console.log(resultado);


//METODO reverse


// let array=[1,2,3,4,5];
// let resultado=array.reverse();
// console.log(array)


//METODO shift


// let array=[1,2,3,4,5];
// let resultado=array.shift()
// console.log(resultado)
// console.log(array)



//METODO slice


// let array=[1,2,3,4,5];
// let resultado=array.slice(0,3)
// console.log(resultado)
// console.log(array)




