# agent/domains/battle.py

class Battle:
    def __init__(self, first_player="player"):
        self.turn = 1                        # ターン数
        self.player_points = 0               # 自分のポイント
        self.opponent_points = 0             # 相手のポイント
        self.result = None                   # 勝敗の結果 ('win', 'lose', 'draw' or None)
        self.first_player = first_player     # 先攻プレイヤー ('player' or 'opponent')
        self.current_turn_player = first_player  # 現在のターンプレイヤー

    def update_turn(self):
        """ターン数を1増やす"""
        self.turn += 1

    def next_turn(self):
        """次のターンに移行し、ターンプレイヤーを交代"""
        self.update_turn()
        if self.current_turn_player == "player":
            self.current_turn_player = "opponent"
        else:
            self.current_turn_player = "player"

    def add_points(self, player_points=0, opponent_points=0):
        """
        ポイントを追加
        player_points: 自分に加算するポイント
        opponent_points: 相手に加算するポイント
        """
        self.player_points += player_points
        self.opponent_points += opponent_points

    def check_result(self):
        """
        勝敗の判定を行う
        勝敗が決まっている場合、結果を返す
        """
        if self.player_points > self.opponent_points:
            self.result = "win"
        elif self.player_points < self.opponent_points:
            self.result = "lose"
        else:
            self.result = "draw"
        return self.result

    def reset(self):
        """バトルの状態をリセット"""
        self.turn = 1
        self.player_points = 0
        self.opponent_points = 0
        self.result = None
        self.current_turn_player = self.first_player

    def __repr__(self):
        return (f"Battle(turn={self.turn}, player_points={self.player_points}, "
                f"opponent_points={self.opponent_points}, result={self.result}, "
                f"first_player={self.first_player}, current_turn_player={self.current_turn_player})")
