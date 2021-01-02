from PIL import Image
import matplotlib.pyplot as plt
im= Image.open('RGB_image.jpg')
b, g ,r = im.split()
GreenHist= g.histogram()
BlueHist= b.histogram()
RedHist= r.histogram()
plt.plot(GreenHist, 'g')
plt.plot(RedHist,'r')
plt.plot(BlueHist, 'b')
plt.xlabel('Pixel Value')
plt.ylable('Frequency of Pixels')
