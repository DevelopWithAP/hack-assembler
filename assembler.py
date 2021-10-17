import re
import HashTable
from helpers import first_pass
import sys
from sys import argv


testfile = argv[1]

def main():
    # symbol_table = first_pass()
    command_list = open_file(testfile)
    commands = extract_commands(command_list)
    write_machine_commands(commands)

    
# open asm file for reading

def open_file (testfile) :
    with open (testfile) as asm_file:
        commands = asm_file.readlines()
    return commands


# performs first pass

# def first_pass() :
#     command_list = open_file(filename)
#     commands = extract_commands(command_list)
#     line_count = 0
#     assembly_labels = {}
#     for line in command_list :
#         line_count += 1
#         if line.isspace() != False :
#             pass
#             line_count -= 1
#         if line.startswith("(") :
#             line_count -= 1
#             label = re.findall("[A-Z]", line)
#             label_name = ''. join(map(str, label))
#             line_name = str(line_count)
#             assembly_labels.update({label_name: line_name}) 
#             symbol_table = dict(symbols, **assembly_labels)
#     return (symbol_table)

# ignores comments

def ignore_comments (command_list) :
    for line in command_list :
        if line.startswith('//') :
            line = ""
    return line


# isolates commands

def extract_commands(command_list) :
    commands = []
    for line in command_list :

        # ignores in-line comments
        split_line = re.split(r'//', line)

        # removes extra white spaces
        raw_command = re.sub('\s+', "", split_line[0])
        command = raw_command.strip()
        commands.append(command)
    return commands
 

# determines command types

def identify_command(command) :
    if '=' in command or ';' in command:
        return 'C_type'
    elif command.startswith('@') :
        return 'A_type'


# parses A-instruction

def parse_A_instruction (command) :
    instr = command.split('@')
    instr = int(instr[1])
    return instr



# parses C-instruction

# dest = comp;jump
# case 1: dest = comp;jump
# case 2: dest = comp
# case 3: comp;jump

def parse_C_instruction (command) :
    command_fields = {'comp': '', 'dest': '', 'jump': ''}
   
    # case 2: dest = comp
    if '=' in command and ';' not in command :

        split_2 = re.split(r'=', command)
        command_fields['dest'] = split_2[0]
        command_fields['comp'] = split_2[1]
        command_fields['jump'] = 'null'

    # case 1: dest = comp ; jump
    if '=' in command and ';' in command :

        split_1 = re.split(r'[=;]', command)
        command_fields['dest'] = split_1[0]
        command_fields['comp'] = split_1[1]
        command_fields['jump'] = split_1[2]

    # case 3: comp ; jump
    if '=' not in command:
        split_3 = re.split(r';', command)
        command_fields['dest'] = 'null'
        command_fields['comp'] = split_3[0]
        command_fields['jump'] = split_3[1]  
          
    return get_C_bin(command_fields['comp'], command_fields['dest'], command_fields['jump']) 
    

# gets A-instruction in binary

def get_A_bin(command) :
    code = bin(parse_A_instruction(command))
    code = code[2:].zfill(16)
    return str(code)
    

# gets C-instruction in binary

def get_C_bin(comp, dest, jump) :
    dest_bin = HashTable.dest[dest]
    comp_bin = HashTable.comp[comp]
    jump_bin = HashTable.jump[jump]

    return ('111' + comp_bin + dest_bin + jump_bin)



# assembles machine commands

def write_machine_commands(commands) :
    machine_commands = []
    for command in commands :
        command_type = identify_command(command)
        if command_type == 'A_type' :
            machine_commands.append(get_A_bin(command))
        elif command_type == 'C_type' :
            machine_commands.append(parse_C_instruction(command))
            
    # returns machine_commands
    with open ('output.hack', 'w') as hackfile :
        sys.stdout = hackfile
        for item in machine_commands:
            print (item)
   
        
# Driver function

if __name__ == "__main__" :
    main()
        








