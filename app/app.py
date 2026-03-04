from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

now = datetime.now()

print(Fore.GREEN + "Current local time:")
print(Fore.YELLOW + now.strftime("%Y-%m-%d %H:%M:%S"))