import numpy as np
import matplotlib.pyplot as plot
x = np.linspace(-4, 4, 100)     #x axis values
vals = np.sinc(x)               #y axis values => sinc
plot.plot(x, vals)              #plots the graph
plot.legend(["sinc"])
plot.ylabel("sinc", fontsize=10)
plot.xlabel("t")
plot.axhline(y=0, color="maroon")
plot.axvline(x=0, color="maroon")
plot.show()                      #displays the figure