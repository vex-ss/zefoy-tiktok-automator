#TikTok Botter
import time
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from os import system, get_terminal_size

init()
system("mode 800")
system("title TikTok Botter -By cwissy#2501 and StanTheMan#0001")

def color(str, color):
    if color.lower() == "green":
        result = f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}{str}{Fore.WHITE}]{Fore.LIGHTGREEN_EX}"

    elif color.lower() == "red":
        result = f"{Fore.WHITE}[{Fore.LIGHTRED_EX}{str}{Fore.WHITE}]{Fore.LIGHTRED_EX}"

    return result

def align(str):
    lines = str.splitlines( )
    greatest = []
    for i in lines:  
        greatest.append(len(i))

    for i in lines:
        length = round(int(greatest[-1])/2)
        print(f"{' '*round(get_terminal_size().columns/2-length)}{i}")

class printing():

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def text():
        text = f"""{Fore.LIGHTBLUE_EX}
 ██████╗██╗    ██╗██╗███████╗███████╗██╗   ██╗
██╔════╝██║    ██║██║██╔════╝██╔════╝╚██╗ ██╔╝
██║     ██║ █╗ ██║██║███████╗███████╗ ╚████╔╝ 
██║     ██║███╗██║██║╚════██║╚════██║  ╚██╔╝  
╚██████╗╚███╔███╔╝██║███████║███████║   ██║   
 ╚═════╝ ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝   ╚═╝   
BY USING THIS BOT, YOU AGREE TO THE TERMS OF SERVICE THAT YOU WILL 
NOT USE ANY COPY OF THIS. 

ANY OTHER USE WITHOUT AUTHORIZATION MAY GET YOU IN PROBLEMS, 
INCLUDING GETTING SUED BY VEX SERVICES-https://discord.gg/y9JCRYWvE4.                                          
                                              
"""
        text = text.replace('▪', f'{Fore.GREEN}▪{Fore.LIGHTBLUE_EX}')
        text = text.replace('•', f'{Fore.GREEN}•{Fore.LIGHTBLUE_EX}')
        text = text.replace('·', f'{Fore.GREEN}·{Fore.LIGHTBLUE_EX}')
        text = text.replace('.', f'{Fore.GREEN}.{Fore.LIGHTBLUE_EX}')
        align(text)

    def info():
        align(f"""{Fore.WHITE}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║                                                                                                                                       ║
║                                                                                                                                       ║
║          {color(">", "green")} Made By: {Fore.LIGHTBLUE_EX}cwissy#2501 and StanTheMan#0001{Fore.WHITE}
║          {color(">", "green")} Discord: {Fore.LIGHTBLUE_EX}https://discord.gg/y9JCRYWvE4{Fore.WHITE}                                              ║
║          {color(">", "green")} Github: {Fore.LIGHTBLUE_EX}https://github.com/cwissyy and https://github.com/VexServices000{Fore.WHITE}                          ║
║          {color(">", "green")} Download Chrome Driver: {Fore.LIGHTBLUE_EX}https://chromedriver.chromium.org/downloads{Fore.WHITE}  ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
""")

    def options():
        align(f"""{Fore.WHITE}
╔═══════════════════════════════╗
║                               ║
║          {color("1", "green")} {Fore.LIGHTBLUE_EX}Start{Fore.WHITE}            ║
║          {color("2", "green")} {Fore.LIGHTBLUE_EX}Info{Fore.WHITE}             ║
║          {color("3", "green")} {Fore.LIGHTBLUE_EX}Options{Fore.WHITE}          ║
║          {color("4", "green")} {Fore.LIGHTBLUE_EX}Clear{Fore.WHITE}            ║
║          {color("5", "green")} {Fore.LIGHTBLUE_EX}Exit{Fore.WHITE}             ║
║                               ║
╚═══════════════════════════════╝
""")

    def botOptions():
        align(f"""{Fore.WHITE}
╔═══════════════════════════════╗
║                               ║
║          {color("1", "green")} {Fore.LIGHTBLUE_EX}Follows{Fore.WHITE}          ║
║          {color("2", "green")} {Fore.LIGHTBLUE_EX}Hearts{Fore.WHITE}           ║
║          {color("3", "green")} {Fore.LIGHTBLUE_EX}Views{Fore.WHITE}            ║
║          {color("4", "green")} {Fore.LIGHTBLUE_EX}Shares{Fore.WHITE}           ║
║          {color("5", "green")} {Fore.LIGHTBLUE_EX}All{Fore.WHITE}              ║
║                               ║
╚═══════════════════════════════╝
""")

    def cooldowns(self):
        align(f"""{Fore.WHITE}
╔═══════════════════════════════╗
║          {color(">", "green")} {Fore.LIGHTBLUE_EX}Cool Downs {color("<", "green")}║
║          {color(">", "green")} {Fore.LIGHTBLUE_EX}Follows: {Fore.LIGHTCYAN_EX}{self.a}s{Fore.WHITE}             ║
║          {color(">", "green")} {Fore.LIGHTBLUE_EX}Hearts: {Fore.LIGHTCYAN_EX}{self.b}s{Fore.WHITE}              ║
║          {color(">", "green")} {Fore.LIGHTBLUE_EX}Views: {Fore.LIGHTCYAN_EX}{self.c}s{Fore.WHITE}               ║
║          {color(">", "green")} {Fore.LIGHTBLUE_EX}Shares: {Fore.LIGHTCYAN_EX}{self.d}s{Fore.WHITE}              ║
║                               ║
╚═══════════════════════════════╝
""")

    def refresh():
        system("cls")
        printing.text()
        align(f"\n\n\t\t\t{color('>', 'green')}Made By: {Fore.LIGHTBLUE_EX}cwissy#2501 and StanTheMan#0001 {color('<', 'green')}")
        align(f"\t\t\t\t{color('>', 'green')} {Fore.LIGHTGREEN_EX}Github: {Fore.LIGHTBLUE_EX} https://github.com/cwissyy {color('<', 'green')}")
        printing.options()

