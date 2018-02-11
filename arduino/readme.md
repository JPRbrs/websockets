# Arduino documentation

The chip used to move the motors is a [L238D](http://pdf.datasheetcatalog.com/datasheet/stmicroelectronics/1330.pdf) and here is the pinning

chip pin | name | arduino pin
---------|------|------------
1 | Enable 1 | arduino D5
2 | In 1 | arduino D4
3 | out 1 | motor right motor active
4 & 5 | GND	| battery pack GND
6 | out 2 |	right motor GND
7 | in 2 | arduino D3
8 | V+ motor |battery pack 6V

9 | Enable 2 |	arduino D10
10 | In 3 |	arduino D9
11 | Out 3 | left motor GND
12 & 13 |  GND | battery pack GND
14 | out 4 | left motor active
15 |  in 4 | arduino D8
16 | V+	| battery pack 6V
