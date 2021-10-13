import numpy as np
import matplotlib.pyplot as plot
fs = 10000                              # sampling freq
fm = 100                                # message freq
w = 2 * np.pi * fm / fs                 # discrete frequency
N = 100                                 # time period
time = np.arange(0, N, 1);              #x axis values
amplitude = np.sin( w * time)
amp2 = np.cos(w*time)                   #y axis values
plot.plot(time, amplitude,color="red")  # plot
plot.stem(time,amp2,linefmt="grey",markerfmt="B",basefmt = "yellow")
plot.title('Sine wave')                 # Give a title for the sine wave plot
plot.xlabel('Time')                     # Give x axis label for the sine wave plot
plot.ylabel('Amplitude = sin(time)')    # Give y axis label for the sine wave plot
plot.grid(True, which='both')
plot.legend(["Sine","Cos"],fontsize = 20)
plot.axvline(x=0, color='green')
plot.axhline(y=0, color='green')
plot.show()