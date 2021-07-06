#Tyler Laudenslager
#4/25/2021
#CSC 402 Data Structures 2
#Spring 2021


class Help(Exception):
    """ Help Error Class
        Custom Exeception to raise
        when user needs help
    """
    pass

class Types(Exception):
    """ Types Error Class
        Custom Exeception to raise
        when user wants to view types
    """
    pass

class History(Exception):
    """ History Error Class
        Custom Exeception to raise
        when user wants to view command
        history
    """
    pass

def filter_by_all(func_list, filt_pokedex):
    """ Recursive Function -------------

        Filter down the pokedex using all
        of the filter_functions defined
        in the func_list returning the
        new pokedex to print back to the user

        Base case is when we run out of filter
        functions to apply
   
    """
    if len(func_list) == 0:
        return filt_pokedex
    new_func = func_list[0]
    pass_func_list = func_list[1:]
    filtered_pokedex = list(filter(new_func, filt_pokedex))
    return filter_by_all(pass_func_list, filtered_pokedex)


#factory functions - functions that create lambda functions to filter
#                    data out of the pokedex defined by the user

def filter_by_name(substring):
    """ filter by pokemon name """
    return lambda pokemon : substring in pokemon.name

def filter_by_type(type_name):
    """ filter by pokemon type """
    return lambda pokemon : type_name in pokemon.ptype

def filter_by_attack_greater_than(value):
    """ filter by attack greater than a value """
    return lambda pokemon : pokemon.attack > value

def filter_by_attack_less_than(value):
    """ filter by attack less than a value """
    return lambda pokemon : pokemon.attack < value

def filter_by_defense_greater_than(value):
    """ filter by defense greater than a value """
    return lambda pokemon : pokemon.defense > value

def filter_by_defense_less_than(value):
    """ filter by defense less than a value """
    return lambda pokemon : pokemon.defense < value

def filter_by_speed_greater_than(value):
    """ filter by speed greater than a value """
    return lambda pokemon : pokemon.speed > value

def filter_by_speed_less_than(value):
    """ filter by speed less than a value """
    return lambda pokemon : pokemon.speed < value

def filter_by_special_attack_greater_than(value):
    """ filter by special attack greater than a value """
    return lambda pokemon : pokemon.sp_atk > value

def filter_by_special_attack_less_than(value):
    """ filter by special attack less than a value """
    return lambda pokemon : pokemon.sp_atk < value

def filter_by_special_defense_greater_than(value):
    """ filter by special defense greater than a value """
    return lambda pokemon : pokemon.sp_def > value

def filter_by_special_defense_less_than(value):
    """ filter by special defense less than a value """
    return lambda pokemon : pokemon.sp_def < value

def filter_by_hp_greater_than(value):
    """ filter by health points greater than a value """
    return lambda pokemon : pokemon.hp > value

def filter_by_hp_less_than(value):
    """ filter by health points less than a value """
    return lambda pokemon : pokemon.hp < value


#shorten the names of the factory functions
#
# [sp]_attribute_filter_(greater | less) <---- consistent form


type_filter = filter_by_type
name_filter = filter_by_name
attack_filter_less = filter_by_attack_less_than
attack_filter_greater = filter_by_attack_greater_than
defense_filter_less = filter_by_defense_less_than
defense_filter_greater = filter_by_defense_greater_than
speed_filter_greater = filter_by_speed_greater_than
speed_filter_less = filter_by_speed_less_than
sp_atk_filter_less = filter_by_special_attack_less_than
sp_atk_filter_greater = filter_by_special_attack_greater_than
sp_def_filter_less = filter_by_special_defense_less_than
sp_def_filter_greater = filter_by_special_defense_greater_than
hp_filter_less = filter_by_hp_less_than
hp_filter_greater = filter_by_hp_greater_than


# define all the commands in a list -> used to identify malformed commands 

command_list = ["Exit","Get","Name", "Type", "Sort", "atk_gtr_than","atk_less_than","def_less_than",
                "def_gtr_than", "hp_less_than","hp_gtr_than","sp_atk_gtr_than", "sp_atk_less_than",
                "sp_def_gtr_than", "sp_def_less_than", "speed_gtr_than", "speed_less_than"]


