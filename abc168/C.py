import math

A, B, H, M = [int(i) for i in input().split()]


difference = H + M/60 - M/5

angle = difference  * 30


c = math.sqrt((A ** 2 + B ** 2) - (2 * A * B * math.cos(angle*math.pi/180)))

print(c)
