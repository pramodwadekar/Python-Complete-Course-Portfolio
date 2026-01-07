cricket=dict()
n=int(input("How many players = "))
for i in range(n):
    k=(input("Player name = "))
    v=eval(input("Player score = "))
cricket.update({k:v})
print("cricket player = ",cricket)
for i in cricket.keys():
    print(i)
player=input("player name = ")
run=cricket.get(player, -1)
if(run == -1):
    print("player is not present....")
else:
    print("{} score is = ".format(player,run))