function tarjetasBicis(bicis) {
  bicis.map(bici => {
    /*let nombre = document.createElement("p");
      nombre.innerHTML = `Nombre de bicicleta ${i + 1}: ${bici.name}`;
      let precio = document.createElement("p");
      precio.innerHTML = `Precio de la bicicleta: ${bici.price}`;
      let color = document.createElement("p");
      color.innerHTML = `Color de la bici: ${bici.colors}`;
      let imagen = document.createElement("img");
      imagen.src = "data:image/jpeg;base64," + bici.img;
      imagen.width = "200"
  
      let caja = document.querySelector(".site-footer");
  
      caja.append(nombre);
      caja.append(precio);
      caja.appendChild(color);
      caja.appendChild(imagen);*/
    //debugger;
    /*let nombre = document.querySelector(".tarjeta-bici h3");
    nombre.innerHTML = bici.name;
    let precio = document.querySelector(".tarjeta-bici p span");
    precio.innerHTML = bici.price;
    let imagen = document.querySelector(".tarjeta-bici img");
    imagen.src = `data:image/jpeg;base64,${bici.img}`;

    let biciCard = document.createElement("div");
    biciCard.setAttribute("class", "tarjeta-bici");
    biciCard.append(imagen);
    biciCard.append(nombre);
    biciCard.append(precio);*/

    let contenidoCarta = document.createElement("div");
    contenidoCarta.setAttribute("class", "tarjeta-bici");
    contenidoCarta.innerHTML = `
      <a href="#">
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

export {
  tarjetasBicis
};
