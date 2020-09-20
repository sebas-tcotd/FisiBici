import * as peticion from "./requests.js";
import * as bici from "./bici.js";
import * as user from './user.js';

function setCors() {
   let whitelist = ['http://fisi-bici.herokuapp.com'];
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

let ruta = document.getElementById('ruta');


if (window.location.href == `${ruta.getAttribute('href')}auth/sign-up`) {
  console.log("Pagina de registro")
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

      peticion.postData(`${ruta.getAttribute('href')}register`, formJSON)
        .then(datos => {
            peticion.postData(`${ruta.getAttribute('href')}login`, formJSON)
              .then(() => {
                  console.log('Datos enviados!');
                });

                alert('Bienvenido a FisiBici :D\nSe te redirigirá a la tienda.');

                window.location.href = `${ruta.getAttribute('href')}shop`; console.log(datos);
              });
        });
  }
  else if (window.location.href == `${ruta.getAttribute('href')}auth/sign-in`) {
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

      peticion.postData(`${ruta.getAttribute('href')}login`, formJSON)
        .then(datos => {
          console.log('Datos enviados!');


          if (datos.message != "Contraseña incorrecta") {
            user.deVisitanteToUser();
            //usuarioEsta = true;
            window.location.href = `${ruta.getAttribute('href')}shop`;
          } else {
            alert(datos.message + "\nIntente nuevamente.");
          }

        })
        .catch(err => {
          console.log("Algo malo ocurrió:" + err);
        })
    });

  } else if (window.location.href == `${ruta.getAttribute('href')}shop` ) {
    /** Si el usuario está en la página de TIENDA */
    let keys, tarjetaBici, biciCard;
    peticion.getData(`${ruta.getAttribute('href')}bicycles`)
      .then(data => {
        keys = Object.values(data.bicycles);
        console.log(keys);
        bici.tarjetasBicis(data.bicycles);

        tarjetaBici = document.querySelector("#modal");
        console.log(tarjetaBici);

        bici.popupBici(tarjetaBici);
      });



    let fondoModal = document.querySelector(".popup-img");
    fondoModal.style.backgroundImage = "{{ url_for('static', filename='img/bici2.jpg') }}";
  }

  document.querySelector('.cerrar-sesion').addEventListener("click", () => {
    //debugger;
    user.cerrarSesion()
      .then(data => {
        alert('Cerró sesión\n', data);
      })
  })
