from cryptographyFramework import *

initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "sua mensagem secreta!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "sua segunda mensagem secreta!")
saveNewLine(encryptedText)

