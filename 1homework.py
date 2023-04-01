stime = int(input("Input time in seconds >>>"))

H = stime // 3600
M = (stime % 3600) // 60
S = (stime % 3600) % 60
print(f"This time in format hh:mm:ss = {H}:{M}:{S}")
