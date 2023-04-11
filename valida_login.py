def valida_usuario(usuario):
    # Verifica se o usuário começa com letra maiúscula, sem caracteres especiais e sem espaços e tem no máximo 30 caracteres
    if not re.match('^[A-Z][a-z]{0,29}$', usuario):
        return "O nome de usuário deve começar com uma letra maiúscula, não pode ter caracteres especiais ou espaços e deve ter no máximo 30 caracteres."
    return "Usuário válido."

def valida_senha(senha):
    # Verifica se a senha tem pelo menos 10 caracteres, um caracter especial, um número, uma letra maiúscula e uma letra minúscula
    if not re.match('^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$', senha):
        return "A senha deve ter pelo menos 10 caracteres, um caracter especial, um número, uma letra maiúscula e uma letra minúscula."
    return "Senha válida."
