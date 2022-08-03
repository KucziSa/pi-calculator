import random
import math


def main():
    inside = 0
    total = 0
    for x in range (9999999):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x*x+y*y)
        if dist < 1:
            inside+=1
        total+=1
        pi = 4.0 * inside / total
        print(pi)
        
        
main()
