#### string ####
# count
changsoo = "Hello Changsoo!"
count_ = changsoo.count('o')
print(count_)  # 3
# find
find_ = changsoo.find('oo')
print(find_)  # 12
find_ = changsoo.find('o0')
print(find_)  # -1
# index
find_ = changsoo.index('oo')
print(find_)  # 12
try:
    find_ = changsoo.index('o0')
    print(find_)  # error
except ValueError as e:
    print('error', e)

# join
changsoo = ['cha', 'ng', 'soo']
joined_cs = ''.join(changsoo)
print(joined_cs)  # changsoo
# lower, upper
changsoo = 'CHaNgSoO'
print(changsoo.lower())  # changsoo
print(changsoo.upper())  # CHANGSOO
# replace
print(changsoo.replace('SoO', 'su'))  # CHaNgsu
# split
changsoo = "Hello Python!"
print(changsoo.split('o'))  # ['Hell', ' Pyth', 'n!']


#### list ####
# len
changsoo = ['a', 'b', 'd', 'c']
print(len(changsoo))  # 4
# del
del changsoo[1]
print(changsoo)  # ['a', 'd', 'c']
# append
changsoo.append('e')
print(changsoo)  # ['a', 'd', 'c', 'e']

# .sort
changsoo = [10, 8, 11, 2]
changsoo.sort()
print(changsoo)  # [2, 8, 10, 11]
# reverse =True
changsoo.sort(reverse=True)
print(changsoo)  # [11, 10, 8, 2]
# sorted()
changsoo = sorted(changsoo)
print(changsoo)  # [2, 8, 10, 11]
# .reverse
changsoo.reverse()
print(changsoo)  # [11, 10, 8, 2]

# index
changsoo = ['가', '다', 'a', 10]
print(changsoo.index('a'))  # 2
try:
    print(changsoo.index('b'))  # error
except ValueError as e:
    print('error', e)
# insert
changsoo.insert(1, 'b')
print(changsoo)  # ['가', 'b', '다', 'a', 10]
# remove
changsoo.remove('a')
print(changsoo)  # ['가', 'b', '다', 10]
# pop
changsoo.pop()
print(changsoo)  # ['가', 'b', '다']
first = changsoo.pop(0)
print(first, changsoo)  # 가 ['b', '다']

# count
changsoo = [1, 1, 3, 4, 5]
print(changsoo.count(1))  # 2

# extend
changsoo = [1, 2, 3]
soochang = [4, 5, 6]
changsoochang = changsoo+soochang
print(changsoochang)  # [1, 2, 3, 4, 5, 6]
changsoo.extend(soochang)
print(changsoo)  # [1, 2, 3, 4, 5, 6]
print(changsoochang == changsoo)  # True


#### Dict ####
changsoo = {}
print(changsoo)  # {}
changsoo = {'a': 1, 'b': 2}
print(changsoo)  # {'a': 1, 'b': 2}
# add pair
changsoo['c'] = 3
print(changsoo)  # {'a': 1, 'b': 2, 'c': 3}
# del
del changsoo['a']
print(changsoo)  # {'b': 2, 'c': 3}
# key-value
print(changsoo['b'])  # 2
try:
    print(changsoo['a'])  # error
except KeyError as e:
    print('error', e)
# keys
print(changsoo.keys())  # dict_keys(['b', 'c'])
# values
print(changsoo.values())  # dict_values([2, 3])
# items
print(changsoo.items())  # dict_items([('b', 2), ('c', 3)])
# clear
print(changsoo.clear())  # None

# get
changsoo = {'c': 1, 'b': 2}
print(changsoo.get('b', None))  # 2
print(changsoo.get('a', None))  # None
# in : key exists?
print('b' in changsoo)  # True
print('a' in changsoo)  # False
