import stpd

while True:
    x = input("stpd > ")

    if x != "exit":
        stpd.run(stpd.tokenize(x))
    else:exit(0)
