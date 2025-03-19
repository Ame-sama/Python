class SieuNhan:
    def __init__(self, name, weapon, hp): # Constructor (n): Hàm khởi tạo
        self.name = name
        self.weapon = weapon 
        self.hp = hp
    def hello(self): # Method (n): Phương thức
        return 'Hello there!, i am', self.name
sieunhanA = SieuNhan('Sieu nhan do', 'Sword', 100) # Object (n): Đối tượng
print('Tên của siêu nhân:', sieunhanA.name)
print('Vũ khí:', sieunhanA.weapon)
print('Máu:', sieunhanA.hp)
print(sieunhanA.hello()) 
