#Tyler Laudenslager
#CSC 402 Data Structures
#Spring 2021



#lambda functions for sorting by all attributes
sort_by_hp = lambda pokemon : pokemon.hp
sort_by_type = lambda pokemon : pokemon.ptype
sort_by_attack = lambda pokemon : pokemon.attack
sort_by_def = lambda pokemon : pokemon.defense
sort_by_sp_atk = lambda pokemon : pokemon.sp_atk
sort_by_sp_def = lambda pokemon : pokemon.sp_def
sort_by_speed = lambda pokemon : pokemon.speed
sort_by_name = lambda pokemon : pokemon.name



def get_sorter(command_dict):
    """ Finds out if the user has requested to
        sort by anything if so we add the function
        to the list

        Input : Command Dictionary

        { "Command" : "Value" , ... , "Command" : "Value" }


        Return : tuple(list with sorting functions, bool_value)

        [ sort_function_1, sort_function_2 , ... , sort_function_n ]

        Also returns if the user would like the sort ascending or descending
        using a boolean value

        
    """

    sorter_func_list = list()
    ascending = False

    if "Sort" in command_dict:
        sort_by = command_dict["Sort"].split(sep="@")
        sort_value = sort_by[0].lower()
        if sort_value == "hp" :
            print("Sorting pokemon by : [ Health ]")
            sorter_func_list.append(sort_by_hp)
        if sort_value == "atk" :
            print("Sorting pokemon by : [ Attack ]")
            sorter_func_list.append(sort_by_attack)
        if sort_value == "def" :
            print("Sorting pokemon by : [ Defense ]")
            sorter_func_list.append(sort_by_def)

        if sort_value == "sp_def" :
            print("Sorting pokemon by : [ Special Defense ]")
            sorter_func_list.append(sort_by_sp_def)

        if sort_value == "sp_atk" :
            print("Sorting pokemon by : [ Special Attack ]")
            sorter_func_list.append(sort_by_sp_atk)

        if sort_value == "speed" :
            print("Sorting pokemon by : [ Speed ]")
            sorter_func_list.append(sort_by_speed)
            
        if sort_value == "name" :
            print("Sorting pokemon by : [ Name ]")
            sorter_func_list.append(sort_by_name)
            
        if sort_value == "type" :
            print("Sorting pokemon by : [ Type ]")
            sorter_func_list.append(sort_by_type)

        if len(sort_by) == 2 :

            if sort_by[1].lower() == "descend" :
                print("Decending Order : [ True ]")
                ascending = True

        return sorter_func_list, ascending

    else:
        return list(), ascending
