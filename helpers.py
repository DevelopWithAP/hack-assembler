import re
import SymbolTable
from sys import argv


symbols = {
    'SP': '0', 
    'LCL': '1',
    'ARG': '2', 
    'THIS': '3', 
    'THAT': '4', 
    'SCREEN': '16384', 
    'KBD': '24576',
    'R0': '0', 
    'R1': '1',
    'R2': '2', 
    'R3': '3', 
    'R4': '4', 
    'R5': '5', 
    'R6': '6', 
    'R7': '7', 
    'R8': '8', 
    'R9': '9', 
    'R10': '10', 
    'R11': '11', 
    'R12': '12', 
    'R13': '13', 
    'R14': '14', 
    'R15': '15' 
}



def open_file (testfile) :
    with open(testfile) as asm_file :
        commands = asm_file.readlines()
    return commands


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



def first_pass() :
    command_list = open_file(testfile)
    commands = extract_commands(command_list)
    line_count = 0
    assembly_labels = {}
    for line in command_list :
        line_count += 1
        if line.isspace() != False :
            pass
            line_count -= 1
        if line.startswith("(") :
            line_count -= 1
            label = re.findall("[A-Z]", line)
            label_name = ''. join(map(str, label))
            line_name = str(line_count)
            assembly_labels.update({label_name: line_name}) 
            symbol_table = dict(symbols, **assembly_labels)
    return (symbol_table)
# second pass - equivalent to main() ?

# def second_pass():
# # #     set n = 16
# # #     scan program
# # #     for each instruction :
# # #         if (symbol -> value) found :
# # #             complete translation
# # #         if (symbol -> value) not found :
# # #             add symbol at n to symbol table
# # #             n++
        
#     symbol_table = first_pass()
#     # for key, value in symbol_table.items():
#         # print(key + " -> " + value)

#     command_list = open_file(testfile)
#     commands = extract_commands(command_list)
#     # print(commands)
#     # print(command_list)
#     # initialise variable count
#     # variable_count = 16

#     # scan program
#     for line in command_list:
#         # print(line)
#         if line.startswith("@"):
#             # isolates instruction
#             instruction = re.split(r"@", line)
#             # print("Not part of the program: " + instruction[1])
#             # ignore inline comments
#             raw_instruction = re.split(r"//", instruction[1])

#             # stores the result  
#             result = str(raw_instruction[0])
#             print(result)
            
            
testfile = "/Users/Apostolis/Desktop/test3.asm"
print(first_pass())







      







    
      


    






    

   
                   
    

    
    
        

      

        


        

        
    
        

        








    

    











    
