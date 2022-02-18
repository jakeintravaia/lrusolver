# lrusolver
This simple python script prints out a simple simulation of page insertion using an LRU algorithm.

# How to use

Simply edit the <b>cache_size</b> and <b>inserts</b> variables to your liking and run the program, it will output a organized series of inserts while logging page faults and inserts.

```
cache_size = 4 # Amount of pages in cache
inserts = [0, 3, 4, 3, 8, 6, 9, 1, 4, 9, 7, 9, 5, 3, 1, 2, 4] # Change these values according to problem set
```

# Sample output

With default settings, this is what you can expect the output to look like

```
INSERT PAGE 0
====================
Value: 0
Value: EMPTY
Value: EMPTY
Value: EMPTY
====================
INSERT PAGE 3
====================
Value: 0
Value: 3
Value: EMPTY
Value: EMPTY
====================
INSERT PAGE 4
====================
Value: 0
Value: 3
Value: 4
Value: EMPTY
====================
INSERT PAGE 3
====================
Value: 0
Value: 3
Value: 4
Value: EMPTY
====================
INSERT PAGE 8
====================
Value: 0
Value: 3
Value: 4
Value: 8
====================
***PAGE FAULT***
INSERT PAGE 6
====================
Value: 6
Value: 3
Value: 4
Value: 8
====================
***PAGE FAULT***
INSERT PAGE 9
====================
Value: 6
Value: 3
Value: 9
Value: 8
====================
***PAGE FAULT***
INSERT PAGE 1
====================
Value: 6
Value: 1
Value: 9
Value: 8
====================
***PAGE FAULT***
INSERT PAGE 4
====================
Value: 6
Value: 1
Value: 9
Value: 4
====================
INSERT PAGE 9
====================
Value: 6
Value: 1
Value: 9
Value: 4
====================
***PAGE FAULT***
INSERT PAGE 7
====================
Value: 7
Value: 1
Value: 9
Value: 4
====================
INSERT PAGE 9
====================
Value: 7
Value: 1
Value: 9
Value: 4
====================
***PAGE FAULT***
INSERT PAGE 5
====================
Value: 7
Value: 5
Value: 9
Value: 4
====================
***PAGE FAULT***
INSERT PAGE 3
====================
Value: 7
Value: 5
Value: 9
Value: 3
====================
***PAGE FAULT***
INSERT PAGE 1
====================
Value: 1
Value: 5
Value: 9
Value: 3
====================
***PAGE FAULT***
INSERT PAGE 2
====================
Value: 1
Value: 5
Value: 2
Value: 3
====================
***PAGE FAULT***
INSERT PAGE 4
====================
Value: 1
Value: 4
Value: 2
Value: 3
====================
Total Inserts: 17
Total Faults: 10
```
