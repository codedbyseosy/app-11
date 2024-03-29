import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str}) # dtype loads all the values in the id col as strings
df_cards = pandas.read_csv("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-11/cards.csv",
                            dtype=str).to_dict(orient="records")# dtype loads all the cols as strings
df_sec_cards = pandas.read_csv("/Users/eseoseodion/Documents/Python 2023/Visual Code/UDEMY_PROJECTS/app-11/card_security.csv",
                            dtype=str) # dtype loads all the cols as strings

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id # 'self.hotel_id' is a property and 'hotel_id' is an instance variable
        self.name =  df.loc[df["id"] == self.hotel_id, "name"].squeeze() # get corresponding name for each id

    def book(self): 
        """This method books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = 'no' # change field from 'yes' to 'no'
        df.to_csv("hotels.csv", index=False) # overwrite the current csv file with the new changes

    def available(self): 
        """This method checks if the hotel is available"""
        availabilty = df.loc[df["id"] == self.hotel_id, "available"].squeeze() # return the 'available' field that corresponds to the entered 'id' field
        if availabilty == "yes":
            return True
        else:
            return False
    

class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name # 'self.customer_name' is a property and 'customer_name' is an instance variable
        self.hotel = hotel_object # 'self.hotel' is a property and 'hotel_object' is an instance variable

    def generate(self): # 'generate' method
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
"""
        return content
    


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        """This method validates the authencity of the card"""
        
        card_data = {"number": self.number, "expiration": expiration, 
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False
        

class SecureCreditCard(CreditCard): # inheritance
    def authenticate(self, given_password):
        password = df_sec_cards.loc[df_sec_cards["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else: 
            return False

        

print("Hi there! Please see the list of our hotels and their availbility status below")
print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID) # create an instance of the object/class 'Hotel'

if hotel.available(): # calling the 'available' method, if hotel.available returns 'True'
    credit_card = SecureCreditCard(number="1234567890123456") # 'number' was part of the 'CreditCard()' class but it was inherited by 'SecureCreditCard()'
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book() # calling the 'book' method
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel) # create an instance of the object/class 'ReservationTicket'
            print(reservation_ticket.generate()) # calling the 'generate' method
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with our payment")
else:
    print("Hotel is not available")