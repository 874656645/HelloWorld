# 利用匿名函数简化以下代码：
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print(list(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '   ', 'END'])))