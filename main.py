import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = round(((rollDice(6)*rollDice(12))/2)+10)
  return healthStat

def strength():
  strengthStat = round(((rollDice(6)*rollDice(8))/2)+12)
  return strengthStat

print("⚔️  EPIC BATTLE ⚔️")
print()
#input 1st character - generate/display stats
character1_name = input("Name your character: ")
character1_type = input("Character Type (Human, Elf, Wizard, Orc): ")
print()
print(character1_name)
character1_health = health()
character1_strength = strength()
print("HEALTH:", character1_health)
print("STRENGTH:", character1_strength)
print()

#input 2nd character - generate/display stats
character2_name = input("Name your character: ")
character2_type = input("Character Type (Human, Elf, Wizard, Orc): ")
print()
print(character2_name)
character2_health = health()
character2_strength = strength()
print("HEALTH:", character2_health)
print("STRENGTH:", character2_strength)

round = 1
winner = None

while True:
  time.sleep(3)
  os.system("clear")
  print("⚔️  Time to Battle ⚔️")
  print()
  
  # players each roll
  c1_roll = rollDice(6)
  c2_roll = rollDice(6)

  # calc diff between rolls
  difference = abs(character1_strength - character2_strength) + 1

  #eval winner of each round
  if c1_roll > c2_roll:
    character2_health -= difference
    if round == 1:
      print(character1_name, "wins the first blow!")
    else:
      print(f"{character1_name} wins round: {round}")
  elif c2_roll > c1_roll:
    character1_health -= difference
    if round == 1:
      print(character2_name, "wins the first blow!")
    else:
      print(f"{character2_name} wins round: {round}")
  print()
  print(character1_name)
  print("HEALTH:", character1_health)
  print()
  print(character2_name)
  print("HEALTH:", character2_health)
  print()
  time.sleep(3)

  #eval if either character has lost all their health - cont. to next round if not
  if character1_health <= 0:
    print(f"{character1_name} has died!")
    winner = character2_name
    break
  elif character2_health <= 0:
    print(f"{character2_name} has died!")
    winner = character1_name
    break
  else:
    print("Both characters still standing, on to the next round")
    round += 1
  time.sleep(1)
  os.system("clear")

#display winner
print()
print(f"{winner} has won in {round} rounds")