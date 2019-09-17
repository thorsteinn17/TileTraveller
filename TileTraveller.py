
#forritð a að vera fullt af if settningum þar sem er hægt að velja hvert skal fara næst. 
#
 
location = (1,1)
print("You can travel: (N)orth.")

while location != (3,1):       
    if location == (1,1):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (1,2)
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print('Not a valid direction!')

    if location == (1,2):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (1,3)
            print("You can travel: (E)ast or (S)outh.")
        elif direction == 'e' or direction == 'E':
            location = (2,2)
            print("You can travel: (S)outh or (W)est.")
        elif direction == 's' or direction == 'S':
            location =(1,1)
            print("You can travel: (N)orth.")
        else :
             print('Not a valid direction!')

    if location == (1,3):
        direction = input('Direction: ')
        if direction == 'e' or direction == 'E':
            location = (2,3)
            print("You can travel: (E)ast or (W)est.")
        elif direction == 's' or direction == 'S':
            location =(1,2)
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else : 
            print('Not a valid direction!')

    if location == (2,1):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (2,2)
            print("You can travel: (S)outh or (W)est.")
        else :
            print('Not a valid direction!')

    if location == (2,2):
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (1,2)
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif direction == 's' or direction == 'S':
            location =(2,1)
            print("You can travel: (N)orth.")
        else : 
            print('Not a valid direction!')

    if location == (2,3):
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (1,3)
            print("You can travel: (E)ast or (S)outh.")
        elif direction == 'e' or direction == 'E':
            location =(3,3)
            print("You can travel: (S)outh or (W)est.")
        else:
            print('Not a valid direction!')

    if location == (3,2):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (3,3)
            print("You can travel: (S)outh or (W)est.")
        elif direction == 's' or direction == 'S':
            location =(3,1)
        else:
            print('Not a valid direction!')

    if location == (3,3):
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (2,3)
            print("You can travel: (E)ast or (W)est.")
        elif direction == 's' or direction == 'S':
            location =(3,2)
            print("You can travel: (N)orth or (S)outh.")
        else:
            print('Not a valid direction!')

if location == (3,1):
        print('Victory!')
        

    