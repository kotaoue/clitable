# clitable
print table at cli.

# usage
When Arguments type of "dict" are passed to "print_table".
```
import clitable

dict = {}
dict['foo'] = 'fighters'
dict['bar'] = 'on'
dict['hoge'] = 'piyo'

clitable.print_table(dict)
```
The following result will be printed.
```
+----------+-----+------+
| foo      | bar | hoge |
+----------+-----+------+
| fighters | on  | piyo |
+----------+-----+------+    
```
