from djitellopy import Tello
import cv2
from keyboard import read_event

tello = Tello()
tello.connect()
tello.takeoff()

x = 0
y = 0
z = 0
yaw = 0
w = s = d = a = e = q = i = k = False

# loop to capture keys continuously
while True:
    # capture a keyboard event
    event = read_event()

    # if a key is pressed
    if event.event_type == 'down':
        # Instead of setting all flags to False, set only the ones you're changing.
        w = s = d = a = e = q = i = k = False

        if event.name == 'esc':
            tello.land()
            tello.streamoff()
            break

        if event.name == 'w':
            z = 40
            w = True

        if event.name == 's':
            z = -40
            s = True

        if event.name == 'd':
            x = 40
            d = True

        if event.name == 'a':
            x = -40
            a = True

        if event.name == 'i':
            y = 40
            i = True

        if event.name == 'k':
            y = -40
            k = True

        if event.name == 'e':
            yaw = 60
            e = True

        if event.name == 'q':
            yaw = -60
            q = True

        if event.name == 'p':
            frame_read = tello.get_frame_read()
            cv2.imshow('Live Video', frame_read.frame)
            cv2.waitKey(1000)

        if event.name == 'enter':
            tello.emergency()
            break

    elif event.event_type == 'up':

        controls = {'w': False, 's': False, 'd': False, 'a': False, 'i': False, 'k': False, 'e': False, 'q': False}
        if event.name in controls:
            controls[event.name] = False

        w, s, d, a, e, q, i, k = [controls[key] for key in ['w', 's', 'd', 'a', 'e', 'q', 'i', 'k']]

    z = 40 if w else (-40 if s else 0)
    x = 40 if d else (-40 if a else 0)
    y = 40 if i else (-40 if k else 0)
    yaw = 60 if e else (-60 if q else 0)

    tello.send_rc_control(x, z, y, yaw)