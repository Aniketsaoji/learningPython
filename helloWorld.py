class MyDog:
  def __init__(self, name):
    self.name = name

  def show_name(self):
    print("My dog's name is ", self.name)

class testClass:
  def calculate_multiply(number1, number2):
    return number1*number2;

def main():
  print("hello World")
  x = MyDog("Prepper")
  x.show_name()
  y = testClass
  print(testClass.calculate_multiply(5, 10))
  name = input("What is your name")
  print("Very nice to meet you" + name)

if __name__ == '__main__':
    main()


