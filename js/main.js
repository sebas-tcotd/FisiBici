import * as peticion from "./requests.js";
import * as bici from "./bici.js";
import * as user from './user.js';

// let keys;
// peticion.getData("http://localhost:5000/bicycles")
//   .then(data => {
//     keys = Object.values(data.bicycles);
//     console.log(keys);
//     //listadoBicis(data.bicycles);
//   });

function setCors() {
  let whitelist = ['http://127.0.0.1:5500', 'http://127.0.0.1:5000'];
  let corsOptions = {
    origin: (origin, callback) => {
      if (whitelist.indexOf(origin) !== -1) {
        callback(null, true)
      } else {
        callback(new Error('Not allowed by CORS'))
      }
    },
    credentials: true
  }
}

setCors();


if (window.location.pathname == "/singup.html") {
  /** Si el usuario está en la página de REGISTRO */
  let formulario = document.querySelector("#appointment-form");
  formulario.addEventListener("submit", event => {

    event.preventDefault();

    let datos = new FormData(formulario);

    user.renderFirstName(datos);

    let formJSON = {
      "name": user.renderFirstName(datos),
      "last_name": user.renderLastName(datos),
      "telephone": user.renderTelephone(datos),
      "email": user.renderEmail(datos),
      "password": user.renderPassword(datos),
      "birthdate": user.renderBirthday(datos),
      "residence": user.renderResidence(datos),
      "district": user.renderDistrict(datos),
      "postal_code": user.renderPostalCode(datos)
    }

    console.log(formJSON);

    peticion.postData('http://127.0.0.1:5000/register', formJSON)
      .then(datos => {
        //window.location.href = "./shop.html";
        console.log(datos);
      });
  });
} else if (window.location.pathname == "/singin.html") {
  /** Si el usuario está en página de INICIO DE SESIÓN */

  console.log("Página de inicio de sesión");

  let formulario = document.querySelector("#appointment-form");
  
  /** Cuando el usuario haga click en el botón de iniciar sesión */
  formulario.addEventListener("submit", event => {
    event.preventDefault();
    //debugger;
    let datos = new FormData(formulario);

    let formJSON = {
      "email": user.renderEmail(datos),
      "password": user.renderPassword(datos)
    }

    console.log(formJSON);

    peticion.postData('http://127.0.0.1:5000/login', formJSON)
      .then(datos => {
        console.log('Datos enviados!');

        console.log(datos);

        user.deVisitanteToUser();
      })
      .catch(err => {
        console.log("Algo malo ocurrió:" + err);
      })
  });

} else if (window.location.pathname == "/shop.html") {
  /** Si el usuario está en la página de TIENDA */
  let keys, tarjetaBici, biciCard;
  peticion.getData("http://127.0.0.1:5000/bicycles")
    .then(data => {
      keys = Object.values(data.bicycles);
      console.log(keys);
      bici.tarjetasBicis(data.bicycles);

      tarjetaBici = document.querySelector("#modal");
      console.log(tarjetaBici);

      bici.popupBici(tarjetaBici);
    });

  

  let fondoModal = document.querySelector(".popup-img");
  fondoModal.style.backgroundImage = "url(../img/bici4.jpg)";
}




// postData("http://localhost:5000/bicycles", {
//     "name": "333",
//     "price": 4000.0,
//     "stock": 1,
//     "colors": ["Amarillo"],
//     "img_path": "../img/bici2.jpg"
// })
// .then(data => console.log(data))
