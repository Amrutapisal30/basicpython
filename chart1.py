#pip install matplotlib
from matplotlib import pyplot
import numpy as np
# y=np.array([15,25,45,55])
# pyplot.pie(y)
# pyplot.show()

# y=np.array([15,25,45,55])
# mylables=["Apple","Banana","Cherry","Mango"]
# pyplot.pie(y,labels=mylables)
# pyplot.legend("Four Fruites")
# pyplot.show()

#Bar char ---- x axis-name   y axis-marks
# x=np.array(["john","blake","martin","tiger"])
# y=np.array([56,89,78,34])
# pyplot.bar(x,y,color=["red","green","blue","orange"])
# pyplot.xlabel("Name")
# pyplot.ylabel("Marks")
# pyplot.title("Marksheet")
# pyplot.legend("marks")
# pyplot.show()

#create a bar char ---x- mobile name y-price
# x=np.array(["Apple","Moto","Samsung","Oppo"])
# y=np.array([60000,30000,20000,10000])
# pyplot.bar(x,y)
# pyplot.xlabel("Mobile Name")
# pyplot.ylabel("Price")
# pyplot.show()


# x=np.array([10,20,30,40,50])
# y=np.array([100,200,300,400,500])
# pyplot.plot(x,y,marker='h') #marker='o','h'm,'v'
# pyplot.show()

#y axis is present and x axis is not present
y=np.array([23,45,67,77,81,93,99,100])
pyplot.plot(y,marker='h',ms='20',mfc='green',mec='red')
#ms-marker size mfc-marker face color mec-marker edge color
pyplot.show()