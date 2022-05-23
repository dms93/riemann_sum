#!/usr/bin/env python3

MIN_LIMIT = 1
MAX_LIMIT = 3
VALUES_RANGE = MAX_LIMIT - MIN_LIMIT
ROUND_DECIMALS = 5

def curve(x):
  return (x * (((x ** 2) + 1) ** 5))


def riemann_sum(rectangles):
  inf = 0
  sup = 0

  try:
    dx = VALUES_RANGE / rectangles
    if rectangles == 1: raise ZeroDivisionError
  except ZeroDivisionError:
    print("Invalid number of rectangles")
    return

  x = MIN_LIMIT
  left = 0
  right = 0
  while x < MAX_LIMIT:
    y1 = round(curve(x),ROUND_DECIMALS)
    y2 = round(curve(x + dx), ROUND_DECIMALS)
    cur_left = (dx * y1)
#   print("Left: {0:.03f} + {1:.03f} = {2:.03f}    x = {3:.03f}".format(dx, y1, round(cur_left,ROUND_DECIMALS), x))
    cur_right = (dx * y2)
#   print("Right: {0:.03f} + {1:.03f} = {2:.03f}    x = {3:.03f}".format(dx, y2, round(cur_right,ROUND_DECIMALS), x))

    left = round(left + cur_left, ROUND_DECIMALS)
    right = round(right + cur_right, ROUND_DECIMALS)
#   print("x = " + str(x) + "\t\ty = " + str(y1))
    x = round(x + dx, ROUND_DECIMALS)

# print()
  print("Left area: " + str(left))
  print("Right area: " + str(right))

  return round((right + left) / 2, ROUND_DECIMALS)


rect = 100000
s = riemann_sum(rect)
print()
print("Riemann Sum: {:.03f}".format(s))
print()
