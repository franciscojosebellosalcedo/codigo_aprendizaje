const abrirModal=document.querySelector(".usuario__login");
const cerrarModal=document.querySelector(".modal__cerrar");
const modal=document.querySelector(".modal");


abrirModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.add("modal--vista");
    
})
cerrarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.remove("modal--vista")
    
})