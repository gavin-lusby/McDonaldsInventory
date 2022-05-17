# Manager or employees check stock (how much has been used, how much needs to be ordered)
def check_stock(item, stock):
  if item == "all":
    for a in stock:
      print(f"There are {a[1]} uses of {a[0]}.")
  else:
    for b in stock:
      if b[0] == item:
        print(f"There are {b[1]} uses of {item}.")


  #for future also print number of boxes and packages
  pass
# Should return nothing(prints current stock, may return current stock in later versions)