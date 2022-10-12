from RPSLS_player import RPSLS_player

class P00000(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    import random
    _proper_shootings = ["rock", "paper", "scissors", "lizard", "spock"]
    return random.choice(_proper_shootings)
  
  def update(self, result: str, competitor_shot: str):
    pass