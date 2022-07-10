const iniciarServidor=(e)=>{
    
    const url=`https://pokeapi.co/api/v2/pokemon/${document.getElementById("input").value}`;
    fetch(url)
    .then((respuesta)=>respuesta.json())
    .then((datos)=>{
        console.log(datos)
        traerPokemon(datos);
    })
    
    
    e.preventDefault();
};

const traerPokemon=(pokemon)=>{
    document.getElementById("nombre__pokemon").innerHTML=`
        <strong>${pokemon.name}</strong>
    `
    document.getElementById("input").value="";
    let con=document.querySelector(".con");
    let imagen=document.createElement("img");
    imagen.src=pokemon.sprites.front_default;
    con.appendChild(imagen);
}


let btn=document.getElementById("btn").addEventListener("click",iniciarServidor);

