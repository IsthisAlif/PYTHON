# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> Enclosed -> Global -> Built-in

# local
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

# Enclosed
def func3():
    x = 1
    def func4():
        x = 2
        print(x)
    func4()

func3()

# Global
def func5():
    print(y)

def func6():
    print(y)

y = 5
func5()
func6()

# Built-in
from math import e

def func7():
    print(e)

func7()