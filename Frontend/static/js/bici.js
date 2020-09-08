function tarjetasBicis(bicis) {
  bicis.map(bici => {

    let contenidoCarta = document.createElement("div");
    contenidoCarta.setAttribute("class", `tarjeta-bici ${bici.id}`);
    //contenidoCarta.setAttribute("id", bici.id);
    contenidoCarta.innerHTML = `
      <a href="#modal" data-toggle="modal" data-target="#modal">
      <img src="data:image/jpeg;base64,${bici.img}" alt="${bici.name}">
      <div class="tarjeta-bici-texto">
        <h3>${bici.name}</h3>
        <p>S/ <span class="precio">${bici.price}</span></p>
      </div>
    </a>  <!-- Tarjeta bici -->
      `;

    let caja = document.querySelector(".bicis-general");
    caja.appendChild(contenidoCarta);
  })
}


 function popupBici(biciCard) {
   
 }

export {
  popupBici,
  tarjetasBicis
};
