carros = ["Ford","Honda", "Toyota"]

for c in carros:
    print(c)

carros.append("Mitsubishi")
print()
for c in carros:
    print(c)
print()

carros.pop(1)
carros.append("BMW")
carros.append("Audi")
carros.remove("Toyota")

for c in carros:
    print(c)