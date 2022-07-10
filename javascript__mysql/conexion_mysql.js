const mysql = require('mysql');
// const colors=require("colors");

// const conexion= mysql.createConnection({
//     host : 'localhost',
//     database : 'p',
//     user : 'root',
//     password : 'developer2021',
// });

// conexion.connect((err)=>{
//     if (err===true) {
//         console.error('Error de conexion: ' + err);
//     }
//     console.log('Conectado con el identificador ');
// });


// const consultaSQL="select * from personas";
// conexion.query(consultaSQL,(error, datos)=>{
//     if(error===true){
//         console.log("Error en obtener los datos");
//     }else{
//         console.log(colors.bgWhite.green(datos));
//     }
// })

// conexion.end();


class  Conexion{
    constructor(usuario,contrasenia,puerto,baseDeDato){
        this.usuario=usuario;
        this.contrasenia=contrasenia;
        this.puerto=puerto;
        this.baseDeDato=baseDeDato;
    }
    conectar(){
        const conexion=mysql.createConnection({
            host :this.puerto,
            database : this.baseDeDato,
            user : this.usuario,
            password : this.contrasenia,
        })
        conexion.connect((err)=>{
            if(err===true){
                console.log("Error al conectar");
            }else{
                console.log("conectado");
            }
            conexion.end();
        });
    }
}
const con=new Conexion("root","developer2021","localhost","p");
con.conectar();
