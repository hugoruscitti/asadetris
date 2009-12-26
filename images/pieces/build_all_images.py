import os

def rotate(index, filename, angle):

    to = "p" + str(index) + "/" + filename.split('.')[0] + "_" + str(angle) + ".png"

    os.system("convert -rotate %d -gravity Center -background none -crop 200x200+0+0 +repage    %s %s" %(angle, filename, to))
    print "creating:", to


for angle in range(0, 360, 30):
    rotate(0, "0.png", angle)
    rotate(1, "1.png", angle)
    rotate(2, "2.png", angle)
    rotate(3, "3.png", angle)
    rotate(4, "4.png", angle)
    rotate(5, "5.png", angle)
    rotate(6, "6.png", angle)
