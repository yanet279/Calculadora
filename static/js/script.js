// Obtener la entrada y el botón de la calculadora
let entrada = document.getElementById('entrada');
let botones = document.querySelectorAll('.boton');

// Función para manejar los clics en los botones
botones.forEach(function(boton) {
    boton.addEventListener('click', function() {
        let valor = boton.innerText;
        
        if (valor === '=') {
            // Enviar la operación al servidor para obtener el resultado
            fetch('/calcular', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operacion: entrada.value
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.resultado !== undefined) {
                    entrada.value = data.resultado;
                } else {
                    entrada.value = data.error;
                }
            })
            .catch(error => {
                entrada.value = "Error de conexión";
            });
        } else if (valor === 'C') {
            // Limpiar la entrada
            entrada.value = '';
        } else if (valor === '←') {
            // Eliminar el último carácter
            entrada.value = entrada.value.slice(0, -1);
        } else {
            // Agregar el valor del botón a la entrada
            entrada.value += valor;
        }
    });
});

document.addEventListener('keydown', function (event) {
    // Identificar las teclas presionadas y hacer clic en el botón correspondiente
    if (event.key === '1') {
        document.getElementById('btn-1').click();
    } else if (event.key === '2') {
        document.getElementById('btn-2').click();
    } else if (event.key === '3') {
        document.getElementById('btn-3').click();
    } else if (event.key === '4') {
        document.getElementById('btn-4').click();
    } else if (event.key === '5') {
        document.getElementById('btn-5').click();
    } else if (event.key === '6') {
        document.getElementById('btn-6').click();
    } else if (event.key === '7') {
        document.getElementById('btn-7').click();
    } else if (event.key === '8') {
        document.getElementById('btn-8').click();
    } else if (event.key === '9') {
        document.getElementById('btn-9').click();
    } else if (event.key === '0') {
        document.getElementById('btn-0').click();
    } else if (event.key === '/') {
        document.getElementById('btn-div').click();
    } else if (event.key === '*') {
        document.getElementById('btn-mult').click();
    } else if (event.key === '+') {
        document.getElementById('btn-add').click();
    } else if (event.key === '-') {
        document.getElementById('btn-sub').click();
    } else if (event.key === 'Enter') {
        document.getElementById('btn-equal').click();
    } else if (event.key === 'c' || event.key === 'C') {
        document.getElementById('btn-clear').click();
    } else if (event.key === 'Backspace') {
        document.getElementById('btn-borrar').click();
    } else if (event.key === '.' || event.key === 'C') {
        document.getElementById('btn-punto').click();
    }
});


fetch("https://mi-backend.onrender.com/calcular", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ a: 5, b: 3 })
})
    .then(res => res.json())
    .then(data => {
        console.log("Resultado:", data.resultado);
});