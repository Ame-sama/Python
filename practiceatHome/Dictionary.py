thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
# Truy cập giá trị trong Dictionary
B = thisDict['brand'] # print(thisDict['brand'])
print(B)
M = thisDict['model']
print(M)
Y = thisDict['year']   
print(Y)
# Thêm và cập nhật giá trị trong Dictionary
thisDict['email'] = 'Ford@gmail.com'
E = thisDict['email']
print(E)
thisDict['year'] = 2020
Y = thisDict['year']
print(Y)
# Xóa cặp key-value trong Dictionary
del thisDict['email']

Y = thisDict.pop('year')
print(Y)
# Trả về tất cả các key trong Dictionary   
K = thisDict.keys()
print(K)
# Trả về tất cả các value trong Dictionary
V = thisDict.values()  # print(thisDict.values())
print(V)
# Đếm số cặp key-value trong Dictionary
print(len(thisDict)) 
# truy cập vào key đã tạo
print(thisDict['brand'])
print(thisDict['model'])
# Loại bỏ khóa và trả về giá trị trong Dictionary
value = thisDict.pop('model')
print(value)
print(thisDict)
# Xóa tất cả các cặp key-value trong Dictionary
thisDict.clear()
print(thisDict)
# Cập nhật Dictionary
thisDict.update({'color' : 'blue'})
print(thisDict)
# item() trả về tất cả các cặp key-value trong Dictionary
print(thisDict.items())
# copy() sao chép Dictionary
print(thisDict.copy())
# get() trả về giá trị của key 
print(thisDict.get('color'))
# setdefault() trả về giá trị của key, nếu key không tồn tại thì thêm key vào Dictionary
print(thisDict.setdefault('Brand', 'Lamborghini'))
# popitem() xóa cặp key-value cuối cùng trong Dictionary
print(thisDict.popitem())
print(thisDict)
# Xoá Dictionary
# del thisDict
