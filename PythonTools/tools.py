import requests



RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
RESET = '\033[0m'

# Example usage
""" print(RED + "This text Is red." + RESET)
print(GREEN + "This text Is green." + RESET)
print(BLUE + "This text Is blue." + RESET) """


def GetData(url, cookieKey):
    # Your session cookie obtained from the browser
    cookie = {'session': cookieKey}
# Perform a GET request with the session cookie
    response = requests.get(url, cookies=cookie)
# Check if the request was successful
    if response.status_code == 200:
        data = response.text
    
        return data
    else:
        print("Failed to retrieve data:", response.status_code)
        return None  # Return None or raise an exception as appropriate


def PrintList(ListName, Colour, ListTitle):
    """
    Prints each element of the list with the specified color and prints the list title at the end.
    """
    for line in ListName:
        print(f'{Colour}{line}{RESET}')
    print(f'{Colour}Length of {ListTitle}: {len(ListName)}{RESET}')





# import os

# for years in range(2015, 2025):
#     year_dir = f'AoC_{years}'
#     os.makedirs(year_dir, exist_ok=True)
#     for days in range(1,26):
#         day_dir = os.path.join(year_dir, f'{years}_Day_{days}')
#         os.makedirs(day_dir, exist_ok=True)
#         with open(os.path.join(day_dir, 'main.py'), 'w') as main_file:
#             main_file.write('''# This is Day {}
# with open('data.txt', 'r') as file:
#     data = file.read()
# \n'''.format(days))
#         open(os.path.join(day_dir, 'mission.txt'), 'w').close()
#         open(os.path.join(day_dir, 'data.txt'), 'w').close()