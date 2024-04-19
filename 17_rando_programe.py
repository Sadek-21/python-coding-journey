import math
import random
import statistics
import time
from datetime import date
import webbrowser

from forex_python.bitcoin import BtcConverter

bitcoin = BtcConverter()
print(bitcoin.get_latest_price('EUR'))
print(bitcoin.get_latest_price('USD'))
print(bitcoin.conver_btc_to_cur(6,'EUR'), 'Euro')


def fact(A):
    
    print(math.factorial(A))
    
def RandomNum():
    
    N = random.randrange(0, 102, 2)
    print(N)

def Statistic ():
    
    print(statistics.mode([10,12,14,5,9,5,7,12,14,2,13,131,31,15]))
    print(statistics.stdev([10,12,14,5,9,5,7,12,14,2,13,131,31,15]))
    

def Day():
    
    print(date.today())
    
    
def OpenWeb():
    
    webbrowser.open('https://translate.google.com/')
    webbrowser.open('https://google.com/')
    

A = int(input("Pleas entry number to calcule the factorial N! :"))
fact(A)
RandomNum()
Statistic ()
Day()
OpenWeb()
    
    
