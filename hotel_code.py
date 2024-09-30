
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
        pass

    def check_in(self):
        pass

    def request_room_service(self, room_service_type):
        pass

    def modify_personal_info(self, name=None, email=None, phone_number=None, address=None):
        pass

    def view_reservation_details(self):
        pass

    def cancel_reservation(self):
        pass



class Reservation:
    def __init__(self, guest, room_type, start_date, end_date):
        self.__guest = guest
        self.__room_type = room_type
        self.__start_date = start_date
        self.__end_date = end_date
        self.__is_checked_in = False

    def mark_as_checked_in(self):
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    def check_in_guest(self, guest):
        pass

    def view_reservations(self):
        pass

    def update_reservation(self, guest, new_room_type=None, new_start_date=None, new_end_date=None):
        pass

    def delete_reservation(self, guest):
        pass













