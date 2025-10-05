def validar_usuario(usuario: str):
    if len(usuario) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    elif len(usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif not usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True
