import os

# Define the ASCII art text for the logo
logo = """
██████╗░████████╗██╗░░██╗
██╔══██╗╚══██╔══╝██║░██╔╝
██████╔╝░░░██║░░░█████═╝░
██╔══██╗░░░██║░░░██╔═██╗░
██║░░██║░░░██║░░░██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print(logo)  # Print the logo
    print('1. Cookies Remove')
    print('2. Number Remove')
    print('3. Middle Line Remove')
    print('4. Line Cutter')  
    print('5. Search and Extract Lines by Keyword')
    print('6. Exit')
    choice = input('>> ')
    if choice == '1':
        file_path = input('Input File Path > ')
        process_file(rc, file_path)
    elif choice == '2':
        file_path = input('Input File Path > ')
        process_file(rn, file_path)
    elif choice == '3':
        file_path = input('Input File Path > ')
        process_file(remove_middle_line, file_path)
    elif choice == '4':
        file_path = input('Input File Path > ')
        combine_every_two_lines(file_path)  # Call the line cutter function
    elif choice == '5':
        input_file = input("Enter the input file path: ")
        keyword = input("Enter the keyword or phrase to search for: ")
        extract_lines_with_keyword(input_file, keyword)
    elif choice == '6':
        exit()
    else:
        menu()

def process_file(callback, file_path):
    try:
        with open(file_path, 'r') as file:
            all_id = file.read().splitlines()
    except FileNotFoundError:
        exit('File Not Valid')

    output_lines = []
    for id_line in all_id:
        result = callback(id_line)
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

def remove_middle_line(id_line):
    try:
        parts = id_line.split('|')
        if len(parts) > 2:
            return f"{parts[0]}|{parts[-1]}"
        else:
            return id_line
    except ValueError:
        return id_line

def combine_every_two_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        exit('File Not Valid')

    formatted_lines = []
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            combined_line = lines[i].strip() + '|' + lines[i + 1].strip()
            formatted_lines.append(combined_line)

    with open(file_path, 'w') as file:
        file.write('\n'.join(formatted_lines))

def extract_lines_with_keyword(input_file, keyword):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        matching_lines = [line for line in lines if keyword in line]

        output_file = 'extracted_lines.txt'
        with open(output_file, 'w') as outfile:
            for line in matching_lines:
                outfile.write(line)

        print(f"Lines containing '{keyword}' extracted to {output_file}")
    except FileNotFoundError:
        print("Input file not found.")

if __name__ == '__main__':
    while True:
        menu()
        choice = input('Do you want to continue? (y/n) ')
        if choice.lower() != 'y':
            break
