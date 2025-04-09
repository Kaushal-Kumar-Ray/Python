import os
import time
import pygame

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def gift_box():
    box = [
        "      _______",
        "     /       \\",
        "    /---------\\",
        "    |  HAPPY  |",
        "    | BIRTHDAY|",
        "    |  GIFT!  |",
        "    \\_________/"
    ]
    for line in box:
        print(line)
        time.sleep(0.2)

def print_cake(name):
    cake = f"""
          ,   ,   ,   , 
        |￣￣￣￣￣￣￣￣| 
        |  🎉 HAPPY 🎉  | 
        | BIRTHDAY {name.upper()}! | 
        |＿＿＿＿＿＿＿＿| 
           🍰  🎂  🍰

        [*]  [*]  [*]  [*]
         |    |    |    |
        *******************
        *   🎈     🎁     🎈   *
        *******************
    """
    print(cake)

def sing_song(name):
    lyrics = [
        "🎵 Happy birthday to you 🎵",
        "🎵 Happy birthday to you 🎵",
        f"🎵 Happy birthday dear {name} 🎵",
        "🎵 Happy birthday to you 🎵",
    ]
    for line in lyrics:
        print(line)
        time.sleep(1.5)

def play_song(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    # Wait until the song finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def start_party(name):
    clear()
    print("🎁 Unwrapping your gift...")
    time.sleep(1)
    gift_box()
    time.sleep(1)
    clear()
    print_cake(name)
    print("\n🎶 Playing the birthday song... 🎶\n")
    time.sleep(1)
    play_song('happy_birthday.mp3')
    sing_song(name)

if __name__ == '__main__':
    person_name = input("🎈 Enter the birthday person's name: ")
    start_party(person_name)
