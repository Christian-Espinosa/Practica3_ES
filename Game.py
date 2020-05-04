import Player
class Game:
    
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
    
    def get_score(self) -> str:
        points_player1 = self.player1.get_points()
        points_player2 = self.player2.get_points()
        if points_player1 > 0:
            if points_player1 == points_player2:
                return "Fifteen-All"
            if points_player1 > points_player2:
                return "Fifteen-love"
        return "Love_All"
    
    def won_point(self, player: Player) -> None:
        if self.player1.is_equal(player):
            self.player1.add_point()
        else:
            self.player2.add_point()