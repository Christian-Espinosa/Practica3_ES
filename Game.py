import Player
class Game:
    
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        
    def get_score(self) -> str:
        p1 = self.player1.get_points()
        p2 = self.player2.get_points()

        if(p1 == p2):#Puntuacion menor que 3
            if(p1 == 0):
                return "Love-All"
            elif(p1 == 1):
                return "Fifteen-All"
            elif(p1 == 2):
                return "Thirty-All"
            elif(p1 >= 3):
                return "Deuce"
        if(p1 == 0):
            if(p2 == 1):
                return "Love-Fifteen"
            elif(p2 == 2):
                return "Love-Thirty"
            elif(p2 == 3):
                return "Love-Forty"
            elif(p2 >= 4):
                return "Win for player2"
        elif(p1 == 1):
            if(p2 == 0):
                return "Fifteen-Love"
            elif(p2 == 2):
                return "Fifteen-Thirty"
            elif(p2 == 3):
                return "Fifteen-Forty"
            elif(p2 >= 4):
                return "Win for player2"
        elif(p1 == 2):
            if(p2 == 0):
                return "Thirty-Love"
            elif(p2 == 1):
                return "Thirty-Fifteen"
            elif(p2 == 3):
                return "Thirty-Forty"
            elif(p2 >= 4):
                return "Win for player2"
        elif(p1 == 3):
            if(p2 == 0):
                return "Forty-Love"
            elif(p2 == 1):
                return "Forty-Fifteen"
            elif(p2 == 2):
                return "Forty-Thirty"
            elif(p2 >= 4):
                return "Advantage player2"
        elif(p1>=4):
            if(p2 <= (p1-2)):
                return "Win for player1"
            elif(p2 == (p1-1)):
                return "Advantage player1"
        if(p2>=4):
            if(p1 <= (p2-2)):
                return "Win for player2"
            elif(p1 == (p2-1)):
                return "Advantage player2"
            
    
    def won_point(self, player: Player) -> None:
        if self.player1.is_equal(player):
            self.player1.add_point()
        else:
            self.player2.add_point()