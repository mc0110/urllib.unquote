 MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#

# Use this for micropython modules
#
# Get formula-entries from browser unicodes (html5) needs
# a parsing and converting process to a utf-8 string
# normally this can be done with the urllib-module
# this is a extrem short form, developed for html-forms

# input string e.g. "a%C3%A4" -> "aü"

def unquote(s):
    if '%' not in s:
        return s
    s = s.split("%")
    a = s[0].encode("utf-8")
    for i in s[1:]:
        a = a + bytearray.fromhex(i[:2]) + i[2:].encode("utf-8")
    return a.decode("utf-8")    
