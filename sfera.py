import math
def VolumeSfera (r):
     return 4./3. * math.pi * r**3

r=input ("inserisci il raggio")
r=int(r)
risultato=VolumeSfera(r)

print (risultato)
