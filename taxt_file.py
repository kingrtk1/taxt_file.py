import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print('1. Cookies Remove')
    print('2. Number Remove')
    choice = input('>> ')
    if choice == '1':
        process_file(rc)
    elif choice == '2':
        process_file(rn)
    else:
        menu()

def process_file(callback):
    clear_screen()
    file_path = input('Input File Path > ')
    try:
        with open(file_path, 'r') as file:
            all_id = file.read().splitlines()
    except FileNotFoundError:
        exit('File Not Valid')

    output_lines = []
    for id in all_id:
        result = callback(id)
        if result:
            output_lines.append(result)

    with open(file_path, 'w') as file:
        file.write('\n'.join(output_lines))

def rc(id_line):
    try:
        uid, password, cookie = id_line.split('|')
        return f"{uid}|{password}"
    except ValueError:
        return id_line

def rn(id_line):
    try:
        count = len(id_line.split('|'))
        if count == 4:
            number, uid, password, cookie = id_line.split('|')
            return f"{uid}|{password}|{cookie}"
        elif count == 3:
            number, uid, password = id_line.split('|')
            return f"{uid}|{password}"
    except ValueError:
        return id_line

if __name__ == '__main__':
    menu()
