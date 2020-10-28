
class Property:
    def __init__(self, square_feet = '', beds = '', baths = '', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_beds = beds
        self.num_baths = baths

    def display(self):
        print('\nProperty Details')
        print('Square Feet: {}'.format(self.square_feet))
        print('Number of Beds: {}'.format(self.num_beds))
        print('Number of Baths: {}'.format(self.num_baths))

    def prompt_init():
        return dict(square_feet = input('Enter square feet: '),
            beds = input('Enter number of beds: '),
            baths = input('Enter number of baths: ')
            )

    prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string, valid_options):
    input_string += "{} \n".format(', '.join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('Apartment Details')
        print('Balcony: {}'.format(self.balcony))
        print('Laundry: {}'.format(self.laundry))


    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input('Laundry facilities: '
        , Apartment.valid_laundries)
        balcony = get_valid_input('Have a balcony: '
        , Apartment.valid_balconies)
        parent_init.update({
            'balcony': balcony,
            'laundry': laundry
        })
        return parent_init
 
    prompt_init = staticmethod(prompt_init)

class Purchase(Property):
    def __init__(self, price = '', taxes = '', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print('Purchase Details')
        print('Price: {}'.format(self.price))
        print('Taxes: {}'.format(self.taxes))

    def prompt_init():
        return dict(
            price = input('Enter price: '),
            taxes = input('Enter taxes: ')
            )

    prompt_init = staticmethod(prompt_init)

class Rental(Property):
    def __init__(self, furnished = '', rent = '', utilities = '', **kwargs):
        super().__init__(**kwargs)
        self.rent = rent
        self.furnished = furnished
        self.utilities = utilities

    def display(self):
        super().display()
        print('Rental Details')
        print('Furnished: {}'.format(self.furnished))
        print('Rent: {}'.format(self.rent))
        print('Utilities: {}'.format(self.utilities))

    def prompt_init():
        return dict(
            rent = input('Enter rent: '),
            utilities = input('Enter utilities: '),
            furnished = get_valid_input('Furnished: ', ('yes', 'no'))
            )

    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Apartment, Purchase):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Apartment, Rental):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class Agent:
    type_map = {
        'purchase': ApartmentPurchase,
        'rental': ApartmentRental
    }
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        payment_type = get_valid_input('Payment Type: ', ('purchase', 'rental')).lower()
        PropertyClass = self.type_map[payment_type]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

    
if __name__ == '__main__':
    agent = Agent()
    agent.add_property()
    agent.display_properties()