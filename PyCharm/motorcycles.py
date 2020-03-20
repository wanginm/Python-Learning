motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('toyota')
print(motorcycles)

motorcycles.insert(0,'honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

people_motorcycle=motorcycles.pop()
print(motorcycles)
print(people_motorcycle)

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

first_owned=motorcycles.pop(0)
print(first_owned)
print(motorcycles)


motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(too_expensive)
print(motorcycles)