
def createfile():
    filename = 'logtest.dat'
    with open(filename, 'a') as file_object:
        file_object.write('Distance\tAltitude\n')

if __name__ == '__main__':
    createfile()