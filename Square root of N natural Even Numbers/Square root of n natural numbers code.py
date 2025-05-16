def sqrt_of_num(i):
    for i in range(sr+1):
        if i%2 == 0:
            print(f"{i} square = {i*i}")
    return "These are Square roots of Even Numbers"
sr = int(input())
print(sqrt_of_num(sr))
