# Tyler Laudenslager
# CSC 402 Data Structures 2
# Spring 2021



def parse(command):
    """ Creates a command dictionary from a command given
        by the user defined by the rules in help_command_menu()
        function

        Example : $ Name : Char ; Type : Fire $

        Where the symbol $ is arbitrary, however

        The first character has to exactly match the last

        Input : command -> string

        Return : command_dictionary -> dict(command:value)
    """

    if command == "" :
        raise ValueError
    
    zero_char_command = command[0]
    last_char_command = command[-1]
    
    if zero_char_command != last_char_command :
         raise ValueError

    command_list = command[1:-2]

    elements_command = command_list.split(sep=";")

    command_pairs = list()

    for command in elements_command:

        if len(command.split()) == 3 and ":" == command.split()[1]:
            command_pairs.append(("".join(command.strip().split(sep=":")).split()))
        else:
            raise ValueError
        
    command_dict = { attribute:value for attribute, value in command_pairs }

    return command_dict



if __name__ == "__main__":

  #testing program not included when importing the module into another program
  try:
    command_dict = parse(input("Enter Command: "))
    if "Name" in command_dict:
        print("Looking for pokemon named", command_dict["Name"])

    if "Type" in command_dict:
        print("Whos type is", command_dict["Type"])

    else:
        pass


    print(*command_dict.items())
        



  except ValueError:
    print("Something Went wrong")
