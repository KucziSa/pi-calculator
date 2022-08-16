import random
import math
import os

operations=0

print("""______  _   _____         _               _         _                
| ___ \(_) /  __ \       | |             | |       | |               
| |_/ / _  | /  \/  __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __ 
|  __/ | | | |     / _` || | / __|| | | || | / _` || __| / _ \ | '__|
| |    | | | \__/\| (_| || || (__ | |_| || || (_| || |_ | (_) || |   
\_|    |_|  \____/ \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|   
                                                                     
""")

while operations > 2147483647 or operations < 0 or operations == 0:

    try:
        operations = int(input('Enter number of calculations - number of operations must be below 2,147,483,647: '))
    except:
        print("Try putting numbers.")

   


inside = 0
total = 0
for x in range (operations):
    x = random.random()
    y = random.random()
    dist = math.sqrt(x*x+y*y)
    if dist < 1:
        inside+=1
    total+=1
    pi = 4.0 * inside / total
    print(pi)
        
        
print("Your calculated pi number is: " + str(pi))
print("Goodbye!")
print("©Kuczi$")
os.system("pause")