day = input("Din enter karo> ")
meal = input("Meal enter karo, jaise breakfast lunch aur dinner mein se ek> ")
if day == "monday":
  if meal == "breafast":
    print("Poha")
  elif meal == "lunch":
    print("Rajma Chawal")
  else:
    print("Roti Sabzi")
elif day == "tuesday":
  if meal == "breakfast":
    print("Poori Sabzi")
  elif meal == "lunch":
    print("Thukpa")
  elif meal=="dinner":
    print("Chicken Chawal")
  else:
    print("Aur kisi bhi din hum daal roti sabzi khaynege.")
else:
  print("aloo paratha")