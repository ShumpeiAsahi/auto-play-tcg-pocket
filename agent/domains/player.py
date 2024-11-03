from domains.card import Support


class Player:
    def __init__(self, name):
        self.name = name                      # プレイヤーの名前
        self.hand = []                        # 手札に入るカードのリスト
        self.support_used = False             # サポートカード使用フラグ
        self.energy_attached = False          # エネルギーアタッチフラグ

    def update_hands(self, cards):
        """手札を更新する"""
        self.hand = cards

    def use_support(self):
        """サポートカードを1ターンに1度だけ使用する"""
        for card in self.hand:
            if isinstance(card, Support) and not self.support_used:
                card.use()
                self.hand.remove(card)
                self.support_used = True
                print(f"{self.name}がサポートカード「{card.name}」を使用しました")
                return
        print(f"{self.name}はサポートカードを使用できません")

    def attach_energy(self, energy_card):
        """エネルギーを1ターンに1度だけポケモンにアタッチする"""
        if not self.energy_attached:
            self.energy_attached = True
            print(f"{self.name}がエネルギーをアタッチしました")
        else:
            print(f"{self.name}はこのターンで既にエネルギーをアタッチしています")

    def reset_turn_flags(self):
        """次のターンのためにサポートとエネルギー使用フラグをリセットする"""
        self.support_used = False
        self.energy_attached = False

    def __repr__(self):
        return (f"Player(name={self.name}, hand_size={len(self.hand)}, "
                f"support_used={self.support_used}, energy_attached={self.energy_attached})")
    
class Opponent:
    def __init__(self, name):
        self.name = name
        self.hand_count = 0

    def update_hands(self, count):
        """カードを引いて手札の枚数を増やす"""
        self.hand_count = count

    def __repr__(self):
        return f"Opponent(name={self.name}, hand_count={self.hand_count})"
