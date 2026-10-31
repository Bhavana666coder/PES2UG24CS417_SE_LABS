
"""Hotel room reservation and booking management module."""

import hashlib
import os
import secrets

room_inventory = {
    "101": {"type": "Deluxe", "price": 150.0, "is_booked": False},
    "102": {"type": "Suite", "price": 300.0, "is_booked": True},
    "103": {"type": "Standard", "price": 90.0, "is_booked": False},
}


def book_room(room_num, guest_name, booking_log=None):
    """Reserve an available room and record the booking."""
    if booking_log is None:
        booking_log = []

    if room_num not in room_inventory:
        return False

    if room_inventory[room_num]["is_booked"]:
        return False

    room_inventory[room_num]["is_booked"] = True
    message = f"Reserved room {room_num} for guest {guest_name}"
    booking_log.append(message)
    return True


def cancel_booking(room_num):
    """Cancel a room reservation if the room exists."""
    if room_num not in room_inventory:
        return False

    room_inventory[room_num]["is_booked"] = False
    return True


def check_room_status(room_num):
    """Return True if an existing room is available."""
    room = room_inventory.get(room_num)

    if room is None:
        return False

    return not room["is_booked"]


def compute_seasonal_rate(room_num, seasonal_multiplier):
    """Calculate a room rate using a numeric multiplier."""
    if room_num not in room_inventory:
        raise ValueError("Room number does not exist.")

    if (
        not isinstance(seasonal_multiplier, (int, float))
        or seasonal_multiplier < 0
    ):
        raise ValueError("Seasonal multiplier must be a non-negative number.")

    base_price = room_inventory[room_num]["price"]
    return base_price * seasonal_multiplier


def generate_guest_hash(guest_id):
    """Generate a SHA-256 hash for a guest identifier."""
    return hashlib.sha256(guest_id.encode("utf-8")).hexdigest()


def generate_booking_ref():
    """Generate a booking reference using a secure random generator."""
    return secrets.randbelow(9000) + 1000


def export_room_ledger(filename="hotel_ledger.txt"):
    """Export the room inventory to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as ledger_file:
        ledger_file.write(str(room_inventory))

    print(f"Hotel ledger exported to: {filename}")


def main():
    """Run a demonstration of the hotel booking functions."""
    hotel_secret_key = os.getenv("HOTEL_ADMIN_RESERVATION_TOKEN")

    book_room("101", "Emma Watson")
    cancel_booking("102")

    print("Is 103 available:", check_room_status("103"))
    print("Surge price:", compute_seasonal_rate("101", 1.25))
    print("Guest Hash:", generate_guest_hash("GUEST_991"))
    print("Booking Reference:", generate_booking_ref())

    export_room_ledger()
    print("Secret key configured:", bool(hotel_secret_key))


if __name__ == "__main__":
    main()
