import numpy, random, os
lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)

#print(weights)

def Perceptron(i1, i2, o):
    pred = i1*weights[0] + i2*weights[1]+bias*weights[2]
    if pred > 0: pred = 1
    else: pred = 0
    error = o - pred #error is the label - our preditcion 
    weights[0] += error * i1 * lr 
    weights[1] += error * i2 * lr 
    weights[2] += error * bias * lr 

def main():
    operation = input('input logical operation (and/or)\n')
    if (operation == "and"):
        for i in range(50) :
            Perceptron(1,1,1) #True and true
            Perceptron(1,0,0) #True and false
            Perceptron(0,1,0) #False and true
            Perceptron(0,0,0) #False and false
    elif (operation == "or"):
        for i in range(50) :
            Perceptron(1,1,1) #True or true
            Perceptron(1,0,1) #True or false
            Perceptron(0,1,1) #False or true
            Perceptron(0,0,0) #False or false
    else:
        print('unidenified operation')
        exit(-1)
    #print(weights)

    x = int(input('first argument\n'))
    y = int(input('second argument\n'))
    pred = x*weights[0] + y*weights[1] + bias*weights[2]
    #activation function
    if pred > 0 : pred = 1
    else : pred = 0

    print(x, operation, y, "is : ", pred)

if __name__ == "__main__":
    main()