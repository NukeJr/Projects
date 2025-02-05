
Fruit = ["Apple", "Pear", "Grapes"]

Vegetables = ["Cucumbers","Broccoli","Cabbage"]

Shopping = ["Milk","Soda"]+["Honey Bunches","Granola" ] 

print(Shopping[2:4])



Shopping = ['Milk','Sprite','Mountain Dew','Grapefruit Juice','Sparkling Water','Kombucka']+["Honey Bunches","Granola" ]

Fruit = Fruit[2:] + ['Blueberries']

Shopping[6] = ["Wheaties"]

Shopping +=   Shopping[6:8]  * 2
Shopping[5] = ''
Fruit += ["Raspberries"]
Shopping.remove('Mountain Dew')
Shopping += Fruit + Vegetables

print(Shopping)





