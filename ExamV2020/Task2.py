xs = {
'a' : 5,
'd' : 'hello',
'z' : 3.1415,
5 : 7
}
print(xs['a'] == 5)

print('hello' in xs.values())

print(list(xs.keys()) == ['a', 'd', 'z', 5])
print(list(xs.keys()))

print(7 == xs[5])
while True:
    text = input()
    if text == "":
        print("bye")
        break
    print(f"Your text had {len(text)} characthers")

