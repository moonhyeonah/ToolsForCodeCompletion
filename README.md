# ToolsForCodeCompletion

read_datafile.py
* Assign the filename you want to parse to 'infile'.
* The current encoding is UTF-8.


### Example
ex) infile: any.i.textual_collection.txt

```
parse time: 589.11s
0 typedef list_ge1_type_specifier_nonunique_declaration_specifier 
 48,1: typedef
 48,9: long
 48,14: unsigned
 48,23: int
 
54 long 
 48,9: long
 
106 unsigned 
 48,14: unsigned
...
```

The resulting list
```
[0, ['typedef', 'list_ge1_type_specifier_nonunique_declaration_specifier'], [(48, 1, 'typedef'), (48, 9, 'long'), (48, 14, 'unsigned'), (48, 23, 'int')]]
[54, ['long'], [(48, 9, 'long')]]
[106, ['unsigned'], [(48, 14, 'unsigned')]]
...
```