def get_filters(command_dict):
    """
       produce a list of all the commands the user
       would like to use by searching through
       the keys of the command dictionary and
       return the corresponding function for that
       commmand

       Input : Command Dictionary

        { "Command" : "Value" , ... , "Command" : "Value" }


        Return : [ filter_functions ] -> list of filter functions

        [ filter_function_1, filter_function_2 , ... , filter_function_n ]


    """

    filter_func_list = list()

    try:

        for key in command_dict.keys():
            if key not in command_list:
                raise ValueError
            else:
                continue

        if "Exit" in set(command_dict):
          raise EOFError
        

        if "Get" in set(command_dict):
          if command_dict["Get"] == "Types":
            raise Types

          if command_dict["Get"] == "Help":
            raise Help

          if command_dict["Get"] == "History":
            raise History

          else:
            raise ValueError
            
          
        if "Name" in set(command_dict):
            value = command_dict["Name"]
            if value.isalpha():
              print("Find pokemon named: [", value.title(), "]")
              filter_func_list.append(name_filter(value.title()))
            else:
              raise ValueError

        if "Type" in set(command_dict):
            value = command_dict["Type"]
            if value.isalpha():
              print("Find pokemon of type: [", value.title(), "]")
              filter_func_list.append(type_filter(value.title()))
            else:
              raise ValueError
        if "atk_less_than" in set(command_dict):
            value = command_dict["atk_less_than"]
            print("Find pokemon with attack less than: [",value, "]")
            filter_func_list.append(attack_filter_less(int(value)))
            
        if "atk_gtr_than" in set(command_dict):
            value = command_dict["atk_gtr_than"]
            print("Find pokemon with attack greater than: [", value, "]")
            filter_func_list.append(attack_filter_greater(int(value)))

        if "def_less_than" in set(command_dict):
            value = command_dict["def_less_than"]
            print("Find pokemon with defense less than: [", value, "]")
            filter_func_list.append(defense_filter_less(int(value)))

        if "def_gtr_than" in set(command_dict):
            value = command_dict["def_gtr_than"]
            print("Find pokemon with defense greater than: [", value, "]")
            filter_func_list.append(defense_filter_greater(int(value)))
            
        if "hp_less_than" in set(command_dict):
            value = command_dict["hp_less_than"]
            print("Find pokemon with health points less than: [", value, "]")
            filter_func_list.append(hp_filter_less(int(value)))
            
        if "hp_gtr_than" in set(command_dict):
            value = command_dict["hp_gtr_than"]
            print("Find pokemon with health points greater than: [", value, "]")
            filter_func_list.append(hp_filter_greater(int(value)))

        if "speed_gtr_than" in set(command_dict):
            value = command_dict["speed_gtr_than"]
            print("Find pokemon with speed greater than: [", value, "]")
            filter_func_list.append(speed_filter_greater(int(value)))

        if "speed_less_than" in set(command_dict):
            value = command_dict["speed_less_than"]
            print("Find pokemon with speed less than: [", value, "]")
            filter_func_list.append(speed_filter_less(int(value)))

        if "sp_atk_less_than" in set(command_dict):
            value = command_dict["sp_atk_less_than"]
            print("Find pokemon with special attack less than [", value, "]")
            filter_func_list.append(sp_atk_filter_less(int(value)))

        if "sp_atk_gtr_than" in set(command_dict):
            value = command_dict["sp_atk_gtr_than"]
            print("Find pokemon with special attack greater than [", value, "]")
            filter_func_list.append(sp_atk_filter_greater(int(value)))

        if "sp_def_less_than" in set(command_dict):
            value = command_dict["sp_def_less_than"]
            print("Find pokemon with special defense less than [", value, "]")
            filter_func_list.append(sp_def_filter_less(int(value)))

        if "sp_def_gtr_than" in set(command_dict):
            value = command_dict["sp_def_gtr_than"]
            print("Find pokemon with special defense greater than [", value, "]")
            filter_func_list.append(sp_def_filter_greater(int(value)))
            

            
    except ValueError:
        raise ValueError

    except EOFError:
        raise EOFError
          

    return filter_func_list
