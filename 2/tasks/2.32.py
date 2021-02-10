ridge_length_in_meters = float(input("Длина гряды в метрах: "))
volume_of_space = float(input("Объем пространства, занимаемого концевой опорой в метрах: "))
amount_of_space_between_vines = float(input("объем пространства между виноградными лозами в метрах: "))
v = (ridge_length_in_meters - (2 * volume_of_space)) / amount_of_space_between_vines
print("Вы можете высадить:", int(v), "шт. виноградных лоз.")