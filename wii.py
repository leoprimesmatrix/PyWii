import pygame
import random
import time
import colorama
import os # fixer
from colorama import Fore,Back,Style
colorama.init()
pygame.init()
pygame.mixer.init()
os.system("") # fixer v2


class game():
    def WII_SHOP(self):
        self.TITLE = self.LIGHTRED + "| Wii Shop |"
        self.PRINT(self.TITLE)
        self.NEWEST_GAME = self.GOLD + "[NEWEST GAME] 1. Super Mario Bros. 3 | " + self.RED + "CONTACT TO PLAY"
        self.GAME1 = self.MAGENTA + "2. Space Shooter 4: One Final Adventure | PLAY NOW!"
        self.GAME2 = self.GREEN + "3. Space Shooter 3 | PLAY NOW!"
        self.GAME3 = self.LIGHTBLACK + "4. Prime's Flappy Bird | " + self.RED + "CONTACT TO PLAY"
        self.PRINT(self.NEWEST_GAME)
        self.PRINT(self.GAME1)
        self.PRINT(self.GAME2)
        self.PRINT(self.GAME3)
        self.SHOP_INPUT = self.NONE
        while self.SHOP_INPUT != "PLACEHOLDER":
            self.SHOP_INPUT_TEXT = self.GREEN + "Select Game: "
            self.SHOP_INPUT = self.INPUT(self.SHOP_INPUT_TEXT)
            self.SHOP_INPUT = self.SHOP_INPUT.lower()
            if self.SHOP_INPUT == "super mario bros. 3":
                self.WII_SELECT.play()
                self.NEWEST_GAME_INPUT = self.GOLD + "Super Mario Bros. 3 | Wii Shop"
                self.PRINT(self.NEWEST_GAME_INPUT)
                self.NEWEST_GAME_INPUT_TEXT = self.YELLOW + "1. Purchase | " + self.LIGHTRED + "2. Go Back "
                self.NEWEST_GAME_INPUT = self.INPUT(self.NEWEST_GAME_INPUT_TEXT)
                if self.NEWEST_GAME_INPUT == "1":
                    self.WII_SELECT.play()
                    self.NEWEST_GAME_PURCHASE_TEXT = self.LIGHTRED + "Please enter your purchase code to continue (Don't have one? Head to the help section in the menu for information.): "
                    self.NEWEST_GAME_PURCHASE = self.INPUT(self.NEWEST_GAME_PURCHASE_TEXT)
                    if self.NEWEST_GAME_PURCHASE == "jD6-hFy-aj6":
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_SUCCESS = self.GOLD + "SUCCESFULLY PURCHASED GAME!"
                        self.PRINT(self.NEWEST_GAME_SUCCESS)
                        self.SMB3_INPUT = self.INPUT("Would you like to get the game as an .html file? (y/n)")
                        if self.SMB3_INPUT == "y":
                            self.PRINT(self.GOLD + "Unable to find game. [ERROR CODE 404]")
                        self.WAIT(1)
                        self.NEWEST_GAME_SUCCESS_INSTRUCTION = self.LIGHTGREEN + "Contact PrimeDev#2349 through Discord to download the game. For more information, please go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_SUCCESS_INSTRUCTION)
                    else:
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_FAILED_TEXT = self.LIGHTRED + "Invalid purchase code. You're either typing it wrong, or your current purchase code has expired. For more help, go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_FAILED_TEXT)

                if self.NEWEST_GAME_INPUT == "2":
                    self.welcome()
                    break

            if self.SHOP_INPUT == "space shooter 4" or self.SHOP_INPUT == "space shooter 4: one final adventure":
                self.WII_SELECT.play()
                self.NEWEST_GAME_INPUT = self.GOLD + "Space Shooter 4: One Final Adventure | Wii Shop"
                self.PRINT(self.NEWEST_GAME_INPUT)
                self.NEWEST_GAME_INPUT_TEXT = self.YELLOW + "1. Purchase | " + self.LIGHTRED + "2. Go Back "
                self.NEWEST_GAME_INPUT = self.INPUT(self.NEWEST_GAME_INPUT_TEXT)
                if self.NEWEST_GAME_INPUT == "1":
                    self.WII_SELECT.play()
                    self.NEWEST_GAME_PURCHASE_TEXT = self.LIGHTRED + "Please enter your purchase code to continue (Don't have one? Head to the help section in the menu for information.): "
                    self.NEWEST_GAME_PURCHASE = self.INPUT(self.NEWEST_GAME_PURCHASE_TEXT)
                    if self.NEWEST_GAME_PURCHASE == "SP4-FINAL-ADVENTURE":
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_SUCCESS = self.GOLD + "SUCCESFULLY PURCHASED GAME!"
                        self.PRINT(self.NEWEST_GAME_SUCCESS)
                        self.WAIT(1)
                        self.NEWEST_GAME_SUCCESS_INSTRUCTION = self.LIGHTGREEN + "Play Now! [https://scratch.mit.edu/projects/651198900/]"
                        self.PRINT(self.NEWEST_GAME_SUCCESS_INSTRUCTION)
                    else:
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_FAILED_TEXT = self.LIGHTRED + "Invalid purchase code. You're either typing it wrong, or your current purchase code has expired. For more help, go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_FAILED_TEXT)

                if self.NEWEST_GAME_INPUT == "2":
                    self.welcome()
                    break

            if self.SHOP_INPUT == "space shooter 3":
                self.WII_SELECT.play()
                self.NEWEST_GAME_INPUT = self.GOLD + "Space Shooter 3 | Wii Shop"
                self.PRINT(self.NEWEST_GAME_INPUT)
                self.NEWEST_GAME_INPUT_TEXT = self.YELLOW + "1. Purchase | " + self.LIGHTRED + "2. Go Back "
                self.NEWEST_GAME_INPUT = self.INPUT(self.NEWEST_GAME_INPUT_TEXT)
                if self.NEWEST_GAME_INPUT == "1":
                    self.WII_SELECT.play()
                    self.NEWEST_GAME_PURCHASE_TEXT = self.LIGHTRED + "Please enter your purchase code to continue (Don't have one? Head to the help section in the menu for information.): "
                    self.NEWEST_GAME_PURCHASE = self.INPUT(self.NEWEST_GAME_PURCHASE_TEXT)
                    if self.NEWEST_GAME_PURCHASE == "PRIME-DEV-SP3":
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_SUCCESS = self.GOLD + "SUCCESFULLY PURCHASED GAME!"
                        self.PRINT(self.NEWEST_GAME_SUCCESS)
                        self.WAIT(1)
                        self.NEWEST_GAME_SUCCESS_INSTRUCTION = self.LIGHTGREEN + "Play Now! [https://scratch.mit.edu/projects/567730620]"
                        self.PRINT(self.NEWEST_GAME_SUCCESS_INSTRUCTION)
                    else:
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_FAILED_TEXT = self.LIGHTRED + "Invalid purchase code. You're either typing it wrong, or your current purchase code has expired. For more help, go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_FAILED_TEXT)

                if self.NEWEST_GAME_INPUT == "2":
                    self.welcome()
                    break

            if self.SHOP_INPUT == "prime's flappy bird" or self.SHOP_INPUT == "flappy bird":
                self.WII_SELECT.play()
                self.NEWEST_GAME_INPUT = self.GOLD + "Prime's Flappy Bird | Wii Shop"
                self.PRINT(self.NEWEST_GAME_INPUT)
                self.NEWEST_GAME_INPUT_TEXT = self.YELLOW + "1. Purchase | " + self.LIGHTRED + "2. Go Back "
                self.NEWEST_GAME_INPUT = self.INPUT(self.NEWEST_GAME_INPUT_TEXT)
                if self.NEWEST_GAME_INPUT == "1":
                    self.WII_SELECT.play()
                    self.NEWEST_GAME_PURCHASE_TEXT = self.LIGHTRED + "Please enter your purchase code to continue (Don't have one? Head to the help section in the menu for information.): "
                    self.NEWEST_GAME_PURCHASE = self.INPUT(self.NEWEST_GAME_PURCHASE_TEXT)
                    if self.NEWEST_GAME_PURCHASE == "jD7-3jf-84J":
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_SUCCESS = self.GOLD + "SUCCESFULLY PURCHASED GAME!"
                        self.PRINT(self.NEWEST_GAME_SUCCESS)
                        self.WAIT(1)
                        self.NEWEST_GAME_SUCCESS_INSTRUCTION = self.LIGHTGREEN + "Contact PrimeDev#2349 through Discord to download the game. For more information, please go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_SUCCESS_INSTRUCTION)
                    else:
                        self.WII_NOTIFICATION.play()
                        self.NEWEST_GAME_FAILED_TEXT = self.LIGHTRED + "Invalid purchase code. You're either typing it wrong, or your current purchase code has expired. For more help, go to the help section in the menu."
                        self.PRINT(self.NEWEST_GAME_FAILED_TEXT)

                if self.NEWEST_GAME_INPUT == "2":
                    self.welcome()
                    break
            if self.SHOP_INPUT == "n" or self.SHOP_INPUT == "exit":
                self.welcome()
                break
                

    def welcome(self):
        self.MENU_TEXT = self.NONE
        while self.MENU_TEXT != "PLACEHOLDER":
            self.MENU = self.LIGHTRED + "1. Wii Shop | " + self.LIGHTMAGENTA + "2. PrimeDev Studios | " + self.GOLD + "3. Information | " + self.LIGHTRED + "4. Wii News/Updates | " + self.LIGHTBLACK + "5. COMING SOON!"
            self.PRINT(self.MENU)
            self.MENU_TEXT = self.LIGHTRED + "Welcome to Wii Menu! " + self.LIGHTMAGENTA + "Select where you'd like to go. "
            self.WELCOME_INPUT = self.INPUT(self.MENU_TEXT)
            if self.WELCOME_INPUT == "shop" or self.WELCOME_INPUT == "wii shop" or self.WELCOME_INPUT == "1":
                self.WII_SELECT.play()
                self.WII_SHOP()
                break
            if self.WELCOME_INPUT == "primedev studios" or self.WELCOME_INPUT == "primedev" or self.WELCOME_INPUT == "2":
                self.WII_SELECT.play()
                self.PRINT(self.GOLD + "PrimeDev Studios is a place where games created by PrimeDev#2349 are created. New games come out very quickly and I hope my games bring joy and laughs to everyone.")
            if self.WELCOME_INPUT == "information" or self.WELCOME_INPUT == "info" or self.WELCOME_INPUT == "3":
                self.WII_SELECT.play()
                self.PRINT(self.LIGHTRED + "| Information |")
                self.PRINT(self.GOLD + "1. Purchase Codes")
                self.PRINT(self.GOLD + "2. Contact to download")
                self.PRINT(self.GOLD + "3. Invalid purchase code")
                self.INFO_INPUT = self.INPUT(self.LIGHTRED + "Select number. ")
                if self.INFO_INPUT == "1":
                    self.WII_SELECT.play()
                    self.PRINT(self.GOLD + "Purchase codes are used to purchase games in the Wii Shop. When Purchasing a game, it will always ask you for a purchase code. This is due to PrimeDev giving out codes for his games on Discord.")
                if self.INFO_INPUT == "2":
                    self.WII_SELECT.play()
                    self.PRINT(self.GOLD + "If you succesfully purchased a game with your purchase code, on your games type of status on the Wii Shop (EXAMPLE: PLAY NOW or CONTACT TO PLAY), that means what will happen when you purchase the game, if the game type is CONTACT TO PLAY, you will need to contact PrimeDev#2349 to play the game on purchased. This is to prevent other people from purchasing the game and sharing the game with other people for further distribution.")
                if self.INFO_INPUT == "3":
                    self.WII_SELECT.play()
                    self.PRINT(self.GOLD + "When attempting to purchase a game using your purchase code, entering a wrong code will tell you " + self.RED + "Invalid Code." + self.GOLD + " This happens either because you're typing your purchase code wrong, or it is because it has expired. When typing a purchase code, make sure your typing it with correct CAPS. For example, if your code is h2D-JK3-G7T, you must type it with the correct CAPS, as of the first part of the code, h2D, you must type it with capital letter D. not h2d. Make sure to include the '-' in codes or it will also not work correctly. In addition, if you're typing it correctly with CAPS and how it was just explained to you, then your code expired. Therefore, this is the meaning behind invalid codes.")
    def __init__(self):
        self.NONE = ""
        self.RED = Fore.RED
        self.BLUE = Fore.BLUE
        self.GREEN = Fore.GREEN
        self.BLACK = Fore.BLACK
        self.YELLOW = Fore.YELLOW
        self.MAGENTA = Fore.MAGENTA
        self.CYAN = Fore.CYAN
        self.GOLD = Fore.LIGHTYELLOW_EX
        self.LIGHTWHITE = Fore.LIGHTWHITE_EX
        self.LIGHTRED = Fore.LIGHTRED_EX
        self.LIGHTBLACK = Fore.LIGHTBLACK_EX
        self.LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX
        self.LIGHTBLUE = Fore.LIGHTBLUE_EX
        self.LIGHTGREEN = Fore.LIGHTGREEN_EX
        self.WHITE = Fore.WHITE
        self.WAIT = time.sleep
        self.PRINT = print
        self.INPUT = input
        self.MUSIC_PLAY = True
        self.WII_MENU_MUSIC = pygame.mixer.Sound("Wii_Config/wii_shop_music.wav")
        self.WII_NOTIFICATION = pygame.mixer.Sound("Wii_Config/wii_message.wav")
        self.WII_SELECT = pygame.mixer.Sound("Wii_Config/select.wav")
        self.WII_DECISION = pygame.mixer.Sound("Wii_Config/decision.wav")
        self.WII_MENU_MUSIC.play()
        self.welcome()

v1 = game()
