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
   let whitelist = ['http://fisi-bici.herokuapp.com/'];
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
user.deVisitanteToUser();
let usuarioEsta;


if (window.location.href == "http://fisi-bici.herokuapp.com/auth/signup") {
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

      peticion.postData('http://fisi-bici.herokuapp.com/register', formJSON)
        .then(datos => {
            peticion.postData('http://fisi-bici.herokuapp.com/login', formJSON)
              .then(() => {
                  console.log('Datos enviados!');
                });

                alert('Bienvenido a FisiBici :D\nSe te redirigirá a la tienda.');

                window.location.href = "http://fisi-bici.herokuapp.com/shop"; console.log(datos);
              });
        });
  }
  else if (window.location.href == "auth/singin") {
    /** Si el usuario está en página de INICIO DE SESIÓN */
    // debugger;
    // if(usuarioEsta == true){
    //   alert("Ya has iniciado sesión.\nSe te redirigirá a la tienda :)");
    //   window.location.pathname = './shop.html';
    // }

    console.log("Página de inicio de sesión");

    let formulario = document.querySelector("#appointment-form");

    /** Cuando el usuario haga click en el botón de iniciar sesión */
    formulario.addEventListener("submit", (event) => {
      //debugger;
      event.preventDefault();
      let datos = new FormData(formulario);

      let formJSON = {
        "email": user.renderEmail(datos),
        "password": user.renderPassword(datos)
      }

      console.log(formJSON);

      peticion.postData('http://fisi-bici.herokuapp.com/login', formJSON)
        .then(datos => {
          console.log('Datos enviados!');


          if (datos.message != "Contraseña incorrecta") {
            user.deVisitanteToUser();
            //usuarioEsta = true;
            window.location.href = "http://fisi-bici.herokuapp.com/shop";
          } else {
            alert(datos.message + "\nIntente nuevamente.");
          }

        })
        .catch(err => {
          console.log("Algo malo ocurrió:" + err);
        })
    });

  } else if (window.location.href == "http://fisi-bici.herokuapp.com/shop" ) {
    /** Si el usuario está en la página de TIENDA */
    let keys, tarjetaBici, biciCard;
    peticion.getData("http://fisi-bici.herokuapp.com/bicycles")
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

  document.querySelector('.cerrar-sesion').addEventListener("click", () => {
    //debugger;
    user.cerrarSesion()
      .then(data => {
        alert('Cerró sesión\n', data);
      })
  })



  // postData("http://localhost:5000/bicycles", {
  //     "name": "333",
  //     "price": 4000.0,
  //     "stock": 1,
  //     "colors": ["Amarillo"],
  //     "img_path": "../img/bici2.jpg"
  // })
  // .then(data => console.log(data))
