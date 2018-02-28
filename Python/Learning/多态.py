''' Python提供了open()函数来打开一个磁盘文件，并返回 File 对象。File对象有一个read()方法可以读取文件内容：

例如，从文件读取内容并解析为JSON结果：

import json
f = open('/path/to/file.json', 'r')
print json.load(f)

由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。

请尝试编写一个File-like Object，把一个字符串 r'["Tim", "Bob", "Alice"]'包装成 File-like Object 并由 json.load() 解析。
 '''

import json

class Student(object):
    def read(self):
        # json 对象必须先单引号后双引号
        return '["Bob", "Tim", "Alice"]'

s = Student()

print(json.load(s))
    