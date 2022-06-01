def fizzbuzz():
    for i in range(101):
        
        if (i%5 ==0 && i%3 ==0):
            print("FizzBuzz")
        else if (i%3 ==0):
            print("Fizz")
        else:
            print(i)
