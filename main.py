import sys
import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import timezone

phone_number = phonenumbers.parse(str(sys.argv[1]))

zone = timezone.time_zones_for_number(phone_number)
geo = geocoder.description_for_number(phone_number, 'es')

print(phone_number, zone, geo)
