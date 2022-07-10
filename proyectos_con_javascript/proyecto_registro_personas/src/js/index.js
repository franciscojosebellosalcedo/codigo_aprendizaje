// class Persona {
//     constructor(nombre, apellido, documento, edad) {
//         this.nombre = nombre;
//         this.apellido = apellido;
//         this.documento = documento;
//         this.edad = edad;
//     }
// }
// class Registro {
//     agregarPersona(persona) {
//         let contenedor = document.getElementById('contenedor');
//         let elemento = document.createElement('div');
//         elemento.innerHTML = `
//         <div>
//         <br>
//             <button id='eliminar' color='danger'>Eliminar ${persona.nombre}</button>
//             <p>
//                 <strong>Nombre:</strong> ${persona.nombre}<br> 
//                 <strong>Apellidos:</strong>${persona.apellido}<br>
//                 <strong>Documento:</strong>${persona.documento}<br>
//                 <strong>Edad:</strong>${persona.edad}
//             </p>
//         </div>
//     `;
//         contenedor.appendChild(elemento);
//     }
//     eliminarPersona(){

//     }
// }
// document.getElementById('boton').addEventListener('click', (e) => {
//     let nombre = prompt('Ingrese su nombre:');
//     let apellido = prompt('Ingrese su apellido:');
//     let documento = prompt('Ingrese su documento:');
//     let edad = prompt('Ingrese su edad:');

//     let persona=new Persona(nombre,apellido,documento,edad)
//     let rP=new Registro();
//     rP.agregarPersona(persona);

//     e.preventDefault();
// })
let cantidad=0;
document.getElementById('boton').addEventListener('click',(e)=>{
    let nombre=document.getElementById('nombre').value;
    let apellido=document.getElementById('apellido').value;
    let documento=document.getElementById('documento').value;
    let edad=document.getElementById('edad').value;
    if(nombre=="" || apellido=="" || documento==0 || edad==0 ){
        alert("Ingrese los datos por favor..");
    }else{
        let contenedor=document.getElementById('contenedor');
        let elemento=document.createElement('div');
        elemento.innerHTML=`
        <div>
            <div class="card-header">
                <strong>Persona</strong> ${cantidad+=1}
            </div>
            <div class="card-body">
                <p>
                    <strong>Nombre:</strong> ${nombre}
                    <strong>Apellido:</strong> ${apellido}
                    <strong>Documento:</strong> ${documento}
                    <strong>Edad:</strong> ${edad}    
                </p>
            </div>
            <button class="btn-danger">Eliminar a ${nombre}</button>
        </div>
        `;
        contenedor.appendChild(elemento);
        document.getElementById('nombre').value="";
        document.getElementById('apellido').value="";
        document.getElementById('documento').value="";
        document.getElementById('edad').value="";
    }
    e.preventDefault();
});

