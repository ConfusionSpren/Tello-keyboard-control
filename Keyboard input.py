from djitellopy import Tello
import threading, math, cv2, keyboard

tello=Tello()

tello.connect()
tello.send_command_with_return('takeoff')
tello.is_flying = True
tello.streamon()
x_accel = 0
y_accel = 0
z_accel = 0
x = True


while x == True:
    #Stablization variables
    tello.get_acceleration_x(x_accel)
    tello.get_acceleration_y(y_accel)
    tello.get_acceleration_z(z_accel)
    
    math.floor(x_accel)
    math.floor(y_accel)
    math.floor(z_accel)
    
    #Keyboard Controls 
    if keyboard.is_pressed('w'):
        tello.send_rc_control(0,40,0,0)
        
    if keyboard.is_pressed('s'):
        tello.send_rc_control(0,-40,0,0)
        
    if keyboard.is_pressed('d'):
        tello.send_rc_control(40,0,0,0)
        
    if keyboard.is_pressed('a'):
        tello.send_rc_control(-40,0,0,0)
        
    if keyboard.is_pressed('i'):
        tello.send_rc_control(0,0,40,0)
        
    if keyboard.is_pressed('k'):
        tello.send_rc_control(0,0,-40,0)
        
    if keyboard.is_pressed('e'):
        tello.send_rc_control(0,0,0,60)
        
    if keyboard.is_pressed('q'):
        tello.send_rc_control(0,0,0,-60)
        
    if keyboard.is_pressed('p'):
        frame_read = tello.get_frame_read()
        cv2.imshow('Live Video', frame_read.frame)
        cv2.waitKey(1000)
        
    if keyboard.is_pressed('enter'):
        tello.land()
        x = False 
        tello.streamoff()
       
    # Stablization for drone, untested
    if not keyboard.is_pressed('w') and not keyboard.is_pressed('s'):
        tello.send_rc_control(0, -z_accel, 0, 0)
    if not keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
        tello.send_rc_control(-x_accel, 0, 0, 0)
    if not keyboard.is_pressed('k') and not keyboard.is_pressed('i'):
        tello.send_rc_control(0, 0, -y_accel, 0)
    else:        pass
exit()