def start(video, botChoice):

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    try:
        service = Service('Enter ur chromedriver path here. It has to include the chromedriver exe file')
        driver = webdriver.Chrome(service=service, options=option)
    except Exception as DriverError:
        print(f"{color('>', 'red')} {Fore.LIGHTRED_EX}Error: {DriverError}")
        input(f"{color('>', 'red')} {Fore.LIGHTRED_EX}Press Enter to Exit")
        exit()

    driver.get("https://zefoy.com")
    
    if driver.title == "zefoy.com | 502: Bad gateway":
            print(f"{color('>', 'red')} Zefoy Is Down... Attempting To Fix.\n")
            while driver.title == "zefoy.com | 502: Bad gateway":
                time.sleep(20)
                driver.refresh()
                if driver.title != "zefoy.com | 502: Bad gateway":
                    print(f"\n{color('>', 'red')} Fixed! Zefoy is Back Up. Starting Now.\n")
                    break
    else:
        print(f"\n{color('>', 'green')} Zefoy Is Up!\n")
    
    captchaCheck = input(f"{color('>>>', 'green')} Type \"y\" Once You Finished The Captcha: {Fore.LIGHTBLUE_EX}")
    captchaFinish = False

    if captchaCheck == "y":
        while captchaFinish != True:
            try:
                driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/h5")
                captchaFinish = True
            except:
                print(f"\n{color('>', 'red')} You Didn't Finish The Captcha.")
                input(f"{color('>>>', 'green')} Type \"y\" Once You Finished The Captcha: {Fore.LIGHTBLUE_EX}")

    #Defining Find Cooldown
    def findCooldown(xpath):
        cooldown = driver.find_element(By.XPATH, xpath).text

        #String Slicing For Minutes
        minute1 = cooldown.find("wait") + 4
        minute2 = minute1
        while True:
            minute2 += 1
            if cooldown[minute2] == "m":
                break

        #String Slicing For Seconds
        second1 = cooldown.find(")") + 1
        second2 = second1
        while True:
            second2 += 1
            if cooldown[second2] == "s":
                break
        
        #Returning Minutes & Second Added
        return (int(cooldown[minute1:minute2])*60) + int(cooldown[second1:second2])

    print(f"\n{color('>', 'green')} Captcha is Finished, Starting...\n")

    #Defining Xpaths
    home = "/html/body/nav/ul/li/a"

    views_enter = "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button"
    views_input = "/html/body/div[4]/div[5]/div/form/div/input"
    views_search = "/html/body/div[4]/div[5]/div/form/div/div/button"
    views_submit = "/html/body/div[4]/div[5]/div/div/div[1]/div/form/button"
    views_cooldowns = "/html/body/div[4]/div[5]/div/div/h4"

    shares_enter = "/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button"
    shares_input = "/html/body/div[4]/div[6]/div/form/div/input"
    shares_search = "/html/body/div[4]/div[6]/div/form/div/div/button"
    shares_submit = "/html/body/div[4]/div[6]/div/div/div[1]/div/form/button"
    shares_cooldowns = "/html/body/div[4]/div[6]/div/div/h4"

    hearts_enter = "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button"
    hearts_input = "/html/body/div[4]/div[3]/div/form/div/input"
    hearts_search = "/html/body/div[4]/div[3]/div/form/div/div/button"
    hearts_submit = "/html/body/div[4]/div[3]/div/div/div[1]/div/form/button"
    hearts_cooldowns = "/html/body/div[4]/div[3]/div/div/h4"

    follows_enter = "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button"
    follows_input = "/html/body/div[4]/div[2]/div/form/div/input"
    follows_search = "/html/body/div[4]/div[2]/div/form/div/div/button"
    follows_submit = "/html/body/div[4]/div[2]/div/div/div[1]/div/form/button"
    follows_cooldowns = "/html/body/div[4]/div[2]/div/div/h4"

    #List of Xpaths for the Bot All
    enterList = [
        [follows_enter, follows_input, follows_search, follows_submit, follows_cooldowns, "Follows"],
        [views_enter, views_input, views_search, views_submit, views_cooldowns, "Views"],
        [hearts_enter, hearts_input, hearts_search, hearts_submit, hearts_cooldowns, "Hearts"],
        [shares_enter, shares_input, shares_search, shares_submit, shares_cooldowns, "Shares"],
    ]

    #Defining Cool-downs
    follows_cooldown = 0
    hearts_cooldown = 0
    views_cooldown = 0
    shares_cooldown = 0

    #Defining Boolean
    continue1 = False
    continue2 = False

    time.sleep(5)

    #Defining Botting Function, Uses XPaths as parameters
    def bot(which, enter, input, search, submit, con1, con2, cooldownText, cooldownTime):
        amount = 0
        while captchaFinish:
            driver.refresh()

            #Checks If Zefoy Down
            if driver.title == "zefoy.com | 502: Bad gateway":
                print(f"{color('>', 'red')} Zefoy Is Down... Attempting To Fix.\n")
                while driver.title == "zefoy.com | 502: Bad gateway":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "zefoy.com | 502: Bad gateway":
                        print(f"\n{color('>', 'red')} Fixed! Zefoy is Back Up. Starting Now.\n")
                        break

            print(f"{color('>', 'green')} Sending {which}...")
            try:
                driver.find_element(By.XPATH, enter).click()
                time.sleep(1)
                driver.find_element(By.XPATH, input).send_keys(video)
                con1 = True
            except:
                con1 = False
                print(f"\n{color('>', 'red')} {which} Page is Down on Zefoy.")
                print(f"{color('>', 'red')} Stopped.")
                time.sleep(1000000)
            if con1 == True:
                time.sleep(2)
                driver.find_element(By.XPATH, search).click()
                time.sleep(3)
                try:
                    driver.find_element(By.XPATH, submit).click()
                    con2 = True
                    print(f"{color('>', 'green')} Sent {which}, Getting Cool Down\n")
                except:
                    con2 = False
                    print(f"{color('>', 'red')} {which} Cool Down Isn't Finished, Getting Cool Down.\n")
                    time.sleep(5)
                    cooldownTime += findCooldown(cooldownText)
                if con2 == True:
                    time.sleep(5)
                    cooldownTime += findCooldown(cooldownText)
                else:
                    pass
            else:
                pass

            amount += 1
            driver.find_element(By.XPATH, home).click()
            print(f"{color('>', 'green')} Completed {Fore.LIGHTCYAN_EX}{amount} {Fore.LIGHTGREEN_EX}Time.")
            print(f"{color('>', 'green')} Cooldown: {Fore.LIGHTCYAN_EX}{cooldownTime}s\n")
            for i in range(10):
                time.sleep(cooldownTime/10)
                driver.refresh()
                print(f"{color('>', 'green')} Cool-Down: {Fore.LIGHTCYAN_EX}{i+1}/10")

            print(f"\n{color('>', 'green')} Finished Cool Down, Restarting...\n")
            time.sleep(5)

    def botAll(boolean):
        amount = 0
        while True:

            #Checks If Zefoy Down
            if driver.title == "zefoy.com | 502: Bad gateway":
                print(f"{color('>', 'red')} Zefoy Is Down... Attempting To Fix.\n")
                while driver.title == "zefoy.com | 502: Bad gateway":
                    time.sleep(20)
                    driver.refresh()
                    if driver.title != "zefoy.com | 502: Bad gateway":
                        print(f"\n{color('>', 'red')} Fixed! Zefoy is Back Up. Starting Now.\n")
                        break

            driver.refresh()
            cooldownList = []
            if boolean:
                for i in enterList:
                    time.sleep(3)
                    print(f"{color('>', 'green')} Sending {i[5]}...")
                    try:
                        driver.find_element(By.XPATH, i[0]).click()
                        time.sleep(1)
                        driver.find_element(By.XPATH, i[1]).send_keys(video)
                        continue1 = True
                    except:
                        print(f"{color('>', 'red')} {i[5]} Page is Down on Zefoy.\n")
                        cooldownList.append(0)
                        continue1 = False
                        driver.find_element(By.XPATH, home)

                    if continue1 == True:
                        time.sleep(2)
                        driver.find_element(By.XPATH, i[2]).click()
                        time.sleep(3)

                        try:
                            driver.find_element(By.XPATH, i[3]).click()
                            continue2 = True
                            print(f"{color('>', 'green')} Sent {i[5]}, Getting Cool Down.\n")
                        except:
                            print(f"{color('>', 'red')} {i[5]} Cool Down Isn't Finished, Getting Cool Down.\n")
                            time.sleep(5)
                            cooldownList.append(findCooldown(i[4]))
                            driver.find_element(By.XPATH, home).click()
                            continue2 = False

                        if continue2 == True:
                            time.sleep(5)
                            cooldownList.append(findCooldown(i[4]))
                            driver.refresh()
                    else:
                        pass
                else:
                    pass
                
                amount +=1
                cooldownList.sort()


                print(f"{color('>', 'green')} Completed {amount} Time.")
                print(f"{color('>', 'green')} Cooldown: {Fore.LIGHTCYAN_EX}{cooldownList[-1]}s\n")

                for i in range(10):
                    time.sleep(cooldownList[-1]/10)
                    driver.refresh()
                    print(f"{color('>', 'green')} Cool-Down: {Fore.LIGHTCYAN_EX}{i+1}/10")

            time.sleep(5)
            print(f"\n{color('>', 'green')} Finished Cool Down, Restarting...\n")
            driver.refresh()

    if botChoice == 1:
        bot("Follows", follows_enter, follows_input, follows_search, follows_submit, continue1, continue2, follows_cooldowns, follows_cooldown)
    elif botChoice == 2:
        bot("Hearts", hearts_enter, hearts_input, hearts_search, hearts_submit, continue1, continue2, hearts_cooldowns, hearts_cooldown)
    elif botChoice == 3:
        bot("Views", views_enter, views_input, views_search, views_submit, continue1, continue2, views_cooldowns, views_cooldown)
    elif botChoice == 4:
        bot("Shares", shares_enter, shares_input, shares_search, shares_submit, continue1, continue2, shares_cooldowns, shares_cooldown)
    elif botChoice == 5:
        botAll(True)

printing.refresh()

while True:
    choice = input(f"{color('>>>', 'green')} Choice: {Fore.LIGHTBLUE_EX}")
    if choice == "1":
        video = input(f"{color('>>>', 'green')} TikTok Video URL: {Fore.LIGHTBLUE_EX}")
        printing.botOptions()
        option = input(f"\n{color('>>>', 'green')} Which to Bot: {Fore.LIGHTBLUE_EX}")
        start(video, int(option))
        break

    elif choice == "2":
        printing.info()
    elif choice == "3":
        printing.options()
    elif choice == "4":
        printing.refresh()
    elif choice =="5":
        exit()