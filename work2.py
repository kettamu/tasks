__author__ = 'mityagov_vi'
d = {
    1: 1,
    2: 2,
    3: 4,
    4: 'qwe'
}
print(d)
d1 = {a: a+1 for a in range(7)}
print(d1)
d.update(d1)
print(d)
print(d.values())
print [x for x in enumerate("abcd")]