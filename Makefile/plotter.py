import matplotlib.pyplot as plt

file = open("Data.txt","r")
data = file.read()

data = data.split("X=")[1].split("Y=")

data_x = data[0].split(",")
data_y = data[1].split(",")


plt.plot(data_x, data_y)
plt.show()