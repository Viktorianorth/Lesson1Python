from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Apple', 'iPhone 14pro', '+7 (999) 476-6670'))
catalog.append(Smartphone('Samsung', 'Galaxy S21', '+7 (923) 698-0910'))
catalog.append(Smartphone('Huawei', 'P40 Pro', '+7 (999) 555-5555'))
catalog.append(Smartphone('Xiaomi', 'Mi 11', '+7 (921) 888-8888'))
catalog.append(Smartphone('Infinix', 'M21', '+7 (913) 666-6666'))

for phone in catalog:
    print(f'Марка: {phone.brand}, Модель: {phone.model}, Номер телефона: {phone.number}') # noqa:  E501.