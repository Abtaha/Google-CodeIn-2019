import sys
sys.setrecursionlimit(10**20)

                      
def subtractor(p, d):
    if p > 0:
        if d % 2 != 0:
            p = p - (d + 1)
        else:
            p = p - d
    else:
        return d
    
    d = d + 1
    return subtractor(p, d)

def algo(p):
    d = subtractor(p, 1)
    #d = 0
    d -= 1

    if d % 2 == 0:
        return "Captain America"
    else:
        return "Iron Man"


p = int(input("Enter Thanos's Power >> "))
print(algo(p))

