# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))
# 20 and 20.0 are treated as the same value in sets, but '20' is a string so it is different