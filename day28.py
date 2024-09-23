import random, os, time

def rolldice(side):
  dice = random.randint(1,side)
  return dice
def healthstat():
  health = ((random.randint(1,6) * random.randint(1,12)) / 2) + 10
  return health
def strengthstat():
  strength = ((random.randint(1,6) * random.randint(1,12)) /2) + 12
  return strength

p1 = input("Name your legend: ")
t1 = input("Character Type (Human, Elf, Wizard, Orc): ")
h1 = healthstat()
s1 = strengthstat()
print(p1)
print("Health: ", h1)
print("Strength: ", s1)
print()
print("They are battling with?")
print()
p2 = input("Name your legend: ")
t2 = input("Character Type (Human, Elf, Wizard, Orc): ")
h2 = healthstat()
s2 = strengthstat()
print(p2)
print("Health: ", h2)
print("Strength: ", s2)

time.sleep(3)
os.system("clear")

round = 1
winner = None

while True:
  time.sleep(3)
  os.system("clear")
  print("\033[35m⚔️ BATTLE TIME ⚔️\033[0m")
  print()
  print("The battle begins!")
  print()
  p1roll = rolldice(6)
  p2roll = rolldice(6)
  
  difference = abs(s1 - s2) + 1
  
  if p1roll > p2roll:
    h1 -= difference
    if round == 1:
      print(p1, "wins the first blow")
    else:
      print(p1, "wins round", round)
      
  elif p2roll > p1roll:
    h2 -= difference
    if round == 1:
      print(p2, "wins the first blow")
    else:
      print(p2, "wins round", round)
    
  else:
    print(p1, "and", p2, "draw round", round)

  print()
  print(p1)
  print("Health: ", h1)
  print()
  print(p2)
  print("Health: ", h2)
  print()

  if h1 < 0:
    winner = p2
    print(p1, "\033[33mhas died!\033[0m")
    break
  elif h2 < 0:
    winner = p1
    print(p2, "\033[33mhas died!\033[0m")
    break
  else:
    print("And they're both standing for the next round")
    round +=1
    continue

time.sleep(3)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")