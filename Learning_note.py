#20250126
#None無屬性替代位(非字串)
user_name = None
user_name = input("Enter you name :")

#f"字串{變數}"格式字串
apple_num = 6
print(f"You got {apple_num} apples.")

#20250127
#玩家角色資訊表
name = "Lopen"
level = 25
character_class = "Windrunner"
armor = int(12.0) #整數化
magic_resistance = 15.4
account_active = True #boolean布林值

print("Character Report")
print(f"{name} is a level {level} {character_class}.") #格式（綴）字串
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

# Don't edit below this line

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"level: {type(level).__name__}, name: {type(name).__name__}, character_class: {type(character_class).__name__}"
) #列出變數的類別屬性type(變數).__name__
print(
    f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
)
print(
    f"account_active: {type(account_active).__name__}"
)

#計算武器攻擊範圍
def area_of_circle(radius): #def定義功能名稱(參數替代位parameter)
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length) #呼叫定義功能並將變數參數值帶入參數替代位
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")

#計算三次攻擊
def triple_attack(damage_one, damage_two, damage_three):
    total_damage = damage_one + damage_two + damage_three
    return total_damage

attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")

#角色介紹
def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro
    
my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.
