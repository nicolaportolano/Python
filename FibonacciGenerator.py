# Generates a Fibonacci's sequence as long as defined by user input.
while True:
        try:
                number = int(input('How many Numbers of the Fibonacci list do you want me to generate? '))
        except ValueError:
                print ('Please enter numbers only. ')
        else:
                break
                


if number == 1:
        fibonacci = [1]

elif number == 2:
        fibonacci = [1,1]

else:
        fibonacci = [1,1]
        while len(fibonacci)<number:
                fibonacci.append(fibonacci[-1]+fibonacci[-2])
        
print (fibonacci)
        
