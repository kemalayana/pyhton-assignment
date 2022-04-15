from datetime import datetime

dogum = input("doğum tarihinizi giriniz: (Gün.Ay.Yıl) ")

toOrdinal_date1 = datetime.strptime(dogum,"%d.%m.%Y").toordinal()
toOrdinal_date2 = datetime.today().toordinal()

ordinal = (toOrdinal_date2 - toOrdinal_date1)  # fark ordinal
Gregorian = date.fromordinal(ordinal)          # Gregorian Ordinal

print(f"1: {toOrdinal_date1}, 2: {toOrdinal_date2} fark day: {ordinal} -- {Gregorian}")