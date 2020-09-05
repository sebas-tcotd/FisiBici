import {
  getData,
  deleteData
} from './requests.js';

/** Funciones de registro de usuario */
function renderFirstName(formData) {
  const $firstName = document.querySelector("#first-name");
  const firstName = formData.get('first-name');
  $firstName.textContent = firstName;
  return firstName;
}

function renderLastName(formData) {
  const $lastName = document.querySelector("#last-name");
  const lastName = formData.get('last-name');
  $lastName.textContent = lastName;
  return $lastName.textContent;
}

function renderTelephone(formData) {
  const $telephone = document.querySelector("#phone_number");
  const telephone = formData.get('phone_number');
  $telephone.textContent = telephone;
  return telephone;
}

function renderEmail(formData) {
  const $email = document.querySelector('#email');
  const email = formData.get('email');
  $email.textContent = email;
  return $email.textContent;
}

function renderPassword(formData) {
  const $password = document.querySelector('#password');
  const password = formData.get('password');
  $password.textContent = password;
  return $password.textContent;
}

function renderBirthday(formData) {
  let $birthday = document.querySelector('#birthday');
  let day, month, year, tempBirthday;
  let birthdate = formData.get('birthday');

  $birthday.textContent = birthdate;
  tempBirthday = $birthday.textContent;

  year = parseInt(tempBirthday.slice(0, 4));
  month = parseInt(tempBirthday.slice(5, 7));
  day = parseInt(tempBirthday.slice(8));

  return {
    "day": day,
    "month": month,
    "year": year
  }
}

function renderResidence(formData) {
  let $address = document.querySelector('#address');
  let address = formData.get('address');

  $address.textContent = address;
  return $address.textContent;
}

function renderDistrict(formData) {
  let $district = document.querySelector('#district');
  let district = formData.get('district');

  $district.textContent = district;
  return $district.textContent;
}

function renderPostalCode(formData) {
  let $postalCode = document.querySelector('#zip');
  let postalCode = formData.get('zip');

  $postalCode.textContent = postalCode;
  return $postalCode.textContent;
}

/** Funciones de inicio de sesión */

function letsGo() {
  if (document.form.password.value == 'CONTRASEÑA' && document.form.login.value == 'USUARIO') {
    document.form.submit();
  } else {
    alert("Porfavor ingrese, nombre de usuario y contraseña correctos.");
  }
}

/** Para cambiar el nombre de VISITANTE a ${NOMBRE-USUARIO} */
export function deVisitanteToUser() {
  //debugger;
  let nombreUser;
  getData('http://127.0.0.1:5000/user')
    .then(data => {

      if(data.message != "Ningun usuario ha iniciado sesion"){
        nombreUser = data.user.name;
  
        /**Para el bottom bar */
        let nombre = document.querySelector('#bottom-nombre-user'); //Selecciona el ID del bottom bar donde dice 'visitante'
        nombre.textContent = nombreUser;
  
        /** Para el top bar */
        let topNombre = document.querySelector("#top-nombre-user");
        let nombreSpan = document.createElement("span");
        nombreSpan.setAttribute("class", "nombreSpan");
        nombreSpan.innerHTML = nombreUser;
        topNombre.append(nombreSpan);
        return true;
      }else {
        console.log(data.message);
        return false;
      }
    })
    .catch(err => console.log("Ups, algo ocurrió mal.\nRazón: " + err));
}

export function cerrarSesion(){
  deleteData('http://127.0.0.1:5000/user')
  .then(() => {
    window.location.reload();
    window.location.pathname = './';
  })
}

export {
  renderFirstName,
  renderLastName,
  renderTelephone,
  renderEmail,
  renderPassword,
  renderBirthday,
  renderResidence,
  renderDistrict,
  renderPostalCode,
  letsGo
};
