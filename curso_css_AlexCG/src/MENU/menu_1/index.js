const abrirModal=document.querySelector(".btn_abrir_modal");
const modal=document.querySelector(".modal__container");
const cerrarModal=document.querySelector(".modal__btn__cerrar");
const cuerpo=document.querySelector(".body");

cerrarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.remove("modal__vista");
    cuerpo.style.backgroundColor = '#fff';
})
abrirModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.add("modal__vista");
    cuerpo.style.backgroundColor = '#FF00FF';
;})