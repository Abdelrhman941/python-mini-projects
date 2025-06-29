########################## The Least Common Multiple ##########################
# LCM(𝑎, 𝑏) =|𝑎 ⋅ 𝑏| / GCD(𝑎, 𝑏)
# Note: GCD stands for Greatest Common Divisor.

def compute_lcm(x, y):
    if x > y: # choose the greater number
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is", compute_lcm(num1, num2))
