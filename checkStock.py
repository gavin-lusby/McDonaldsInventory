# Manager or employees check stock (how much has been used, how much needs to be ordered)

# Edited by Isaac (2022-5-23)

def DD_find (DD, item):
  for l in range(len(DD)):
    if DD[l] == item:
      return l
  pass

def check_stock(item, stock, subdivs):
  if item == "all":
    for a in stock:
      subdindex = DD_find(subdivs, a)
      print(f"There are {a[1]//subdivs[0]} {a[0]} ({a[1] uses}).")
  else:
    for b in stock:
      if b[0] == item:
        print(f"There are {b[1]} uses of {item}.")


  #for future also print number of boxes and packages
  pass
# Should return nothing(prints current stock, may return current stock in later versions)