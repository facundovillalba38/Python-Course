# App to create a basketball roster program

players = []


pg = input("Who is your point guard? ")
pg = pg.title()
players.append(pg)

sg = input("Who is your small guard? ")
sg = sg.title()
players.append(sg)

sf = input("Who is your small forward? ")
sf = sf.title()
players.append(sf)

pf = input("Who is your power forward? ")
pf = pf.title()
players.append(pf)

c = input("Who is your center? ")
c = c.title()
players.append(c)


print("\tYour starting 5 for this season:")
for player in players:
     print("\t\t",player)

injured_player = players.pop(1)
print(injured_player)

print("Oh no",injured_player,"is injured.")
print("Your team only has",len(players),"players")
new_player = input("Who will take the spot? ")
new_player = new_player.title()
players.insert(1,new_player)

print("\tYour final 5 for this season:")
for player in players:
     print("\t\t",player)

