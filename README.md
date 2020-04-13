# clitable
print table at cli.
![GitHub](https://img.shields.io/github/license/kotaoue/clitable)

# usage
When Arguments type "list" is passed to "print_table".
```
import clitable

target_list = [
    {'id': 1, 'time': 1586995200, 'name': 'kota', 'do': 'breakfast'},
    {'id': 2, 'time': 1587006000, 'name': 'kota', 'do': 'lunch'},
    {'id': 3, 'time': 1587016800, 'name': 'kota', 'do': 'teatime'},
    {'id': 4, 'time': 1587031200, 'name': 'kota', 'do': 'dinner'},
]

clitable.print_table(target_list)
```
The following result will be printed.
```
+----+------------+------+-----------+
| id | time       | name | do        |
+----+------------+------+-----------+
| 1  | 1586995200 | kota | breakfast |
| 2  | 1587006000 | kota | lunch     |
| 3  | 1587016800 | kota | teatime   |
| 4  | 1587031200 | kota | dinner    |
+----+------------+------+-----------+ 
```
