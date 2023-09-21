# Triangle number 
# Create a function that will display a pattern number using the sequence numbers(n) of the parameter 
def triangle_number(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

n = 10 
triangle_number(n)            
