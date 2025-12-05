result = []

for i in range(1, 6):
    string = input()
    found = False

    if "MOLANA" in string:
        found = True
    if "HAFEZ" in string:
        found = True

    if found:
        result.append(i)

if result:
    print(*result)
else:
    print("NOT FOUND!")

