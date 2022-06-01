from pyzbar.pyzbar import decode #importing module for decoding QR Code and 1D array code
from PIL import Image #importing Image from Pillow module

print('Welcome to QR reader, have a great time') #welcome message

qrcode=input("Input the name of QR code file to be scanned: ") #taking the input QR Code from user

img=Image.open(qrcode) #using Open method of Image module, store the image you wish to get secret code of

secretcode=decode(img) #calling decode method for our QR code or img.
# print('The secret code is:', secretcode) -- #This returns an output with data,type,scale,shape,quality, etc.
#so to access/print only the data(i.e. secret code), we will use secretcode[0].data.decode()
print() #Changing the line to print the secret code

print('The secret code is:', secretcode[0].data.decode()) #printing the secret code of QR code