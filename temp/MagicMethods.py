## container = class

from abc import abstractmethod


class Counter:
    def __init__(self, iCount):
        self.counter = iCount
    
    def display(self):
        print(self.counter)
    
    @classmethod
    def myStaticMethod(cls, myValue):
        cls.myValue = myValue
    
    @classmethod
    def dispalyStaticMethod(cls):
       print(cls.myValue)

    def __eq__(self, another_Counter):
        return self.counter == another_Counter.counter
    
    def __gt__(self, another_Counter):
        return self.counter > another_Counter.counter
    
    def __add__(self, adder):
      self.counter += adder.counter 

Counter.myStaticMethod("class method")
counter_1 = Counter(45)
# counter_1.myStaticMethod("counter 1")
counter_2 = Counter(50)
counter_1.display()
counter_1.dispalyStaticMethod()
counter_1.dispalyStaticMethod()
Counter.dispalyStaticMethod()
print( counter_1 == counter_2)
print( counter_1 > counter_2)

counter_2 + Counter(5)
counter_2.display()

class MyList:
    def __init__(self, list = []):
        self.myList = list
    
    def __add__(self, adder):
      self.myList.append(**adder.myList)

    def __len__(self):
       return len(self.myList)
    



my_list_1 = MyList([1,23,4,5,6,7,9])
print(len(my_list_1))


if __name__ == "__main__":
    pass


class Animal:
    @abstractmethod
    def walk(slef):
        pass

    def eat(slef):
        pass

class Dog(Animal):
    def walk(slef):
        return "normal walk"

    def eat(slef):
        return "fast eat"

class Cat(Animal):
    def walk(slef):
        return "walk & jump"

    def eat(slef):
        return "slow eat"
