SELECT - unary
(1 table in 1 table out)

SELECT literally means select a subset of rows from the original table, and put those into a new table. Example:
```
ANSWER := SELECT ORDER WHERE ORDER < "1234"
                    ^  ----------^---------
	            Name of      Condition for
	     original table      selecting rows from this table
```

PROJECT chooses a subset of columns and put them in a new table
```
ANSWER := PROJECT customer OVER name, address
^                    ^     --------^---------
Name of	         Name of      Condition for
new table	   original col      selecting rows from this table
```

