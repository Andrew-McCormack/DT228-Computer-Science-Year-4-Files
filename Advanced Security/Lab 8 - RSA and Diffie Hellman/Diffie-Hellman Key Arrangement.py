def compute(pModulus, base, secretInteger):
    return base**secretInteger % pModulus

def calculateSharedSecret(B, secretIneger, pModulus):
    return B**secretInteger % pModulus


print('Enter prime modulus: ')
pModulus = int(input())
print('Enter base: ')
base = int(input())

print('What is your secret integer? ')
secretInteger = int(input())

A = (compute(pModulus, base, secretInteger))
print('A is: ' + str(A))

print('Do you have a value for B? (Answer Y or N')
selection = raw_input()

if(selection.lower() == 'y'):
    print('What is the value of B?')
    B = int(input())

    print('Shared secret is: ' + str(calculateSharedSecret(B, secretInteger, pModulus)))