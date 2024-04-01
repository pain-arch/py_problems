while True: 
  print("Welcome to the Name the Lyrics game")
  print("")
  print("Fill in the blank lyrics!")
  print("")
  print("Type in the blank lyrics and see if you are as cool as me.")
  print("")
  print("Never going to ______ you up.")
  answer = input("what is the word? : ")
  if answer != "give":
    print("try again")
  elif answer == "give":
    print("well done")
    break
