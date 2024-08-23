from address import Address
from mailing import Mailing

to_address = Address("123456", "г. Калининград", "ул. Ленина", "д. 1", "кв. 1")
from_address = Address("654321", "г. Санкт-Петербург", "пр. Невский", "д. 2", "кв. 10")
mailing = Mailing(to_address, from_address, 500, "45005145009749")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей")
