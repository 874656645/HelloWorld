def format_name(s):
    s = s.strip()           # 去除字符串首尾的空格
    if len(s) < 1:
        raise Exception('name can not be empty.')
    return s[0].upper() + s[1:].lower()
    # return s.capitalize()
    # return s.title()

print(list(map(format_name, [' adam ', 'LISA', 'barT'])))