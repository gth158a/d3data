import matplotlib.pyplot as plt
import numpy as np

def plot9():
    data = [ ("data1", 34), ("data2", 22),
            ("data3", 11), ( "data4", 28),
            ("data5", 57), ( "data6", 39),
            ("data7", 23), ( "data8", 98)]
    #N = len( data )
    N = len( ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] )
    x = np.arange(1, N+1)
    #y = [ num for (s, num) in data ]
    y = [8, 8, 3, 18, 9, 10, 4]
    # labels = [ s for (s, num) in data ]
    labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    width = 1
    bar1 = plt.bar( x, y, width, color="y" )
    plt.ylabel( 'Commits' )
    plt.xticks(x + width/2.0, labels )
    plt.show()


plot9()