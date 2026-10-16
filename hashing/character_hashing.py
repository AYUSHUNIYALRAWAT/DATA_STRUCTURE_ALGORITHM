#counting frequency by using dictionary
s = "azyxyyzaaaa"
q = ["d","a","y","x"]
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0) + 1
for ch in q:
 print(ch,freq.get(ch,0))

#counting frequency by hashing
s = "azyxyyzaaaa"
q = ["d","a","y","x"]
hash_list = [0]*26
for ch in s :
    index = ord(ch)-97
    hash_list[index] += 1
for ch in q :
    index = ord(ch) -97
    print(ch,hash_list[index])