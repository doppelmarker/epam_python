def func(pos1=4, pos2=0, /, m=3, g=8, *args, kw1=1, kw2, kw3=3, **kwargs):
    local_vars = locals()
    for arg in local_vars:
        print(f"{arg} - {local_vars[arg]}", end="; ")
    print()


d = {"kw1": 2, "kw2": 4, "kw3": 6}
d1 = {"a": 8, "b": 8}
t = (1, 2, 3, 4, 5)
# func(2, *d, kw2=3, **d)
# func(1, 2, 3, 4, kw2=3, **d)
func(1, 2, 3, 4, **d1, **d)
func(*t, *t, *t, cp=312, **d, **d1)

d2 = {**d, **d1, **d, **d1}
print(d2)
