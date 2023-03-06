ingredients = input()

ice_cream = 0
milk = 0
ice = 0

for ingred in ingredients:
  if ingred == "I":
    ice_cream += 1
  elif ingred == "M":
    milk += 1
  elif ingred == "C":
    ice += 1

if ice_cream < 2:
  print("I")
elif milk < 1:
  print("M")
elif ice < 3:
  print("C")
else:
  print("W")
