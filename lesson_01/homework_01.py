# 1. Вывести строку "Hello, world!" (без кавычек) в консоль с помощью функции print.

print("Hello, World!")



# 2. Выведите строку в консоли “Я люблю:”, а затем 3 пронумерованных пункта с тем, что вам нравится

likes = ["Фильмы", "Minecraft", "Кока-кола"]

print("Я люблю:")
for i, item in enumerate(likes, 1):
    print(f"{i}. {item}")
