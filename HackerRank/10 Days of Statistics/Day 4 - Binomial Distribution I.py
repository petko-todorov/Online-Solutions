from math import comb

p = 1.09 / (1.09 + 1)
prob = sum(comb(6, k) * p ** k * (1 - p) ** (6 - k) for k in range(3, 7))
print(f"{prob:.3f}")
