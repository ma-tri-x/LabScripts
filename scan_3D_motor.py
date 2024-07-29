#!/usr/bin/python3
def moveMotor(whichMotor, step, x,y,z):
    if whichMotor == "X":
        x = x+step
    if whichMotor == "Y":
        y = y+step
    if whichMotor == "Z":
        z = z+step
    return x,y,z

def scan(stepsX, stepsY, stepsZ, shots_per_step):
    step_size_x = 1
    step_size_y = 1
    step_size_z = 1
    x_pos,y_pos,z_pos = 0.,0.,0.
    old_x_step = 0
    old_y_step = 0
    old_z_step = 0
    print("bla")
    for x_step in range(stepsX):
        for y_step in range(stepsY):
            for z_step in range(stepsZ):
                i = 0
                while True:
                    #data = arduino.readline().decode().strip()
                    data = "some"
                    if data and i < shots_per_step:
                        print(x_step,y_step,z_step,"  ",i, "\t",x_pos,y_pos,z_pos)
                        i += 1
                    if i == shots_per_step:
                        i=0
                        if z_step < stepsZ:
                            x_pos,y_pos,z_pos = moveMotor("Z",step_size_z,x_pos,y_pos,z_pos)
                        if z_step == stepsZ-1:
                            x_pos,y_pos,z_pos = moveMotor("Z",-stepsZ*step_size_z,x_pos,y_pos,z_pos)
                            x_pos,y_pos,z_pos = moveMotor("Y",step_size_y,x_pos,y_pos,z_pos)
                            if y_step == stepsY-1:
                                x_pos,y_pos,z_pos = moveMotor("Y",-stepsY*step_size_y,x_pos,y_pos,z_pos)
                                x_pos,y_pos,z_pos = moveMotor("X",step_size_x,x_pos,y_pos,z_pos)
                        break

scan(
    stepsX = 3,
    stepsY = 3,
    stepsZ = 3,
    shots_per_step=2)
print("end")
