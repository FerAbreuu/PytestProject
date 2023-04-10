def senha(senha):
    if " " in senha:
        return("f")
    elif senha.islower():
        return("f")
    else:
        if senha.isspace():
            return("f")
        else:
            if senha.isalpha():
                return("f")
            elif senha.isdecimal():
                return("f")
            elif senha.isalnum():
                return("f")
            else:
                if len(senha) < 10 or len(senha)> 30:
                    return("f")
                else:
                    string=list(senha)
                    if any(char.isdigit() for char in string):
                        return("c")
                    else:
                        return("f")
def usuario(usuario):
    if len(usuario) > 30 or len(usuario)< 4:
        return("f")
    else:
        if usuario.isspace():
            return("f")
        else:
            if usuario[0].isupper():
                if usuario.isalnum():
                    return("c")
                else:
                    return("f")
            else:
                return("f")
def limite(mensagem):
    if len(mensagem)> 70:
        return("f")
    else:
        return("c")
