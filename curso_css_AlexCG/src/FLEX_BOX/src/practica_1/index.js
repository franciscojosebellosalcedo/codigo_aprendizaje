const modal=document.querySelector(".modal");
const activarModal=document.querySelector(".con__cabeza__btn");
const cerrarModal=document.querySelector(".modal__cerrar");
const botonIniciarSesion=document.querySelector(".modal__boton");
const form=document.querySelector(".modal__formulario");




activarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.add("modal--activacion");
})
cerrarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.remove("modal--activacion");
})
form.addEventListener("submit",(e)=>{
    e.preventDefault();
    console.log(document.getElementById("correo").value,document.getElementById("contraseña").value);
    form.reset();
    setTimeout(()=>{
        modal.classList.remove("modal--activacion");
    },100)
})
