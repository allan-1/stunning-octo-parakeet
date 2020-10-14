countries = [("Nairobi", 37), ("Kigali", 23), ("Dar-es laam", 44), ("Kampala", 33), ("Addis Ababa", 55)]
c_to_f = lambda lists : (lists[0], 9/5*lists[1] + 32)
farhheit = map(c_to_f, countries)
print(list(farhheit))
