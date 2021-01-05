import schemas
import datetime


def get_booking_amount(booking: schemas.Booking):
    start_date = booking.start_date.replace(tzinfo=None)
    end_date = booking.end_date.replace(tzinfo=None)
    total_amount = 0.0
    if start_date and end_date:
        rate_card = booking.machine.rate_card
        if rate_card.type.id == 'H':
            hours = (end_date - start_date).seconds/3600
            total_amount = hours * rate_card.amount/rate_card.quantity
        elif rate_card.type.id == 'A':
            total_amount = booking.area * rate_card.amount/rate_card.quantity

    return total_amount
