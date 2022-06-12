while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(choice == "#"):
    print("Done. Terminating")
    exit()
  def checking(g):
    if g.isdigit():
      continue
    else:
      print("Not a valid number,please enter again")
      break
  def gettingNumbers():
    a= input("Enter first number: ")
    checking(a) 
    b= input("Enter second number: ")
    checking(b)
    return a,b
  
