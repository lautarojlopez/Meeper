document.addEventListener('keyup', function(e) {
    if(e.target.id == "mensaje"){

        //Agrandar textarea a medida que se escribe
        e.target.style.height = 'auto';
        let scrollH = e.target.scrollHeight;
        e.target.style.height = `${scrollH}px`

        let contador = e.target.parentElement.querySelector('#contador')
        contador.innerHTML = e.target.value.length

        if(e.target.value.length > 0 && e.target.value.length <= 280){
            let enviar = e.target.parentElement.querySelector('#botonEnviar')
            enviar.classList.remove('desactivado')
            enviar.classList.add('activo')
            enviar.classList.remove('bg-gray-300')
            enviar.classList.add('bg-teal-500')
            enviar.classList.remove('cursor-auto')
            enviar.classList.add('cursor-pointer')

            e.target.classList.remove('border-red-500')
            e.target.classList.remove('bg-red-50')

            //Contador gris
            let texto_contador = e.target.parentElement.querySelector('.texto-contador')
            texto_contador.classList.remove('text-red-500')
            texto_contador.classList.add('text-gray-400')
        }
        
        if(e.target.value.length == 0){
            let enviar = e.target.parentElement.querySelector('#botonEnviar')
            enviar.classList.add('desactivado')
            enviar.classList.remove('activo')
            enviar.classList.remove('bg-teal-500')
            enviar.classList.add('bg-gray-300')
            enviar.classList.remove('cursor-pointer')
            enviar.classList.add('cursor-auto')
        }

        if(e.target.value.length > 280){
            e.target.classList.remove('border-gray-200')
            e.target.classList.add('border-red-500')
            e.target.classList.add('bg-red-50')
            //Contador rojo
            let texto_contador = e.target.parentElement.querySelector('.texto-contador')
            texto_contador.classList.remove('text-gray-400')
            texto_contador.classList.add('text-red-500')
            //Desactiva el boton
            let enviar = e.target.parentElement.querySelector('#botonEnviar')
            enviar.classList.add('desactivado')
            enviar.classList.remove('activo')
            enviar.classList.remove('bg-teal-500')
            enviar.classList.add('bg-gray-300')
            enviar.classList.remove('cursor-pointer')
            enviar.classList.add('cursor-auto')
        }
    }
})

document.addEventListener('click', function(e) {

    if(e.target.classList.contains('desactivado')){
        e.preventDefault()
    }

    //Mostrar Menu Post
    if(e.target.id == "menuPostIcon"){
        let menu = e.target.parentElement.querySelector('#menuPost')
        menu.classList.toggle('hidden')
    }

    //Eliminar Post
    if(e.target.id == "eliminarPost"){
        Swal.fire({
            title: '¿Estás seguro?',
            text: "Esta acción no se podrá revertir.",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#0d9488',
            cancelButtonColor: '#ef4444',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
          }).then((result) => {
            if (result.isConfirmed) {
                console.log(`${location.origin}/post/eliminar/${e.target.dataset.postid}`);
              axios.get(`${location.origin}/post/eliminar/${e.target.dataset.postid}`)
                .then(function (response) {
                    e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.remove()
                    console.log(response);
                    Swal.fire(
                        'Eliminado',
                        '',
                        'success'
                      )
                })
                .catch(function (error) {
                    console.log(error);
                    Swal.fire(
                        'XD?',
                        '',
                        'error'
                      )
                })
            }
          })
    }
})

botonMenu = document.querySelector('#botonHiddenMenu')
botonMenu.addEventListener('click', function(e) {
    hiddenMenu = document.querySelector('#hiddenMenu')
    hiddenMenu.classList.toggle('hidden')
})