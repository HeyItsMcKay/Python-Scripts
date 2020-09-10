length = int(input("Length of bridge: "))
#sub cap num, check cap-1 mod
for caps in range(2, length):
    if ((length-caps) % (caps-1) == 0):
        print(str(caps) + " caps, sections of length " + str((length-caps) / (caps-1))[:2])
input()