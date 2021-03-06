class Property:
    """
    Represents property.
    """
    def __init__(self, name="", square_feet='', beds='',
                 baths='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Print property info on the screen.
        :return: None
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))

    def prompt_init():
        """
        Request user to enter property info.
        :return: user input
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Request user to input data and checks whether it is correct.
    :param input_string: string, displayed in the input request
    :param valid_options: allowed input
    :return: user input
    """
    input_string += " ({}) ".format((", ".join(valid_options)))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class House(Property):
    """
    Represents house.
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Print house info on the screen.
        :return: None
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Request user to enter house info.
        :return: user input
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Represents apartment.
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Print apartment info on the screen.
        :return: None
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        """
        Request user to enter apartment info.
        :return: user input
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
                "What laundry facilities does "
                "the property have? ",
                Apartment.valid_laundries)
        balcony = get_valid_input(
                "Does the property have a balcony?",
                Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Represents rental.
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Print rental info on the screen.
        :return: None
        """
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Request user to enter rental info.
        :return: user input
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Represents purchase.
    """
    def __init__(self, price='', taxes='', **kwargs):
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Print purchase info on the screen.
        :return: None
        """
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Request user to enter purchase info.
        :return: user input
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class HouseRental(House):
    """
    Represents house for rental.
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        Rental.__init__(self, furnished, utilities, rent)

    def display(self):
        super().display()
        Rental.display(self)

    def prompt_init():
        """
        Request user to enter house rental info.
        :return: user input
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(House):
    """
    Represents house for purchase.
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        Purchase.__init__(self, price, taxes)

    def display(self):
        super().display()
        Purchase.display(self)

    def prompt_init():
        """
        Request user to enter house purchase info.
        :return: user input
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Apartment):
    """
    Represents apartment for rental.
    """
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        super().__init__(**kwargs)
        Rental.__init__(self, furnished, utilities, rent)

    def display(self):
        super().display()
        Rental.display(self)

    def prompt_init():
        """
        Request user to enter apartment rental info.
        :return: user input
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Apartment):
    """
    Represents apartment for purchase.
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        Purchase.__init__(self, price, taxes)

    def display(self):
        super().display()
        Purchase.display(self)

    def prompt_init():
        """
        Request user to enter apartment purchase info.
        :return: user input
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Represents agent.
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        """
        Print all properties info on the screen.
        :return: None
        """
        for property in self.property_list:
            property.display()

    def find_properties_by_key(self, key, value, percentage=0.25):
        """
        Find all properties, which key match to value.
        :param key: keyword
        :param value: value of keyword
        :param percentage: +- percentage of value
        :return: list of properties
        """
        properties = []
        for property in self.property_list:
            if value.isalpha() and eval("property." + key) == value:
                properties.append(property)
            elif int(eval("property." + key)) >= int(value) * (1 - float(percentage)) and\
               int(eval("property." + key)) <= int(value) * (1 + float(percentage)):
                properties.append(property)
        return properties

    def add_property(self):
        """
        Create and add new property to all properties.
        :return: None
        """
        property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()
        payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()

        property_class = self.type_map[(property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.property_list.append(property_class(**init_args))

    def remove_properties_by_key(self, key, value, percentage):
        """
        Remove all properties, which key match to value.
        :param key: keyword
        :param value: value of keyword
        :param percentage: +- percentage of value
        :return: None
        """
        for property in self.find_properties_by_key(key, value, percentage):
            self.property_list.remove(property)

    def display_properties_by_key(self, key, value, percentage=0):
        """
        Find and print all properties, which key match to value.
        :param key: keyword
        :param value: value of keyword
        :param percentage: +- percentage of value
        :return: None
        """
        for property in self.find_properties_by_key(key, value, percentage=percentage):
            property.display()
