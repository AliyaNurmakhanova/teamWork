
def dateInputs():
    date_entry = ()
    while True:
        date = input("Введите дату поступления в университет :")
        if not date:
            break
        date_entry = date_entry + (date,)
    return date_entry

print(dateInputs())