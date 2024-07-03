import re
p = re.compile(r"[0-9]{2,4}\\[0-9]{2,4}", re.IGNORECASE)
s = input("Введите строку: ")
str_list = p.findall(s)
for s in str_list:
    j = s.find("\\")
    s_l = s[:j]
    s_r = s[j+1:]
    while len(s_l) < 4:
        s_l = "0"+s_l
    while len(s_r) < 5:
        s_r = "0"+s_r
    print(s_l+"\\"+s_r)