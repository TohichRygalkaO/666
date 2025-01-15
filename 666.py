
import random

class Room: #комната
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items if items else {}
        self.exits = exits if exits else {}

    def describe(self):
        print(f"\n{self.name}\n{self.description}")
        if self.items:
            print("Вы видите: " + ", ".join(self.items.keys()))
        else:
            print("Здесь ничего нет.")

class Player: # игрок его действия
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            self.current_room.describe()
        else:
            print("Там тупик вы не можете туда пойти!")

    def take_item(self, item_name):
        if item_name in self.current_room.items:
            self.inventory.append(item_name)
            print(f"Вы взяли {item_name}.")
            del self.current_room.items[item_name]
        else:
            print(f"{item_name} здесь нет.")

    def show_inventory(self):
        if self.inventory:
            print("В вашем инвентаре: " + ", ".join(self.inventory))
        else:
            print("К сожалению инвентарь пуст.")




# комнаты описание и вещи
room1 = Room("Темная комната", "Вы в очень темной комнате, тут ничего не видно.", 
              items={"ключ": "старый ключ"}, 
              exits={})
room2 = Room("Светлая комната", "Вы попали в светлую комнату, здесь много вещей.", 
              items={"фонарик": "яркий фонарик"}, 
              exits={})

room1.exits["вперед"] = room2  #выход из первой комнаты в вторую




# инициализация игрока
player = Player(room1)
player.current_room.describe()




#цикл
while True:
    action = input("\nЧто вы хотите сделать? (осмотреться/идти/взять/инвентарь) > ").lower()
    
    if action == "осмотреться":
        player.current_room.describe()
    elif action == "идти":
        direction = input("Куда вы хотите пойти? (вперед) > ").lower()
        player.move(direction)
    elif action == "взять":
        item_name = input("Что вы хотите взять? > ")
        player.take_item(item_name)
    elif action == "инвентарь":
        player.show_inventory()






    # Проверка случайного события
    if random.randint(1, 5) == 1:  # 20% шанс на случайное событие
        print("Неожиданно в комнате появился дух!")
        if "ключ" in player.inventory:
            print("Вы использовали ключ, после чего заперли духа!")
            break  # завершение 
        else:
            print("У вас нет ключа, вы не смогли сбежать от духа проиграли!")
            break  # завершение


