angles = [int(input()) for _ in range(3)]

if all(angles) and sum(angles) == 180:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
