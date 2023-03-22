import time

# Izveido spēlētāja statusu.
player = {
    "name": "",
    "health": 100,
    "attack": 10,
    "defence": 5,
    "gold": 0
}

# Izveido pretinieka statusu.
enemy = {
    "name": "Orc",
    "health": 50,
    "attack": 25,
    "defence": 2,
    "gold": 10
}

# Izveido spēlētāja izskatu un pretinieka izskatu.
player_art = r"""
 |\             //
  \\           _!_
   \\         /___\
    \\        [+++]
     \\    _ _\^^^/_ _
      \\/ (    '-'  ( )
      /( \/ | {&}   /\ \
      \  / \     / _> )
        "`   >:::;-'`""'-.
            /:::/         \
           /  /||   {&}   |
          (  / (\         /
          / /   \'-.___.-'
        _/ /     \ \
       /___|    /___|
"""
enemy_art = r"""
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo"""

# Izveido funkciju lai veidotu ASCII animāciju


def print_art(art):
    print(art)
    time.sleep(1)

# izveido funkciju "Sākt spēli"


def start_game():
    print("Sveiki varoni!")
    player["name"] = input("Ievadiet savu vārdu: ")
    print("Sveiks varenais,", player["name"], "sāksim cīņu!")
    time.sleep(1)

# Izveido funkciju priekš spēlētāja gājiena


def player_turn():
    print_art(player_art)
    print("Tavs gājiens!")
    choice = input("Spied 1 lai uzbruktu un 2 lai aizsargātos: ")
    if choice == "1":
        enemy["health"] -= player["attack"]
        print("Tu uzbruki", enemy["name"], "un izdarīji", player["attack"], "damage!")
    elif choice == "2":
        player["defence"] += 2
        print("Tu aizsargāji sevi un uzlaboji savu aizsardzību par 2!")
    else:
        print("Nepareiza izvēle. Tu zaudēji savu gājienu.")
    time.sleep(1)

# Izveido funkciju priekš pretinieka gājiena


def enemy_turn():
    print_art(enemy_art)
    print("Pretinieka gājiens!")
    damage = max(enemy["attack"] - player["defence"], 0)
    player["health"] -= damage
    print(enemy["name"], "uzbruka tev un izdarīja", damage, "damage!")
    time.sleep(1)

# Izveido funkciju "Spēles beigas"


def end_game():
    if player["health"] <= 0:
        print("Tu zaudēji!")
    elif enemy["health"] <= 0:
        print("Tu uzvarēji!")
        player["gold"] += enemy["gold"]
        print("Tu ieguvi", enemy["gold"], "zeltu!")
    print("SPĒLES BEIGAS, Paldies par spēlēšanu!")

# Sāk spēli


start_game()

# Turpina spēli līdz tā beidzas
while player["health"] > 0 and enemy["health"] > 0:
    player_turn()
    enemy_turn()

# Beidz spēli
end_game()
