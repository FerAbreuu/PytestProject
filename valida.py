def senha(senha):
    if len(senha) < 10 or len(senha) > 30:
        return False
    if " " in senha or senha.islower() or senha.isspace() or senha.isalpha() or senha.isdecimal() or senha.isalnum():
        return False
    if any(char.isdigit() for char in senha):
        return "Correto!"
    return False

def usuario(usuario):
    if len(usuario) > 30 or len(usuario) < 4 or usuario.isspace() or not usuario[0].isupper() or not usuario.isalnum():
        return False
    return "Correto!"

def limite(mensagem):
    return len(mensagem) <= 70

