
#Tyler Laudenslager
#CSC 402 Data Structures 2
#Spring 2021


import pokemon as p
import command_parser as cmdp
import pokemon_filter as f
import pokemon_sorter as s
import csv
import sys


def build_pokedex(from_file):
    """Create a pokedex from a CSV (Comma Separated Values) file

       First line in the file gets skipped  

       Name,Type,Strength,Defense,...,Health

       Usually defined as column identifiers for the data below.


       Returns a list of pokemon objects created from the
       corresponding data in the file.

       [pokemon_1,pokemon_2,...,pokemon_n]
       for n = f_lines - 1 where f_lines = total lines in file

    """
       
    new_pokedex = list()
    with open(from_file, newline='') as csvfile:
        f_read = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(f_read):
            if index == 0:
                continue
            new_pokedex.append(p.Pokemon(*row))
    return new_pokedex

def get_types(pokedex):
    """ returns a set of all unique values of the types of
        pokemon available in the pokedex
    """
    return set([x.ptype for x in pokedex])

def splash_screen():
    """ information screen when the program starts
    """
    print("""
Pokemon Pokedex
version 2.3.8
Professor Oak
    """)
    print("Example command : $ Name : Char ; Type : Fire $")
    print()
    print("Command -> $ Get : Help $ for additional commands")
    print()

def invalid_command():
    """ tells user that the command entered is of invalid form
        or meaning
    """
    print()
    print("Invalid Command")
    print("Try Command -> $ Get : Help $")
    print()

def help_command_menu():
    """ A command menu displaying all possible command options available
        for filtering and sorting the pokedex.

    """

    print("""
    Pokedex Command Structure :
             
             $ Command : Value [ ; Command : Value ]* $

             Commands available :
             
                Name : String
                Type : String
                Sort : Sort Values
                Get : Get Values
                atk_less_than : Int
                def_less_than : Int
                sp_atk_less_than : Int
                sp_def_less_than : Int
                hp_less_than : Int
                speed_less_than : Int
                atk_gtr_than : Int
                def_gtr_than : Int
                sp_atk_gtr_than : Int
                sp_def_gtr_than : Int
                hp_gtr_than : Int
                speed_gtr_than : Int

             Sort Values:

                * value -> meaning *
             
                name -> Name
                hp -> Health Points
                def -> Defense Points
                atk -> Attack Points
                type -> Type
                sp_def -> Special Defense
                sp_atk -> Special Attack
                speed -> Speed
                

                descending order put @descend at the end

             Get Values:
             
                Types -> prints all pokemon types
                Help -> provides this menu
                History -> prints the most recent commands

     Example Command -> $ Name : star ; Type : water ; Sort : atk@descend $
            """)


def print_types(pokedex):
    """ prints all the pokemon types that are available in
        the pokedex
    """
       
    print("Type Options")
    print("------------------------", end='')
    for index, poke_type in enumerate(get_types(pokedex)):
        if index % 3 == 0:
            print()
        print(poke_type, end=' ')
    print("\n")

def print_history(command_list):
    """ prints the five most recent commands the user has
        entered ( feature only available in interactive mode)
    """
    print("Recent Commands")
    for command in command_list[-5:][::-1]:
        print(command)
    print()

def execute(command_line, pokedex):
    """ execute one command through the interpreter.

        commands follow the standard rules defined
        in the help_command_menu() function.

        History feature is missing
        Exit feature is missing

        Used in batch mode only
    """
    print("Command : \n", command_line)
    try:
      command_dict = cmdp.parse(command_line)

      print()

      filter_func_list = f.get_filters(command_dict)
      sort_func_list, order = s.get_sorter(command_dict)

      pokedex_filtered = f.filter_by_all(filter_func_list,pokedex)
      
      #if user did not issue command sort dont sort the filtered pokedex
      if len(sort_func_list) != 0:
          #sorts by first sort function in list ignores the rest
          pokedex_sorted = sorted(pokedex_filtered, key=sort_func_list[0], reverse=order)
          print()
          print(*pokedex_sorted, sep="")
      else:
          print()
          print(*pokedex_filtered, sep="")



    except ValueError:
      invalid_command()

    except f.Help:
      help_command_menu()

    except f.Types:
      print_types(pokedex)

    except TypeError:
      invalid_command()

def main():
    """ Builds the Pokedex from mod_pokemon.csv file

        Then starts a loop that will read in commands
        specified by help_command_menu() function

        Depending on the command issued will determine
        the pokemon returned from the pokedex for
        viewing

        loop ends by entering the command below

         "$ Exit : Now $"
    """
    pokedex = build_pokedex('mod_pokemon.csv')


    if len(sys.argv) > 1 :
        print("\nBatch Mode \n----------------------------\n")
        for file in sys.argv[1:]:
            print("File : ", file, "\n")
            try:
              for command in open(file):
                  #skip comments <- skip this in the file
                  if command[0] == "#" or command.strip("\n") == "":
                      continue
                  execute(command.rstrip("\n"), pokedex)
            except FileNotFoundError:
                print("File Not Found --->", file)
                sys.exit()

    else:
        
        splash_screen()

        command_list = list()

        
        
        while True:
            
            try:
              print("$ Exit : Now $ -> Quit")
              command = input("Enter Command: ")
              command_dict = cmdp.parse(command)

              print()

              filter_func_list = f.get_filters(command_dict)
              sort_func_list, order = s.get_sorter(command_dict)

              pokedex_filtered = f.filter_by_all(filter_func_list,pokedex)

              command_list.append(command)
              
              if len(sort_func_list) != 0:
                  pokedex_sorted = sorted(pokedex_filtered, key=sort_func_list[0], reverse=order)
                  print()
                  print(*pokedex_sorted, sep="")
              else:
                  print()
                  print(*pokedex_filtered, sep="")



            except ValueError:
              invalid_command()

            except f.Help:
              help_command_menu()

            except f.Types:
              print_types(pokedex)

            except f.History:
              print_history(command_list)
            
            except EOFError:
              print("logging off...")
              break

            except TypeError:
              invalid_command()
        
if __name__ == "__main__":

   main()
   

