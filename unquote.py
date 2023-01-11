def unquote(s):
    if '%' not in s:
        return s
    s = s.split("%")
    a = s[0].encode("utf-8")
    for i in s[1:]:
        a = a + bytearray.fromhex(i[:2]) + i[2:].encode("utf-8")
    return a.decode("utf-8")    
