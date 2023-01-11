# urllib.unquote

## micropython urllib.unquote html5 -> utf-8

Normally, one uses the standard Python module *urllib* to translate return strings as GET or POST elements from Unicode to UTF-8. 

The module is not available for micropython. This small routine translates existing Unicodes according to the [HTML URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.ASP) and returns a UTF-8 string.

With reference to the ASCII Encoding Reference your browser will encode input, according to the character-set used in your page. The default character-set in HTML5 is UTF-8.

Get formula-entries from browser unicodes (html5) needs a parsing and converting process to a utf-8 string
normally this can be done with the urllib-module this is a extrem short form, developed for html-forms

Using the unquote-function with e.g. "a%C3%A4" -> "aü"