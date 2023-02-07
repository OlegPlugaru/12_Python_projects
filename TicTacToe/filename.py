def ReadData(read):
    return f"candy data from {read}\n"

# OUR PROGRAM STARTS HERE
fileName = [None]*700
masterData = ""

for i in range(len(fileName)):
    fileName[i] = f"Candy Data {i+1}.txt"
    masterData += ReadData(fileName[i])

print(masterData)