import pyautogui as ag
from time import sleep



essai = ag.prompt('Etes vous prets ?', 'TEST')

print(essai)

if essai == 'oui' :
 distance = 200
 while distance > 0:
        ag.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        ag.drag(0, distance, duration=0.5)   # move down
        ag.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        ag.drag(0, -distance, duration=0.5)  # move up
else : print('fin du programme')