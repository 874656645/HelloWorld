''' 利用import ... as ...，还可以动态导入不同名称的模块。

Python 2.6/2.7提供了json 模块，但Python 2.5以及更早版本没有json模块，不过可以安装一个simplejson模块，这两个模块提供的函数签名和功能都一模一样。

试写出导入json 模块的代码，能在Python 2.5/2.6/2.7都正常运行。 '''

try:
    import json
except ImportError as identifier:
    import simplejson as json

print(json.dumps({'Python': 2.7}))

try:
    from cStringIO import StringIO
except ImportError as identifier:
    from io import StringIO

s = StringIO()
s.write('aaa')
lines = ['bbb', 'ccc']
s.writelines(lines)

s.seek(0)
print(s.read())
print(s.getvalue())

s.write('ttt')
print(s.getvalue())

s.writelines(['111', '222'])
s.seek(0)
print(s.readlines())
