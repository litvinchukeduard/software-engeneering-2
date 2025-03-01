from pathlib import Path
'''
Нам потрібно перебрати усі файли у папці та підпапках та вивести зайві файли або зайві папки
'''

unwanted_files = ['.DS_Store']
unwanted_folders = ['__pycache__']

def print_unwanted(folder: str):
    p = Path(folder)
    for element in p.iterdir():
        if element.is_dir():
            if element.name in unwanted_folders:
                print(element)
            print_unwanted(element)
        elif element.name in unwanted_files:
            print(element)

print_unwanted('.')

