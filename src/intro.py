import colorama, random, sys

def intro():
    banner = '''
/$$      /$$                     /$$                           
| $$$    /$$$                    | $$                           
| $$$$  /$$$$  /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$  /$$    /$$
| $$ $$/$$ $$ |____  $$ /$$_____/| $$__  $$ /$$__  $$|  $$  /$$/
| $$  $$$| $$  /$$$$$$$|  $$$$$$ | $$  \ $$| $$  \ $$ \  $$/$$/ 
| $$\  $ | $$ /$$__  $$ \____  $$| $$  | $$| $$  | $$  \  $$$/  
| $$ \/  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$|  $$$$$$/   \  $/   
|__/     |__/ \_______/|_______/ |__/  |__/ \______/     \_/    

'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]
    

    return ''.join(colored_chars)