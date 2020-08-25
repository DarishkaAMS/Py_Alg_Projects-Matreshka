counter = 0
def matreshka(n):
    print("I'm Matreshka" + str(n), "I was born")

    if n == 1:
        print("Matreshka")
    else:
        print("Upper Part = ", n)
        matreshka(n-1)
        print("Lower Part = ", n)
    print("I'm Matreshka" + str(n), "I died")

matreshka(5)
