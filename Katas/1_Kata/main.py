  
import sms

mensaje = input('escribe tu mensaje: ')

salida = sms.traduce(mensaje)

print('{} es -{}-'.format(mensaje, salida))