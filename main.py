import numpy as np
import cv2
from matplotlib import pyplot as plt

obj_img =  cv2.imread("images/car.jpg")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
print(type(obj_img))
input()
plt.imshow(obj_img)
plt.show()

height, width, colorChannelNumber = obj_img.shape

print("[Image Dimensions]: " + str(height) + "x" + str(width) + "\n")
print("[Color Channel Number]: " + str(colorChannelNumber) + "\n")

f = open("imageInformationText/imageInformation.txt", "w")

for x in range(0, height):
    for y in range(0, width):

        line = "[obj_img["+str(x)+"]["+str(y)+"]]: " + str(obj_img[x][y]) + "\n"

        f.write(line)

        print(line)
        print(type(obj_img[x][y]))

        #if (x == 9 and y == 3):
        #   input()

        if(y < 11 and y > -1 and (x == 0 or x == 1)):
            obj_img.itemset((x,y,1), 0)
            obj_img.itemset((x,y,2), 0)

    f.write("\n\n")
    print("\n\n")


plt.imshow(obj_img)
plt.show()


a = np.array([1,1,1])
print(a + [1,5,1])
print(a / 5)




