while True:
  try:
    num = int(input("pick a num between 1 and 26"))
    print(chr(96 + num))
  except:
    num = 0
  if not 1 < num < 26:
    print("invalid")
