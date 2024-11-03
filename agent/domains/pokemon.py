class Pokemon:
    def __init__(self, name, hp, retreat_cost):
        self.name = name                     # ポケモンの名前
        self.hp = hp                         # 体力
        self.attached_energy = 0             # アタッチされたエネルギー
        self.retreat_cost = retreat_cost     # にげるコスト
        self.moves = []                      # わざのリスト（Moveインスタンスのリスト）
        self.abilities = []                  # 特性のリスト（Abilityインスタンスのリスト）
        
        # 状態異常のフラグ
        self.status_conditions = {
            "poisoned": False,  # どく
            "burned": False,    # やけど
            "asleep": False,    # ねむり
            "confused": False,  # こんらん
            "paralyzed": False  # 麻痺
        }

    def attach_energy(self, amount):
        """エネルギーをアタッチする"""
        self.attached_energy += amount
        print(f"{self.name}に{amount}エネルギーをアタッチしました（合計: {self.attached_energy}）")

    def take_damage(self, damage):
        """ダメージを受ける"""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name}は気絶しました")
        else:
            print(f"{self.name}は{damage}ダメージを受けました（残りHP: {self.hp}）")

    def add_move(self, move):
        """わざを追加する"""
        self.moves.append(move)

    def add_ability(self, ability):
        """特性を追加する"""
        self.abilities.append(ability)

    def set_status(self, status):
        """状態異常を設定する"""
        if status in self.status_conditions:
            self.status_conditions[status] = True
            print(f"{self.name}は{status}状態になりました")
        else:
            print(f"無効な状態異常: {status}")

    def clear_status(self, status=None):
        """特定の状態異常を解除するか、全ての状態異常を解除する"""
        if status:
            if status in self.status_conditions:
                self.status_conditions[status] = False
                print(f"{self.name}の{status}状態が解除されました")
            else:
                print(f"無効な状態異常: {status}")
        else:
            for key in self.status_conditions:
                self.status_conditions[key] = False
            print(f"{self.name}の全ての状態異常が解除されました")

    def is_status_active(self, status):
        """指定された状態異常が発動中か確認する"""
        return self.status_conditions.get(status, False)

    def use_move(self, move_name):
        """指定した名前のわざを使用する"""
        for move in self.moves:
            if move.name == move_name:
                if move.energy_cost <= self.attached_energy:
                    print(f"{self.name}は「{move.name}」を使った！")
                    self.attached_energy -= move.energy_cost
                    return move.damage
                else:
                    print(f"エネルギーが足りません（必要: {move.energy_cost}, 現在: {self.attached_energy}）")
        return 0  # ダメージなし

    def __repr__(self):
        status = ", ".join([key for key, value in self.status_conditions.items() if value])
        return (f"Pokemon(name={self.name}, hp={self.hp}, attached_energy={self.attached_energy}, "
                f"retreat_cost={self.retreat_cost}, status=[{status}], moves={self.moves}, abilities={self.abilities})")
