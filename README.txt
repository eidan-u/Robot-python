Le servo moteur va servir � d�tecter un mouvement � l'aide de ce capteur 
et du Raspberry est tr�s simple sachant que la sortie du capteur ne peut 
avoir que les valeurs 1 & 0. 

Caract�ristiques du capteur
   Alimentation : 4.5V � 20V DC
   Sortie : high 3.3V, low 0V
   D�lai de sortie et sensibilit� ajustable par potentiom�tre
   D�clenchement avec ou sans r�p�tition
   Port�e de 7 m et angle de 120�

Connexion du capteur au Raspberry
Le capteur HC-SR501 poss�de 3 pins :

   Le VCC (+5V);
   Le GND, (0V);
   L'output (qui renvoie une valeure TOR)
Information
A propos du TOR
La sortie tout ou rien du capteur PIR (1 ou 0) fait que le capteur peut �tre directement reli� � la commande d'un relai

Ordre des sortie du capteur
Selon la version du capteur, l'ordre des pins peut varier. Ils peuvent �tre dans des ordres diff�rents quand on les regarde face "globe vers nous". L'ordre peut �tre :

    > VCC - Out - GND
     ou
    > GND - Out - VCC
Pour savoir o� est le VCC & le GND, il y a deux solutions :

    1. Soulever le "globe" en plastique qui est normalement juste clips� puis regarder ce qui est marqu� aux endroits de soudure des Pins (VCC, Out, GND)
    2. Sur toutes les versions se trouve, � l'arri�re du capteur, un microcontr�leur. Le c�t� o� se trouve le microcontr�leur est le c�t� ou se trouve le Pin GND.