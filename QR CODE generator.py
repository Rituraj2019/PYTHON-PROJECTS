import pyqrcode  #import QR code generator module

print("Welcome to the QR Code generator, have a good time") #welcome message
content=input("Enter the content for QR Code:  ")#Taking user input for the secret message

secretcode=pyqrcode.create(content) #storing the created QR code in a variable
import png  #importing png from pypng module for genertaing pnq file of QR code
secretcode.png("QRCODE.png", scale = 5)  #.png file generated, take different input for the png file like scale
print('QR Code generated successfully :)') #mission successful


