import logging
import sys


#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

       quotient = dividend/divisor  
       print (quotient)
        
    #pulled logging level error, made the exception more specific ZeroDivisionError instead of Exception  
    except ZeroDivisionError as e:
        logging.error(" The exception that occurred is: %s", e)

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)