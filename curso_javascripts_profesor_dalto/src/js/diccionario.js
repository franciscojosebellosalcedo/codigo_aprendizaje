
let materias={
    fisica:["profesor miguel","juan","pedro"],
    castellano:["profesor machado","luis","francisco"],
    sociales:["profesor gomez","juan","loco","marioo"]
}
function inscribirAlumno(materia,nombreAlumno) {
    let listaMate=materias[materia];
    let profesor=listaMate.shift()
    let cantidadDeAlumno=listaMate.length;
    if(cantidadDeAlumno>=20){
        document.write(`${nombreAlumno} la cantidad de alumno ya esta completa .`);
    }else{
        listaMate.push(nombreAlumno);
        document.write(`${nombreAlumno} te has inscrito y te hemos añadido en la materia ${materia} y tu profesor sera ${profesor} `);
    }
}               
// inscribirAlumno("castellano","cofla"),"<br>";

