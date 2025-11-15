
import os
import sys
import ctypes
import subprocess

def main():
    ctypes.windll.user32.keybd_event(0x7A, 0, 0, 0) 
    ctypes.windll.user32.keybd_event(0x7A, 0, 2, 0)  

    print("\n"*15)
    print(" "*18*6 + "ВАШ WINDOWS ЗАБЛОКИРОВАН")
    print(" "*14*6 + "ЧТОБЫ ЕГО РАЗБЛОКИРОВАТЬ ПЕРЕВЕДИТЕ НА КАРТУ 10 РУБЛЕЙ")
    print("\n"+" "*14*6 + "ПРИ ПОПЫТКИ ОБХОДА БЛОКИРОВКИ ВАШ ВИНДОВС СЛОМАЕТСЯ ")
    print("\n"*4)
    key = input(" "*4+"Пароьл: ")
    if key == "иди нахуй":
        print("Пароль правильный")
    else:
        print("Пароль не правильный")


if __name__ == "__main__":
    main()
    
    input("...")
