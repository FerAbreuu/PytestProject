from valida import *
from cryptographyFramework import *
user=""
sen=""
valid1=""
valid2=""
valid3=""
while True:
    user=input("Digite um usuário")
    sen=input("Digite uma senha")
    valid1=usuario(user)
    valid2=senha(sen)
    if valid1 != "Correto!":
        print("o usuário deve ter entre 4 e 30 caracteres e ter o primeiro me maiusculo")
    else:
        if valid2 != "Correto!":
            print("a senha deve ter entre 10 e 30 caracteres e ter 1 letra maiuscula, 1 minuscula, 1 numero e 1 simbolo") 
        else:
            break
while True:
    mensagem=input("digite a mensagem para encripitar com no maximo 70 caracteres")
    valid3=limite(mensagem)
    if valid1 != "Correto!":
        print("a mensagem deve ter no maximo 70 caracteres")
    else:
        break
encryptedText = encryptMessage(user, sen, mensagem)
saveNewLine(encryptedText)
