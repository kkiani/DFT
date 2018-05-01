import matplotlib.pyplot as plt
import random
import numpy as np



def main():
    a = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    b = [2, 4, 8, 16, 32, 64, 128]
    c = [8, 5, 4, 3, 2, 2, 1, 1]
    d = [0, 0, 0, 0, 3, 3, 3, 3]
    # ef = np.e
    x = np.array(a)
    y = np.fft.fft(x)
    yy = []
    for item in y:
    	yy.append(abs(item))
    z = DFT(x)

    showPlot(x, yy, z)



def DFT(input_sample):
    N = input_sample.__len__()
    dft = []
    for k in range(0, N):
        x = 0
        for n in range(0, N-1):
            x += input_sample[n]*pow(np.e, -1j*(2*np.pi*k*n)/N)

        dft.append(abs(x))

    return dft


def showPlot(*xarg):
    plotNum = xarg.__len__()
    fig = plt.figure()
    fig.canvas.set_window_title('DFT Test')

    i = 1
    for draw in xarg:
        ax1 = fig.add_subplot(plotNum, 1, i)
        ax1.stem(draw)
        i += 1


    plt.show()


if __name__ == "__main__":
    main()
