def unlock():
    final_pin = "00"

    one = 0
    two = 10
    three = 100

    first_print = False
    second_print = False
    
    pin_found = False

    while True:
        final_pin = "00{}".format(one)
        
        if(final_pin != pin and pin_found == False and first_print == False):
            print("Trying PIN: {}".format(final_pin))
            one = one + 1

            if(one > 9):
                break

        else:
            first_print = True

            if(first_print == True): 
                pin_found = True
                print()
                print("PIN FOUND: {}".format(final_pin))
                print()
                break
            
            else:
                break
        

    one = 0

    while True:
        final_pin = "0{}".format(two)

        if(final_pin != pin and pin_found == False):
            print("Trying PIN: {}".format(final_pin))
            two = two + 1

            if(two > 99):
                break

        else:
            second_print = True
            
            if(first_print == False): 
                pin_found = True
                print()
                print("PIN FOUND: {}".format(final_pin))
                print()
                break
            
            else:
                break
            
    two = 0


    while True:
        final_pin = "{}".format(three)

        if(final_pin != pin and pin_found == False):
            print("Trying PIN: {}".format(final_pin))
            three = three + 1

            if(three > 999):
                break

        else:

            if(first_print == False and second_print == False): 
                pin_found = True
                print()
                print("PIN FOUND: {}".format(final_pin))
                print()
                break
            
            else:
                break

            
try:
    pin = str(input("PIN: "))
    print()
    pin = pin.replace(" ","")
    
    if len(pin) == 3:
        unlock()
        
    else:
        print("La LUNGHEZZA del PIN deve essere di 3 NUMERI!")
        
except ValueError:
    print()
    print("INSERISCI SOLO NUMERI!")
