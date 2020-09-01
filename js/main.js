import * as peticion from "./requests.js";

let keys;
peticion.getData("http://localhost:5000/bicycles")
  .then(data => {
    keys = Object.values(data.bicycles);
    console.log(keys);
    //listadoBicis(data.bicycles);
  });

function listadoBicis(bicis) {
  bicis.map((bici, i) => {
    let nombre = document.createElement("p");
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
    caja.appendChild(imagen);
  })
}
