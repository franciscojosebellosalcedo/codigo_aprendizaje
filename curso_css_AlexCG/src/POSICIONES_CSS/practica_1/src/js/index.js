const btn_acceder=document.querySelector(".hero__btn");
const cerrarModal=document.querySelector(".container__modal__cerrar");
const modal=document.querySelector(".container");


btn_acceder.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.add("modal--vista");
})
cerrarModal.addEventListener("click",(e)=>{
    e.preventDefault();
    modal.classList.remove("modal--vista");
})
