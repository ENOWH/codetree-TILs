c = input()
a = float(input())
b = float(input())

print(f"{c}\n{a:.2f}\n{b:.2f}")
print("{0}\n{1:.2f}\n{2:.2f}".format(c, a, b))
print("%s\n%.2f\n%.2f" % (c, a, b))