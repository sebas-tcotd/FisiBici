async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response.json();
}

async function getData(url = '') {
  const response = await fetch(url, {
    method: 'GET',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
  });
  return response.json();
}

async function putData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'PUT',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json; charset=UTF-8'
    },
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data)
  });
  return response.json();
}

async function deleteData(url = '') {
  const response = await fetch(url, {
    method: 'DELETE',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
  });
  return response.json();
}

let keys, bicis;
const dataCargada = getData("http://localhost:5000/bicycles")
.then(data => {
    keys = Object.values(data.bicycles);
    console.log(keys);
    listadoBicis(data.bicycles);
});

function listadoBicis(bicis){
    bicis.map((bici, i) => {
        let nombre = document.createElement("p");
        nombre.innerHTML = `Nombre de bicicleta ${i + 1}: ${bici.name}`;
        let precio = document.createElement("p");
        precio.innerHTML = `Precio de la bicicleta: ${bici.price}`;
        let caja = document.querySelector("p.texto-header");
        caja.append(nombre);
        caja.append(precio);
    })
}

