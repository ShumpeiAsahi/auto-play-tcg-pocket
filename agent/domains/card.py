class Card:
    def __init__(self, name, card_type):
        self.name = name              # カードの名前
        self.card_type = card_type    # カードの種類（例: "BasicPokemon", "EvolvedPokemon", "Item", "Support"）

    def __repr__(self):
        return f"{self.card_type}(name={self.name})"
    
class BasicPokemon(Card):
    def __init__(self, name, hp, retreat_cost):
        super().__init__(name, card_type="BasicPokemon")
        self.hp = hp                       # 体力
        self.retreat_cost = retreat_cost   # にげるコスト
        self.moves = []                    # わざのリスト
        self.abilities = []                # 特性のリスト

    def add_move(self, move):
        """わざを追加"""
        self.moves.append(move)

    def add_ability(self, ability):
        """特性を追加"""
        self.abilities.append(ability)

    def __repr__(self):
        return (f"BasicPokemon(name={self.name}, hp={self.hp}, retreat_cost={self.retreat_cost}, "
                f"moves={self.moves}, abilities={self.abilities})")

class EvolvedPokemon(BasicPokemon):
    def __init__(self, name, hp, retreat_cost, evolves_from):
        super().__init__(name, hp, retreat_cost)
        self.card_type = "EvolvedPokemon"    # カードの種類を上書き
        self.evolves_from = evolves_from     # 進化元ポケモンの名前

    def __repr__(self):
        return (f"EvolvedPokemon(name={self.name}, hp={self.hp}, retreat_cost={self.retreat_cost}, "
                f"evolves_from={self.evolves_from}, moves={self.moves}, abilities={self.abilities})")

class Item(Card):
    def __init__(self, name, effect):
        super().__init__(name, card_type="Item")
        self.effect = effect    # アイテムの効果

    def use(self):
        """アイテムの効果を発動"""
        print(f"{self.name}を使用しました: {self.effect}")

    def __repr__(self):
        return f"Item(name={self.name}, effect={self.effect})"
    
class Support(Card):
    def __init__(self, name, effect):
        super().__init__(name, card_type="Support")
        self.effect = effect    # サポートカードの効果

    def use(self):
        """サポートカードの効果を発動"""
        print(f"{self.name}を使用しました: {self.effect}")

    def __repr__(self):
        return f"Support(name={self.name}, effect={self.effect})"
