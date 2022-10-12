from RPSLS_player import RPSLS_player

class P17566(RPSLS_player):
  shots = []
  def __init__(self):
    import random
    random.seed(999)

  def shoot(self):
    import random
    random.seed(999)
    if(len(P17566.shots) == 0):
      return "paper" 
    elif (len(P17566.shots)<20):
      P17566.shots[-1]
    elif (P17566.shots.count(max(P17566.shots))/len(P17566.shots) > 0.7):
      if(max(P17566.shots) == "rock"):
        return "paper"
      elif(max(P17566.shots) == "scissors"):
        return "rock"
      elif(max(P17566.shots) == "paper"):
        return "scissors"
      elif(max(P17566.shots) == "lizard"):
        return "scissors"
      elif(max(P17566.shots) == "spock"):
        return "lizard"
    else:
      return P17566.shots[-1]
  
  def update(self, result: str, competitor_shot: str):
    P17566.shots.append(competitor_shot)