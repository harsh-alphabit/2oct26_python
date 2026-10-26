def getdata(data):
    print("ID:",data[0])
    print("Name:",data[1])
    print("City:",data[2])

getdata([45,'harsh','rajkot']) #List arg


def stdata(*data):
    print("ID:",data[0])
    print("Name:",data[1])
    #print("City:",data[2])
    

stdata(1,'harsh','Rajkot')
