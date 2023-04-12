############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    
    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
    

    def __repr__(self):
        return f'MelonType({self.name}, {self.code}, {self.first_harvest}, {self.color}, {self.is_seedless}, {self.is_bestseller})'        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    muskmelon.add_pairing(["mint"])
    casaba.add_pairing(["mint", "strawberries"])
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing(['prosciutto'])
    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Loop over each melon in the list and print its information.
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
    

def make_melon_type_lookup(melon_types):
    """Takes a list of Melon_Types and returns a dictionary of melon type by code."""
    melons = {}
    for melon in melon_types:
        melons[melon.code] = melon
        print(melon.code, melon)

    return melons


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(
        self, type, shape_rating, color_rating, harvested_from, harvested_by
    ):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    # shape and color ratings are greater than 5, and it didn’t come from field 3
    def is_sellable(self):
        if self.color_rating > 5 and self.shape_rating and self.harvested_from != 3:
            return True
        return False
    

def make_melons(melon_types, melons_list=None):
    """Returns a list of Melon objects."""
    all_melon_types = []
    
    if melons_list != None:
        #[sr, cr, code, harvest_by, field_num])
        for list in melons_list:
            all_melon_types.append(Melon(melon_types[list[2]], list[0], list[1], list[4], list[3]))

    melon1 = Melon(melon_types["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melon_types["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melon_types["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melon_types["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melon_types["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melon_types["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melon_types["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melon_types["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melon_types["yw"], 7, 10, 3, "Sheila")

    all_melon_types.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])
    
    return all_melon_types


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        sellable = "CAN BE SOLD" if melon.is_sellable() else "NOT SELLABLE"
        print (f"Harvested by {melon.harvested_by} from Filed {melon.harvested_from}: {sellable}")

def tokenize(filename):
    data = open(filename)
    lst = []
    for line in data:
        [_, sr, _, cr, _, code, _, _, harvest_by, _, _, field_num] = line.split()
        lst.append([int(sr), int(cr), code, harvest_by, int(field_num)])

    return lst


melon_types = make_melon_types()
lookup = make_melon_type_lookup(melon_types)
# melon = make_melons(lookup)
# get_sellability_report(melon)

harvest = tokenize('harvest_log.txt')
melon2 = make_melons(lookup, harvest)
get_sellability_report(melon2)