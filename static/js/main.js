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

    if(e.target.classList.contains('enviarComentario') && e.target.classList.contains('activo')){
        let post = e.target.parentElement.parentElement.parentElement.parentElement
        axios({
            method: 'post',
            url: `${location.origin}/post/${post.querySelector('#post_id').value}/comentar/`,
            data: {
              'content': post.querySelector('#mensaje').value
            },
            headers: {
              "X-CSRFToken": post.querySelector('input[name="csrfmiddlewaretoken"]').value, 
              "content-type": "application/x-www-form-urlencode"
            }
          }).then(function (response) {
            let div = document.createElement('div')
            let HTML = `
            <div class="border-t bg-gray-50 p-3 border-gray-200 w-full">
                <div class="flex items-center text-sm px-5">
                    <img class="relative m-3 ml-0 object-cover w-10 h-10 rounded-full" src="${response.data.img}" alt="">
                    <div class="flex flex-col">
                        <a href="{% url 'ver-perfil' comentario.autor.username %}">
                            <p>${response.data.nombre}</p>
                        </a>
                        <a href="{% url 'ver-perfil' comentario.autor.username %}">
                            <p class="text-gray-400">@${response.data.username}</p>
                        </a>
                    </div>
                </div>
                <p class="px-5 text-gray-400 text-sm">hace un segundo</p>
                <p class="px-5 text-sm">${response.data.content}</p>
            </div>
            `
            div.innerHTML = HTML
            post.querySelector('#comentarios').appendChild(div)

            //Vaciar textarea y deshabilitar boton
            post.querySelector('#mensaje').value = ''
            e.target.classList.add('desactivado')
            e.target.classList.remove('activo')
            e.target.classList.remove('bg-teal-500')
            e.target.classList.add('bg-gray-300')
            e.target.classList.remove('cursor-pointer')
            e.target.classList.add('cursor-auto')
            post.querySelector('#contador').innerHTML= 0
            
          }).catch(function (error) {
            console.log(error)
          });
            }
})

botonMenu = document.querySelector('#botonHiddenMenu')
botonMenu.addEventListener('click', function(e) {
    hiddenMenu = document.querySelector('#hiddenMenu')
    hiddenMenu.classList.toggle('hidden')
})