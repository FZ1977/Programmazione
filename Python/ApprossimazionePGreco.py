#approssimazione p-greco/4

n = 0
limit = 10

for i in range(limit):
    n += ((-1)**i)/(2*i+1)**i
    print(f"p-greco/4 = {n:.5f}")
