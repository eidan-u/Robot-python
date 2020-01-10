import RPi.GPIO as GPIO #on importe le module GPIO pour controler les ports
import time #on importe le module time ce qui permettra d'utiliser des fonctions comme time.sleep()

GPIO.setmode(GPIO.BCM)#on explique sur quelle numérotation de port on se trouve(BOARD ou BCM ) ici en BCM chaque ports possedent un numero unique (non ordonné ni croissant)

#IMPORTANT ici on se trouve dans le cas ou l'on possede 1 capteur donc une entrée un moteur connecté à une carte de controle de sens à 2 sorties (voir explications ci dessous).

GPIO.setup(7, GPIO.IN) #on initialise le port utilisé dans ce cas si c'est le 7 pour le capteur. Il y est rentré la valeur "in" car le capteur envoie vers le microprocesseur c'est une entrée.
GPIO.setup(17, GPIO.OUT)#ici on fait pareil, ce port servira au moteur pour un sens et il est "out" car les info viennent du microprocesseur vers le moteur
GPIO.setup(18, GPIO.OUT)# pareil mais pour l'autre sens
GPIO.setwarnings(False) #supprime les messages d'erreures
print ("Demarrage du capteur")
time.sleep(2) #la fonction sleep() permet de créer un "delay" avant la suite du code soit 2 secondes ici
print ("Capteur pret a detecte un mouvement")
while True:
   if GPIO.input(7): #ici si le apteur capte du mouvement ca lance le code
      print("arret des roues")
      GPIO.output(17, False) #on arrete les roues
      GPIO.output(18, False)#on arrete les roues
      time.sleep(2)
   else:
    print('héééééé zé party')
    while True:
        try:#ici on a une boucle infinie si le capteur ne capte pas de mouvement du coup le moteur tournera en continue dans les 2 sens
            print("dans un sens")
            GPIO.output(17, True)#permet de faire tourner dans un sens
            GPIO.output(18, False)
            time.sleep(2)
            print("dans l'autre sens")
            GPIO.output(17, False)#permet de faire tourner dans l'autre sens
            GPIO.output(18, True)
            time.sleep(2)
            
        except(KeyboardInterrupt): #ici cette commande permet de faire une exception au programme seulement si "controle-c" est pressé
            Print('on arrete tout')
            GPIO.output(17, False)
            GPIO.output(18, False)
            break #Stop la boucle infinie
            GPIO.cleanup() #permet de re-initialiser les ports










