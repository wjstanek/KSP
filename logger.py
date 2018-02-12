import os.path

def log(sensorData):
    for i in range(0,99):
        filename = str('data' + str(i) + '.dat')
        if not os.path.isfile(filename):
            break
    with open(filename,'a') as file_object:
        file_object.write(str(sensorData[0]) + '\t' + str(sensorData[1]) + '\t' + str(sensorData[2]) + '\n')

if __name__ == '__main__':
    pass