import * as peticion from "./requests.js";
import * as bici from "./bici.js";

let keys;
peticion.getData("http://localhost:5000/bicycles")
  .then(data => {
    keys = Object.values(data.bicycles);
    console.log(keys);
    bici.tarjetasBicis(data.bicycles);
  });