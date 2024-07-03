//Obtener las referencias del DOM/HTML

const ciudadInput = document.getElementById("ciudad");

const obtenerPronosticoBtn = document.getElementById("obtenerPronostico");

const pronosticoDiv = document.getElementById("pronostico");

//Función que me permite obtener el pronóstico

obtenerPronosticoBtn.addEventListener("click", obtenerPronostico);

function obtenerPronostico(){

    const ciudad = ciudadInput.value.trim();

    if(ciudad===""){
        mostrarError("Por favor ingresa una ciudad")
        return;
    }
    //Pega tu llave API acá abajo

    const apiKey = "f4713b05361b7c34acc6c065eebda2c5";

    const url = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad}&appid=${apiKey}&units=metric&lang=es`; 

    //Realizar una solicitud HTTP utilizando la función fetch

    fetch(url)
    .then(response => response.json())
    .then(data => {

        mostrarPronostico(data);
    })
    
    .catch(error =>{
        mostrarError("Error al obtener el pronóstico");
    });

}

//Mostrar datos en el html
function mostrarPronostico(data){

const {name, main, weather}=data;
const temperatura = main.temp;
const sensacion = main.feels_like;
const humedad = main.humidity;
const descripcion = weather[0].description;

const pronosticoHTML = `

  <div class="card">
    <div class="card-body">
       <h2 class="card-title">${name}</h2>
       <p class="card-text">Temperatura: ${temperatura}</p>
       <p class="card-text">Sensación: ${sensacion}</p>
       <p class="card-text">Humedad: ${humedad}</p>
       <p class="card-text">Descripción: ${descripcion}</p>       
    </div>
  </div>

`;

   pronosticoDiv.innerHTML = pronosticoHTML;
}
   function mostrarError(mensaje){
    const errorHTML = `
      <div class="alert alert-danger" role="alert">
        ${mensaje}
      </div>
    `;
    pronosticoDiv.innerHTML = errorHTML;


   }