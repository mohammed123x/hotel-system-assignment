
class Guest:
    def __init__(self, name, email, phone_number, address):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__reservation = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_reservation(self):
        return self.__reservation

    def set_reservation(self, reservation):
        self.__reservation = reservation

    def make_reservation(self, room_type, start_date, end_date):
        '''
        This method will initiate the request for making a reservation with the necessary details
        that the guest have for the reservation
        '''
        print(f"Request of Reservation for {self.get_name()} with room type {room_type} Date : {start_date} till : {end_date}.")

    def check_in(self):
        '''
        This method will check the guest into their reserved room.
        '''
        print(f"Checking in {self.__name}.")

    def request_room_service(self, room_service_type):
        '''
        This method will be used when the guest desires to call the room service
        '''
        print(f"I {self.__name} would like a room service of type {room_service_type}.")

    def modify_personal_info(self, name=None, email=None, phone_number=None, address=None):
        '''
        This method will allow the user to update his/her details

        '''
        print("Modifying guest's personal information.")

    def view_reservation_details(self):
        '''
        This method will show the details of the guest's reservation.
        '''

        print(f"Reservation details for {self.__name}.")

    def cancel_reservation(self):
        '''
        This method will be called to cancel the reservation for the guest

        '''
        print(f"Cancelling reservation for {self.__name}.")



class Reservation:
    def __init__(self, guest, room_type, start_date, end_date):
        self.__guest = guest
        self.__room_type = room_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__is_checked_in = False

    def mark_as_checked_in(self):
        '''
        This method will mark the reservation as checked in
        Returns:

        '''
        print(f"Marking {self.__guest.get_name()}'s reservation as checked in.")

    def get_guest(self):
        return self.__guest

    def set_guest(self, guest):
        self.__guest = guest

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_start_date(self):
        return self.__start_date

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        self.__end_date = end_date


class RoomService:
    def __init__(self, service_type, room_number):
        self.__service_type = service_type
        self.__room_number = room_number
        self.__order_time = None
        self.__delivery_time = None

    def deliver_guest_order(self):
        '''
        This method will return the ordered itmes to the guest

        '''
        print("THis method will deliver the room service order to the guest.")

    def get_service_type(self):
        return self.__service_type

    def get_room_number(self):
        return self.__room_number

    def set_order_time(self, order_time):
        self.__order_time = order_time

    def get_order_time(self):
        return self.__order_time

    def set_delivery_time(self, delivery_time):
        self.__delivery_time = delivery_time

    def get_delivery_time(self):
        return self.__delivery_time


class FoodDelivery(RoomService):
    def __init__(self, room_number):
        super().__init__("Food Delivery", room_number)
        self.__food_items = {
            "Burger": 12,
            "Pasta": 14,
            "Steak": 25,
            "Salad": 8,
            "Dessert": 7
        }


    def get_food_menu(self):
        '''
        Shows all the items of food when the service offers

        '''
        return self.__food_items

class LaundryService(RoomService):
    def __init__(self, room_number):
        super().__init__("Laundry Service", room_number)
        self.__laundry_items = {
            "Shirt": 5,
            "Pants": 7,
            "Dress": 10,
            "Suit": 15
        }


    def get_laundry_menu(self):
        '''
        Shows all the items offered by the laundary service

        '''
        return self.__laundry_items

class Receptionist:
    def __init__(self, name, employee_id, contact_number):
        self.__name = name
        self.__employee_id = employee_id
        self.__contact_number = contact_number
        self.__reservations = []

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_contact_number(self):
        return self.__contact_number

    def make_reservation(self, guest, room_type, start_date, end_date):
        '''

        THis method will take the details of the reservation and make a reservation for that guest
        it will also show the details of the reservation which has been just created by the receptionist.

        '''
        reservation = Reservation(guest, room_type, start_date, end_date)
        guest.set_reservation(reservation)
        self.__reservations.append(reservation)

        # showing all the details
        print(f"Reservation confirmed for {guest.get_name()}:")
        print(f"Room Type: {room_type}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")

    def check_in_guest(self, guest):
        print(f"Checked in guest: {guest.get_name()}.")

    def view_reservations(self):
        print("Viewing all reservations.")

    def update_reservation(self, guest, new_room_type=None, new_start_date=None, new_end_date=None):
        print(f"Updated the reservation")

    def delete_reservation(self, guest):
        print(f"Deleted reservation for {guest.get_name()}.")


# making the objects for the guests
guest1 = Guest("Khalid", "khalid@gmail.com", "123-456-7890", "UAE")
guest2 = Guest("Ali", "ali@gmail.com", "234-567-8901", "UAE")
guest3 = Guest("Mohammed", "mohammed@gmail.com", "345-678-9012", "UAE")

# making the object for receptionist
receptionist = Receptionist("Umar", "EMP001", "987-654-3210")

# Making reservation for guest 1
room_type_1 = "Deluxe Room"
start_date_1 = "2024-09-30"
end_date_1 = "2024-10-02"

reservation_1 = receptionist.make_reservation(guest1, room_type_1, start_date_1, end_date_1)


# Making reservation for guest 2
room_type_2 = "Standard Room"
start_date_2 = "2024-10-03"
end_date_2 = "2024-10-05"

reservation_2 = receptionist.make_reservation(guest2, room_type_2, start_date_2, end_date_2)


# Making reservation for guest 3
room_type_3 = "Deluxe Room"
start_date_3 = "2024-10-05"
end_date_3 = "2024-10-07"

reservation_3 = receptionist.make_reservation(guest3, room_type_3, start_date_3, end_date_3)




