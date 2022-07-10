const abrirModal=document.querySelector(".usuario__login");
const cerrarModal=document.querySelector(".modal__login__cerrar");
const botonIniciarSesion=document.querySelector(".modal__login__iniciar");
const modal=document.querySelector(".container__modal__login");


abrirModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.add("modal--vista")
})
cerrarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.remove("modal--vista")
})
botonIniciarSesion.addEventListener("click",(e)=>{
    e.preventDefault();
    
})