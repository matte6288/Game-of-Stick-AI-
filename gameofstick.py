import random
import turtle
sticks=20
bot1moves=[[1],[1,2]]
bot2moves=[[1],[1,2]]
player=True
bot1roundmoves=[]
bot2roundmoves=[]
tortellini = turtle.Turtle()
learningRounds=0
explaination=["Above is a visual of the player 1 AI learning","Numbers above each box represents the amount of sticks left in the game","The more red a square is the more likely the AI is to take 1 stick","The more green the more likely the AI is to take 2","The more blue the more likely the AI is to take 3"]
for i in range(0,18):
  bot1moves.append([1,2,3])
  bot2moves.append([1,2,3])

gameMode = input("Play against the bot or watch the bots play? (watch or play)")
def reset():
  global sticks
  global bot1roundmoves
  global bot2roundmoves
  if player:
    if learningRounds==0:
     print "player 1 wins!"
     draw()
    for i in bot1roundmoves:
      bot1moves[i[0]-1].append(i[1])

    
  if not player:
    if gameMode=="watch":
      print "player 2 wins!"
    if gameMode=="play" and learningRounds==0:
      print "You win!"
    for i in bot2roundmoves:
      bot2moves[i[0]-1].append(i[1])
  sticks=20
  bot1roundmoves=[]
  bot2roundmoves=[]
      

def draw():
  
  tortellini.speed(10000)
  tortellini.penup()
  tortellini.goto(-180,180)
  tortellini.pendown()
  count=0
  color=[]
  for i in bot1moves:
    tortellini.pendown()
    threes=0
    ones=0
    twos=0
    for l in i:
      if l==3:
        threes=threes+1
      if l==1:
        ones=ones+1
      if l==2:
        twos=twos+1
    
    threeBlue=threes/len(i)*255
    oneRed=ones/len(i)*255
    twoGreen=twos/len(i)*255
    color=[oneRed,twoGreen,threeBlue]
    tortellini.color(color)
    tortellini.begin_fill()
    for k in range(0,4):
      tortellini.forward(40)
      tortellini.right(90)
    tortellini.end_fill()
    count+=1
    tortellini.color("black")
    tortellini.write(count, move=False, align="left", font=("Arial", 10, "normal"))
    tortellini.penup()
    tortellini.forward(52)
    if count%5==0:
      tortellini.goto(-180,180-(count*12))
      
for i in range(0,5):
  tortellini.penup()
  tortellini.goto(-180,-90+(-15*i))
  tortellini.pendown()
  tortellini.write(explaination[i], move=False, align="left", font=("Arial",8, "normal"))
draw()
if gameMode=="watch":
  for i in range(0,10000):
    while sticks>0:
      if player:
        move=random.choice(bot1moves[sticks-1])
        bot1roundmoves.append([sticks,move])
        sticks=sticks-move
        print "bot 1 took "+str(move)+" sticks. There are "+str(sticks)+" left"
        player=False
      elif not player:
        move=random.choice(bot2moves[sticks-1])
        bot2roundmoves.append([sticks,move])
        sticks=sticks-move
        print "bot 2 took "+str(move)+" sticks. There are "+str(sticks)+" left"
        player=True
    reset()

if gameMode=="play":
  learningRounds=raw_input("How many rounds will you let the bot learn for?")
  learningRounds=int(learningRounds)
  for i in range(0,learningRounds):
    while sticks>0:
      if player:
        move=random.choice(bot1moves[sticks-1])
        bot1roundmoves.append([sticks,move])
        sticks=sticks-move
        player=False
      elif not player:
        move=random.choice(bot2moves[sticks-1])
        bot2roundmoves.append([sticks,move])
        sticks=sticks-move
        player=True
    reset()
  learningRounds=0
  for i in range(0,10000):
    while sticks>0:
      if player:
        move=random.choice(bot1moves[sticks-1])
        bot1roundmoves.append([sticks,move])
        sticks=sticks-move
        print "bot 1 took "+str(move)+" sticks. There are "+str(sticks)+" left"
        player=False
      elif not player:
        move=raw_input("How many sticks will you take? (1, 2, or 3)")
        intMove=int(move)
        while intMove>sticks or intMove<1 or intMove>3:
          print("You can't take that many sticks")
          print("There are "+str(sticks)+" left")
          move=input("How many sticks will you take?")
          intMove=int(move)
        sticks=sticks-intMove
        print "you took "+str(move)+" sticks. There are "+str(sticks)+" left"
        player=True
    reset()
  
  






