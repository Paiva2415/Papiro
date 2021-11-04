hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura
hour = hour + (mins // 60)
mins2 = mins % 60
hour2 = hour % 24

print (hour2, ":", mins2)
2
