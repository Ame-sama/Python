List = [1, 2, 3, 4, 5]
print(List) 
List = List + [6, 7, 8, 9, 10] # thêm 1 mảng vào mảng List
print(List)
List.append(11) # thêm 1 phần tử vào mảng List
List.insert(0, 0) # thêm 1 phần tử vào mảng List tại vị trí 0
List.remove(0) # xóa 1 phần tử trong mảng List
List.pop() # xóa phần tử cuối cùng trong mảng List
List.pop(0) # xóa phần tử đầu tiên trong mảng List
List.clear() # xóa toàn bộ phần tử trong mảng List
List.reverse() # đảo ngược mảng List
List.sort() # sắp xếp mảng List
List.sort(reverse=True) # sắp xếp mảng List theo chiều ngược lại
print(List.index(2)) # trả về vị trí của phần tử trong mảng List
print(List.count(1)) # trả về số lần xuất hiện của phần tử trong mảng List
print(List.copy()) # sao chép mảng List

# số đối tượng trong mảng
print(len(List))