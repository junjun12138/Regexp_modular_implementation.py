

s = """
    <div class = 'jppy'><span id = '1'>发呢分</span></div>
    <div class = 'jay'><span id = '1'>送一</span></div>
    <div class = 'dve'><span id = '2'>数字</span></div>
    <div class = 'egv'><span id = '3'>我么</span></div>
    <div class = '2es'><span id = '4'>怕后面</span></div>
"""
#（？P<分组名字>正则表达式）可以单独从匹配正则的内容中进一步提取
import re
obj = re.compile(r"<div class = '.*?'><span id = '(?P<BIZUI>\d+)'>(?P<wawawa>.*?)</span></div>",re.S)   #re.S   匹配换行
les = obj.finditer(s)
for i in les:
    print(i.group("wawawa"))
    print(i.group("BIZUI"))
# print(list(les))