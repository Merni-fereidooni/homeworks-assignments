import qrcode

x = input('whatever you want: ')
path = input('enter the path where u want to save your qrcode: ')
img = qrcode.make(x)

img.save(path, format="PNG")