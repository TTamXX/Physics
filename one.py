import math

def decartTOspher(x, y, z, count):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = math.acos(z / r)
    phi = math.atan2(y, x)

    return round(r, count), round(math.degrees(theta), count), round(math.degrees(phi), count)


def spherTOdecart(r, theta, phi, count):
    x = r * math.sin(math.radians(theta)) * math.cos(math.radians(phi))
    y = r * math.sin(math.radians(theta)) * math.sin(math.radians(phi))
    z = r * math.cos(math.radians(theta))

    return round(x, count), round(y, count), round(z, count)


whatsystem = input("Введите систему координат для перевода: 'decart' для декартовых или 'spher' для сферических: ")
count = int(input("Введите точность вычислений: "))

if whatsystem == 'decart':
    coorinats = input("Введите координаты в формате x, y, z: ").split(", ")
    x, y, z = map(float, coorinats)
    r, theta, phi = decartTOspher(x, y, z, count)
    print(f"Координаты в сферической системе: r = {r}, theta = {theta}, phi = {phi}")

elif whatsystem == 'spher':
    coorinats = input("Введите координаты в формате r, theta, phi: ").split(", ")
    r, theta, phi = map(float, coorinats)
    x, y, z = spherTOdecart(r, theta, phi, count)
    print(f"Координаты в декартовой системе: x = {x}, y = {y}, z = {z}")

else:
    print("Некорректный выбор системы координат.")

#формулы перехода
#Из декартовой в сферическую:
#r = sqrt(x^2 + y^2 + z^2)
#theta = acos(z / r)
#phi = atan2(y, x)
#Из сферической в декартовую:
#x = r * sin(theta) * cos(phi)
#y = r * sin(theta) * sin(phi)
#z = r * cos(theta)



