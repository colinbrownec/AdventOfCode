given t and d:
```
t_up + t_down = t
t_down * t_up > d
```

rewrite:
```
t_up = t - t_down
```

substitute:
```
t_down * (t - t_down) = d
-t_down ** 2 + t * t_down - d = 0
```

note:
```
a * x**2 + b * x + c = 0
a = -1
b = t
c = -d
```

solve:
```
t_down = (-t +/- sqrt(t ** 2 - 4 * -1 * -d)) / (2 * -1)
t_down = (t +/- sqrt(t ** 2 - 4 * d)) / 2
```