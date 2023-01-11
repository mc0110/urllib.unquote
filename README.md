# urllib.unquote

micropython urllib.unquote html5 to utf-8

Normally, one uses the standard Python module *urllib* to translate return strings as GET or POST elements from Unicode to UTF-8. The module is not available for micropython. This small routine translates existing Unicodes according to the [table](https://www.w3schools.com/tags/ref_urlencode.ASP) and returns a UTF-8 string.