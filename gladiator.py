# gladiator.py
base_hp = 90
base_sp = 20

class Gladiator:
    def __init__(self, name, str_, agi, vit, sta, int_):
        self.name = name
        self.hp = base_hp + (vit * 10)
        self.sp = base_sp + (sta * 3)
        self.sp_regen = 5
        self.str_ = str_
        self.agi = agi
        self.vit = vit
        self.sta = sta
        self.int_ = int_
