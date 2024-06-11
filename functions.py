# Do functions need to be linear?

def add2(num1, num2):
    return add(num1, num2)

def add(num1, num2):
    return num1 + num2

def main():
    print(add2(1,2))

if __name__ == '__main__':
    main()