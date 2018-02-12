import matplotlib.pyplot as plt

x = []
y = []

with open('logtest.dat', 'r') as file_object:
    for lines in file_object:
        lines.strip()
        cols = lines.split()
        x.append(float(cols[0]))
        y.append(float(cols[1]))

print(x)
plt.plot(x,y)
plt.show()