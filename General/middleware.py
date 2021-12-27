from Usuarios.models import *
def a_quien_seguir(get_response):

    def middleware(request):
        # Código que se ejecutará antes del llamado a la vista.
        if request.user.is_authenticated:
            user_ids = Relacion.objects.filter(from_user=request.user).values_list('to_user_id', flat=True)
            request.no_seguidos = User.objects.all().exclude(id__in=user_ids).exclude(id=request.user.id).order_by('?')[:3]
            print(request.no_seguidos)
        response = get_response(request)
        # Código que se ejecutará después del llamado a la vista.
        return response

    return middleware