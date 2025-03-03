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

print("=========================")
print("Character Report Complete")
print("Data types:")
print(f"level: {type(level).__name__}, name: {type(name).__name__}, character_class: {type(character_class).__name__}") 
#列出變數的類別屬性type(變數).__name__
print(f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")

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


#20250128
#定義頭銜功能
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title #給出結果值

#定義頭銜功能測試
def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)#呼叫頭銜功能
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)#呼叫之後獲得的結果值
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")


#在開始點(entry point)進行功能呼叫之前先寫好功能定義
#一般entrypoint使用main作為簡單明瞭的開始點
#Python的def定義功能不需要按照順序

def main():           # defined first
    health = 10
    armor = 5
    add_armor(health, armor)  # calls add_armor
    #呼叫增加裝甲血量計算，並於下方定義功能

def add_armor(h, a):  # defined second
    new_health = h + a
    print_health(new_health)  # calls print_health
    #呼叫列印血量功能，並於下方定義

def print_health(new_health):  # defined third
    print(f"The player now has {new_health} health")

# call entrypoint last
#在最後呼叫開始點
main()

#將華氏(Fahrenheit)轉為攝氏(Celsius)
def to_celsius(f):
    return (5/9 * (f - 32))#輸出參數計算

def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)#100 degrees fahrenheit is 37.78 degrees celsius
test(88)#88 degrees fahrenheit is 31.11 degrees celsius
test(104)#104 degrees fahrenheit is 40.0 degrees celsius
test(112)#112 degrees fahrenheit is 44.44 degrees celsius

#小時轉換為秒
def hours_to_seconds(hours):
    return (hours * (60 * 60))

def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")

test(10)#10 hours is 36000 seconds
test(1)#1 hours is 3600 seconds
test(25)#25 hours is 90000 seconds

#定義如果沒有下return的話會回傳None
def say_hello():
    print("Hello!")

result = say_hello()
print(result)
#回傳Hello!跟None

#複數數值=引數(Argument)回傳以逗號分開
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values
    
dmg, mana = cast_iceblast(5, 100)#回傳參數的順序指定=引數(Argument)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90

#範例練習_轉職戰士
def become_warrior(full_name, power):
    title = f"{full_name} the warrior" #設定頭銜
    new_power = power + 1 #設定新能力
    return title, new_power

def main(): #設定開始點
    test("Frodo Baggins", 5)#測試數據
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2): #設定測試
    result1, result2 = become_warrior(input1, input2)#數據順序與呼叫功能
    print(result1, "has a power level of:", result2)

#執行起始點
main()
# Frodo Baggins the warrior has a power level of: 6
# Bilbo Baggins the warrior has a power level of: 11
# Gandalf The Grey the warrior has a power level of: 9001


#20250129

#引數(Argument) 是用於呼叫函式， 參數(Parameter) 是方法簽章(方法的宣告)。
#參數可為任何自訂義的佔位符，引數則為實際帶入數值
#參數 (Parameter)=建立功能（函式）時預設帶入的變數
#函式可以沒有參數，比如上面提到作為起始點的main()
# Default function parameters
# allow named parameters to be initialized with default values if no value or undefined is passed.

# Ref: MDN web docs - https://developer.mozilla.org/en-US/

# 引數 (Argument)
# Argument
# is an Array-like object accessible inside functions that contains the values of the arguments passed to that function.

# Ref: MDN web docs - https://developer.mozilla.org/en-US/

# 呼叫函式時，傳給該函式的參數的值

#使用=設定預設值
def get_punched(health, armor=0):#護甲預設值為0
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health



def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)

# Running tests for health 400 and armor 5
# ========================================
# Health: 400, Armor: 5
# Health after punch: 355
# ----------------------------------------
# Health: 400, Armor: 5
# Health after slash: 305
# ----------------------------------------
# Health: 400, Armor: no armor!
# Health after slash: 300
# ----------------------------------------
# Health: 400, Armor: no armor!
# Health after punch: 350
# ----------------------------------------

#練習題1
def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5
    greater_cursed = weapon_damage * 0.25
    return lesser_cursed, greater_cursed


# Don't modify below this line


def test(weapon_damage):
    print("Weapon's base damage:", float(weapon_damage))
    print("Cursing...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("With lesser curse the damage is:", float(lesser_cursed), "damage.")
    print("With greater curse the damage is:", float(greater_cursed), "damage.")
    print("=====================================")


def main():
    test(100)


main()

# Weapon's base damage: 100.0
# Cursing...
# With lesser curse the damage is: 50.0 damage.
# With greater curse the damage is: 25.0 damage.
# =====================================

#練習題2
def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enchanted_weapon = f"enchanted {weapon}"
    return enchanted_weapon, new_health


def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage} - Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()

# The target has 100 health.
# sword base damage: 50 - Enchanting and attacking.
# The target has been attacked with the enchanted sword.
# The target has 40 health remaining.
# =====================================
# The target has 500 health.
# axe base damage: 100 - Enchanting and attacking.
# The target has been attacked with the enchanted axe.
# The target has 390 health remaining.
# =====================================
# The target has 1000 health.
# bow base damage: 250 - Enchanting and attacking.
# The target has been attacked with the enchanted bow.
# The target has 740 health remaining.
# =====================================
