import csv

with open("RF.csv","r") as file:
	keys = file.readline()
	reader = csv.reader(file, delimiter=",")
	dataset = [x for x in reader]
keys = list(keys.split(","))
women_passengers = list(map(lambda x: x[4] == 'Безвизовый (до 90 дней)', dataset))
print(women_passengers.count(True))
