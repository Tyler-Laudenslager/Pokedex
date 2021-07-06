class Pokemon:
    """ Creates pokemon objects
        with the following attributes

        1. name
        2. type
        3. health points
        4. attack points
        5. defense points
        6. special attack points
        7. speical defense points
        8. speed points

        Where the numbers indicate the order
        the attributes should be added when
        creating a pokemon object.

    """
    def __init__(self,name, ptype, hp, attack, defense, sp_atk, sp_def, speed):
        """ Dunder method for initilizing a
            new pokemon object with appropriate attributes

            Example :

            Pokemon("Charmander", "Fire", 120, 76, 56, 45, 87, 100)

            Creates a pokemon called "Charmander" of type "Fire"
            that has different values corresponding to the different
            attributes.
        """
        self.name = name
        self.ptype = ptype
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.sp_atk = int(sp_atk)
        self.sp_def = int(sp_def)
        self.speed = int(speed)

    def __repr__(self):
        """ Dunder method for representation of a pokemon object.

            Allows for consistent printing of all pokemon created
            in a clean concise manner.

        """
        return ("Name: " + self.name + "\n"
                "\t" + " T: " + self.ptype +
                " HP: " + str(self.hp) +
                " A: " + str(self.attack) +
                " D: " + str(self.defense) +
                " SpAtk: " + str(self.sp_atk) +
                " SpDef: " + str(self.sp_def) +
                " Speed: " + str(self.speed) + "\n") 
