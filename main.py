def jumlahkan(num_1: int, num_2: int = 10) -> int:
    return num_1 + num_2

class Angka:
    def __init__(self, number: int):
        self.number = number

    def add_new(self, other_num: int):
        self.number = jumlahkan(self.number, other_num)
