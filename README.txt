Le servo moteur va servir à détecter un mouvement à l'aide de ce capteur 
et du Raspberry est très simple sachant que la sortie du capteur ne peut 
avoir que les valeurs 1 & 0. 

Caractéristiques du capteur
   Alimentation : 4.5V à 20V DC
   Sortie : high 3.3V, low 0V
   Délai de sortie et sensibilité ajustable par potentiomètre
   Déclenchement avec ou sans répétition
   Portée de 7 m et angle de 120°

Connexion du capteur au Raspberry
Le capteur HC-SR501 possède 3 pins :

   Le VCC (+5V);
   Le GND, (0V);
   L'output (qui renvoie une valeure TOR)
Information
A propos du TOR
La sortie tout ou rien du capteur PIR (1 ou 0) fait que le capteur peut être directement relié à la commande d'un relai

Ordre des sortie du capteur
Selon la version du capteur, l'ordre des pins peut varier. Ils peuvent être dans des ordres différents quand on les regarde face "globe vers nous". L'ordre peut être :

    > VCC - Out - GND
     ou
    > GND - Out - VCC
Pour savoir où est le VCC & le GND, il y a deux solutions :

    1. Soulever le "globe" en plastique qui est normalement juste clipsé puis regarder ce qui est marqué aux endroits de soudure des Pins (VCC, Out, GND)
    2. Sur toutes les versions se trouve, à l'arrière du capteur, un microcontrôleur. Le côté où se trouve le microcontrôleur est le côté ou se trouve le Pin GND.