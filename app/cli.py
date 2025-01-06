from models import Band, Venue, Concert,Session
from helpers import validate_date,validate_string 

def main_menu() :
    print ("===Music-Event-Manager===")
    print("1. Add New Band")
    print("2. Add New Venue")   
    print("3. Schedule Concert")
    print("4. List All Bands")
    print("5. Exit")
    
    
def get_user_input(prompt, validator=None):
    while True:
        value = input(prompt).strip()
        if validator is None or validator(value):
            return value
        print("Invalid input. Please try again.")

def add_band(session):
    name = get_user_input("Enter band name: ", validate_string)
    hometown = get_user_input("Enter hometown: ", validate_string)
    band = Band(name=name, hometown=hometown)
    session.add(band)
    session.commit()
    print(f"Added band: {band.name} from {band.hometown}")

def add_venue(session):
    title = get_user_input("Enter venue name: ", validate_string)
    city = get_user_input("Enter city: ", validate_string)
    venue = Venue(title=title, city=city)
    session.add(venue)
    session.commit()
    print(f"Added venue: {venue.title} in {venue.city}")

def list_bands(session):
    bands = session.query(Band).all()
    if not bands:
        print("No bands found.")
        return
    print("\nAll Bands:")
    for band in bands:
        print(f"- {band.name} from {band.hometown}")

def handle_choice(choice, session):
    if choice == '1':
        add_band(session)
    elif choice == '2':
        add_venue(session)
    elif choice == '3':
        schedule_concert(session)   
    elif choice == '4':
        list_bands(session)
    elif choice == '5':
        return False
    return True    

def schedule_concert(session):
    band_id = get_user_input("Enter Band ID: ", lambda x: x.isdigit())
    venue_id = get_user_input("Enter Venue ID: ", lambda x: x.isdigit())
    date = get_user_input("Enter concert date (YYYY-MM-DD): ", validate_date)
    
    band = session.query(Band).get(int(band_id))
    venue = session.query(Venue).get(int(venue_id))

    if not band or not venue:
        print("Error: Invalid Band or Venue ID")
        return

    concert = Concert(date=date, band=band, venue=venue)
    session.add(concert)
    session.commit()
    print(f"Concert scheduled for {band.name} at {venue.title} on {date}")
