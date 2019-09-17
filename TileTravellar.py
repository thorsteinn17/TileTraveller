
#forritð a að vera fullt af if settningum þar sem er hægt að velja hvert skal fara næst. 
#
 
location = (1,1)

while location != (3,1):       
    if location == (1,1):
        print("You can travel: (N)orth.")
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (1,2)
        else:
            print('Not a valid direction!')

    if location == (1,2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (1,3)
        elif direction == 'e' or direction == 'E':
            location = (2,2)
        elif direction == 's' or direction == 'S':
            location =(1,1)
        else :
             print('Not a valid direction!')

    if location == (1,3):
        print("You can travel:(E)ast or (S)outh.")
        direction = input('Direction: ')
        if direction == 'e' or direction == 'E':
            location = (2,3)
        elif direction == 's' or direction == 'S':
            location =(1,2)
        else : 
            print('Not a valid direction!')

    if location == (2,1):
        print("You can travel: (N)orth.")
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (2,2)
        else :
            print('Not a valid direction!')

    if location == (2,2):
        print("You can travel: (W)est or (S)outh.")
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (1,2)
        elif direction == 's' or direction == 'S':
            location =(2,1)
        else : 
            print('Not a valid direction!')

    if location == (2,3):
        print("You can travel: (W)est or (E)ast.")
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (1,3)
        elif direction == 'e' or direction == 'E':
            location =(3,3)
        else:
            print('Not a valid direction!')

    if location == (3,2):
        print("You can travel: (N)orth or (S)outh.")
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            location = (3,3)
        elif direction == 's' or direction == 'S':
            location =(3,1)
        else:
            print('Not a valid direction!')

    if location == (3,3):
        print("You can travel: (W)est or (S)outh.")
        direction = input('Direction: ')
        if direction == 'w' or direction == 'W':
            location = (2,3)
        elif direction == 's' or direction == 'S':
            location =(3,2)
        else:
            print('Not a valid direction!')

if location == (3,1):
        print('Victory!')
        

    