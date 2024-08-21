from smartphone import Smartphone

catalog = []
samsung = Smartphone("Samsung", "Galaxy S23", "+79111111111")
iphone = Smartphone("iPhone", "15 Pro Max", "+79222222222")
realme = Smartphone("realme", "11", "+79333333333")
honor = Smartphone("Honor", "200", "+79444444444")
huawei = Smartphone("Huawei", "nova 12i", "+79555555555")

catalog.append(samsung)
catalog.append(iphone)
catalog.append(realme)
catalog.append(honor)
catalog.append(huawei)

for p in catalog:
    print(f"[{p.brand} - {p.model}. {p.number}]")
