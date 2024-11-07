from address import Address
from Mailing import Mailing

to_address = Address("123456", "Moscow", "Pobedy", "6", "456")
from_address = Address("789012", "SPb", "Pobedy", "9", "1")
mailing = Mailing(to_address, from_address, 200, "1234567890")
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.room}"
      f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.room}. "      f"Стоимость {mailing.cost} рублей.")