import matplotlib.pyplot as plt

tmpFile = "robocontrol.txt"
car_pos_xs=[]
car_pos_ys=[]
planXsYs=[]
targXsYs=[]

with open(tmpFile,"r",  encoding='utf-8') as fopen:
    allLines = fopen.readlines()
    for curLine in allLines:
        curLine = curLine.strip()

        if "car_pos" in curLine or "zhang: mowing_xy[0]" in curLine or "target_pose of the current path--x, y :" in curLine:
            #print(curLine)
            if "car_pos_x" in curLine:
                finalIndex = curLine.find("car_pos_x:")
                posX = float(curLine[finalIndex+10: finalIndex+10+8])
                car_pos_xs.append(posX)
                #print(posX)
            elif "car_pos_y" in curLine:
                finalIndex = curLine.find("car_pos_y:")
                posY = float(curLine[finalIndex+10: finalIndex+10+8])
                car_pos_ys.append(posY)
                #print(posY)
            elif "zhang: mowing_xy[0]" in curLine and "mowing_xy[1]" in curLine and"mowing_xy[2]" in curLine:
                print(curLine)
                index0 = curLine.find("zhang: mowing_xy[0]:")
                index1 = curLine.find("mowing_xy[1]:")
                index2 = curLine.find("mowing_xy[2]:")
                planX0=float(curLine[index0+20: index1].split(",")[0])
                planY0=float(curLine[index0+20: index1].split(",")[1])
                planX1=float(curLine[index1+13: index2].split(",")[0])
                planY1=float(curLine[index1+13: index2].split(",")[1])
                planX2=float(curLine[index2+13: -1].split(",")[0])
                planY2=float(curLine[index2+13: -1].split(",")[1])
                if (planX0,planY0) not in planXsYs:
                    planXsYs.append((planX0,planY0))
                if (planX1,planY1) not in planXsYs:
                    planXsYs.append((planX1,planY1))
                if (planX2,planY2) not in planXsYs:
                    planXsYs.append((planX2,planY2))
                #mowXs.append(mowX)
                #mowYs.append(mowY)
                #print(mowX0, ",", mowY0," ; ",mowX1,",",mowY1," ; ",mowX2,",",mowY2)
            elif "target_pose of the current path--x, y :" in curLine:
                finalIndex = curLine.find("target_pose of the current path--x, y :")
                targX=float(curLine[finalIndex+39: -1].split(",")[0])
                targY=float(curLine[finalIndex+39: -1].split(",")[1])
                if (targX,targY) not in targXsYs:
                    targXsYs.append((targX,targY))
                #print(mowX, " , ", mowY)


assert len(car_pos_xs)==len(car_pos_ys), "not equal car_pos_xy"

plt.plot(car_pos_xs, car_pos_ys, label="car_pos")
planXs=[]
planYs=[]
for planXY in planXsYs:
    planXs.append(planXY[0])
    planYs.append(planXY[1])
# plt.plot(planXs, planYs, label="plan_path")
targXs=[]
targYs=[]
for targXY in targXsYs:
    targXs.append(targXY[0])
    targYs.append(targXY[1])
plt.plot(targXs, targYs, label="target_point")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

