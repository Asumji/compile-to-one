# reading every data file
data = ["data1.txt", "data2.txt", "data3.txt"]

full_data = ""
for i in range(8):
    with open(data[i], "r") as f:
        readData = f.read()
        print("\n" + data[i] + "\n" + readData)
        full_data += "\n\n" + data[i] + "\n" + readData

#writing to the main file
with open("output.txt", "w") as f:
    f.write(full_data)
