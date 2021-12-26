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
            heightAuto: false,
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
              axios.delete(`${location.origin}/post/eliminar/${e.target.dataset.postid}`)
                .then(function (response) {
                    e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.remove()
                    Swal.fire({
                        heightAuto: false,
                        title: "Post eliminado",
                        icon: "success"
                    })
                })
                .catch(function (error) {
                    Swal.fire(
                        'XD?',
                        '',
                        'error'
                      )
                })
            }
          })
    }

    //Enviar comentario
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
                    <div class="flex flex-col w-full">
                        <a href="${location.origin}/@${response.data.username}">
                            <p>${response.data.nombre}</p>
                        </a>
                        <a href="${location.origin}/@${response.data.username}">
                            <p class="text-gray-400">@${response.data.username}</p>
                        </a>
                    </div>
                    <div class="relative -top-5 w-full flex justify-end">
                        <i class="cursor-pointer text-gray-400 text-2xl fas fa-ellipsis-h" id="menuPostIcon"></i>
                        <div class="hidden transition-all duration-100 ease-linear absolute rounded top-5 w-auto border border-gray-300 bg-gray-100 hover:bg-gray-200" id="menuPost">
                            <ul>
                                <li>
                                    <p class="cursor-pointer text-red-500 text-center p-2" id="eliminarComentario" data-comentarioid="${response.data.id}"><i class="far fa-trash-alt"></i> Eliminar</p>
                                </li>
                            </ul>
                        </div>
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
            Swal.fire(
                'Ups... ha ocurrido un error',
                'Intentalo nuevamente',
                'error'
              )
          });
            }

    //Eliminar Comentario
    if(e.target.id == "eliminarComentario"){
        let comentario = e.target.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement
        Swal.fire({
            heightAuto: false,
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
                axios({
                    method: 'delete',
                    url: `${location.origin}/post/comentario/${e.target.dataset.comentarioid}/eliminar/`,
                    data: {
                    },
                    headers: {
                      "content-type": "application/x-www-form-urlencode"
                    }
                  })
                  .then(function(response) {
                        comentario.remove()
                        Swal.fire({
                            heightAuto: false,
                            title: "Comentario eliminado",
                            icon: "success"
                        })
                  })
                  .catch(function(error) {
                      
                  })
            }
          })
    }

    //Follow
    if(e.target.id == "followButton"){
        axios({
            method: 'POST',
            url: `${location.origin}/follow/${e.target.dataset.username}`
        })
        .then(function(response) {
            e.target.innerHTML = "Dejar de seguir"
            e.target.id = "unfollowButton"
            e.target.classList = "border-2 bg-teal-500 border-teal-500 text-white p-2 rounded-full hover:bg-red-500 hover:border-red-700 hover:text-white transition-all ease-linear duration-100"
        })
        .catch(function(error) {
            Swal.fire({
                heightAuto: false,
                title: "Ups... ha ocurrido un error",
                text: "Intentalo nuevamente",
                icon: "error"
            })
        })
    }

    //Unfollow
    if(e.target.id == "unfollowButton"){
        axios({
            method: 'POST',
            url: `${location.origin}/unfollow/${e.target.dataset.username}`
        })
        .then(function(response) {
            e.target.innerHTML = "Seguir"
            e.target.id = "followButton"
            e.target.classList = "border-2 border-teal-500 text-teal-500 p-2 rounded-full hover:bg-teal-500 hover:text-white transition-all ease-linear duration-100"
        })
        .catch(function(error) {
            Swal.fire({
                heightAuto: false,
                title: "Ups... ha ocurrido un error",
                text: "Intentalo nuevamente",
                icon: "error"
            })
        })
    }

    //Like
    if(e.target.id == "likeButton"){
        let post = e.target.parentElement.parentElement.parentElement
        let boton = e.target.parentElement
        post_id = post.querySelector('#post_id').value
        axios({
            method: 'POST',
            url: `${location.origin}/post/${post_id}/like/`
        })
        .then(function(response) {
            let corazon = boton.querySelector('i')
            corazon.classList.remove('far')
            corazon.classList.add('fas')
            boton.classList.remove('text-gray-400')
            boton.classList.add('text-red-600')
            let numero = parseInt(boton.querySelector('span').innerHTML)
            boton.querySelector('span').innerHTML = numero + 1
            e.target.id = "dislikeButton"
        })
        .catch(function(error) {
            Swal.fire(
                'Ups... ha ocurrido un error',
                'Intentalo nuevamente',
                'error'
              )
        })
    }

        //Dislike
        if(e.target.id == "dislikeButton"){
            let post = e.target.parentElement.parentElement.parentElement
            let boton = e.target.parentElement
            post_id = post.querySelector('#post_id').value
            axios({
                method: 'POST',
                url: `${location.origin}/post/${post_id}/dislike/`
            })
            .then(function(response) {
                let corazon = boton.querySelector('i')
                corazon.classList.add('far')
                corazon.classList.remove('fas')
                boton.classList.add('text-gray-400')
                boton.classList.remove('text-red-600')
                boton.classList.add('hover:text-red-600')
                let numero = parseInt(boton.querySelector('span').innerHTML)
                boton.querySelector('span').innerHTML = numero - 1
                e.target.id = "likeButton"
            })
            .catch(function(error) {
                Swal.fire(
                    'Ups... ha ocurrido un error',
                    'Intentalo nuevamente',
                    'error'
                  )
            })
        }

        if(e.target.id == "commentButton"){
            let post = e.target.parentElement.parentElement.parentElement
            let textarea = post.querySelector('textarea')
            textarea.focus()
        }
})

botonMenu = document.querySelector('#botonHiddenMenu')
botonMenu.addEventListener('click', function(e) {
    hiddenMenu = document.querySelector('#hiddenMenu')
    hiddenMenu.classList.toggle('hidden')
})

document.addEventListener('DOMContentLoaded', () =>{

    if(location.pathname == '/notificaciones/'){
        axios({
            method: 'POST',
            url: `${location.origin}/notificaciones/leer/`
        })
        .then( (response) => {
        })
        .catch( (error) => {
        })
    }

})