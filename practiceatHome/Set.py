thisSet = {'apple', 'banana', 'cherry'}
# Thêm một phần tử vào Set
thisSet.add('kiwi')
# Thêm nhiều phần tử vào Set
thisSet.update(['orange', 'mango', 'grapes'])
# Xóa một phần tử trong Set sẽ báo lỗi nếu phần tử không tồn tại
thisSet.remove('banana')
# Xóa một phần tử trong Set mà không báo lỗi nếu phần tử không tồn tại
thisSet.discard('banana')
# Xóa phần tử cuối cùng trong Set
thisSet.pop()
# Xóa toàn bộ phần tử trong Set
thisSet.clear()
# Hợp nhất 2 hoặc nhiều Set
Set1 = {'a', 'b', 'c'}
Set2 = {1, 2 , 3}
Set3 = {'e', 'f', 'g'}
unionSet = Set1.union(Set2, Set3)
print(unionSet)
# Giao của 2 hoặc nhiều Set (Intersection)
S1 = {'Faker', 'Bang', 'Wolf'}
S2 = {'Bang', 'Faker', 'Teddy'}
S3 = {'Gumayusi', 'Faker', 'Bang'}
intersectionSet = S1.intersection(S2, S3)
print(intersectionSet) 
# intersection_update 
S1.intersection_update(S2, S3)
print(S1)
# Hiệu của 2 hoặc nhiều Set (Difference)
S4 = {'Faker', 'Bang', 'Wolf'}
S5 = {'Bang', 'Faker', 'Teddy'}
S6 = {'Gumayusi', 'Faker', 'Bang'}
differenceSet = S6.difference(S4, S5)
print(differenceSet)
# difference_update
S6.difference_update(S4, S5)
print(S6)
# Trả về tất cả các phần tử không trùng nhau của 2 Set (Symmetric Difference)
S7 = {'1', '2', '3'}
S8 = {'2', '3', '4'}
symmetricDifferenceSet = S7.symmetric_difference(S8) 
print(symmetricDifferenceSet)
# symmetric_difference_update
S7.symmetric_difference_update(S8)
print(S7)
# Kiểm tra xem Set có chứa phần tử hay không
print('1' in S7)
print('Faker' in S7)
# Copy Set
copySet = S7.copy()
print(copySet)
# print(S7.copy())
# Xóa Set
# del S7
print(thisSet)
print(sorted(thisSet))
print(len(thisSet))