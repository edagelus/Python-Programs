# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 16:14:47 2019

@author: Sartaj 

The program  prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

"""
def fizzbuzz(r):
        for i in range(1,r):
            if (i % 3 == 0  and i % 5 == 0 ):
                print(str(i)+ "= FuZZ BuZZ " )
            else:
                if (i % 3 == 0 ):
                    print(str(i) + " = Fizz ")
                else:
                    if (i % 5 == 0 ):
                            print(str(i) + "Buzz")
                    else:
                        print(str(i))
fizzbuzz(100)