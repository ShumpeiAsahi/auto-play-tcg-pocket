class BattleField:
    def __init__(self):
        self.active_pokemon = None                   # プレイヤーのアクティブポケモン
        self.active_opponent_pokemon = None          # 相手のアクティブポケモン
        self.benched_pokemons = []                   # プレイヤーのベンチポケモンリスト
        self.opponent_benched_pokemons = []          # 相手のベンチポケモンリスト

    def set_active_pokemon(self, pokemon):
        """プレイヤーのアクティブポケモンを設定"""
        self.active_pokemon = pokemon
        print(f"アクティブポケモンに{pokemon.name}を設定しました")

    def set_active_opponent_pokemon(self, pokemon):
        """相手のアクティブポケモンを設定"""
        self.active_opponent_pokemon = pokemon
        print(f"相手のアクティブポケモンに{pokemon.name}を設定しました")

    def add_to_bench(self, pokemon, is_opponent=False):
        """ポケモンをベンチに追加。プレイヤーか相手かを指定"""
        if is_opponent:
            if len(self.opponent_benched_pokemons) < 5:  # ベンチの上限を5体と仮定
                self.opponent_benched_pokemons.append(pokemon)
                print(f"相手のベンチに{pokemon.name}を追加しました")
            else:
                print("相手のベンチは満員です")
        else:
            if len(self.benched_pokemons) < 5:
                self.benched_pokemons.append(pokemon)
                print(f"自分のベンチに{pokemon.name}を追加しました")
            else:
                print("自分のベンチは満員です")

    def remove_from_bench(self, pokemon, is_opponent=False):
        """ベンチからポケモンを削除"""
        bench = self.opponent_benched_pokemons if is_opponent else self.benched_pokemons
        if pokemon in bench:
            bench.remove(pokemon)
            print(f"{pokemon.name}をベンチから削除しました")
        else:
            print(f"{pokemon.name}はベンチにいません")

    def __repr__(self):
        return (f"BattleField(\n"
                f"  Active Pokemon: {self.active_pokemon},\n"
                f"  Active Opponent Pokemon: {self.active_opponent_pokemon},\n"
                f"  Benched Pokemons: {self.benched_pokemons},\n"
                f"  Opponent Benched Pokemons: {self.opponent_benched_pokemons}\n)")
