import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import mouse
from util_paddle_ocr import *
import pyautogui



# mouse = Controller()


screen =  {'top': 240, 'left': 0, 'width': 2560, 'height':1440 }
hand = {'top': 1450, 'left': 650, 'width': 1300, 'height':250 }
monsters = {'top': 1050, 'left': 650, 'width': 1250, 'height':200 }
spells =  {'top': 1300, 'left': 650, 'width': 1250, 'height':200 }
turns =  {'top': 1300, 'left': 650, 'width': 1250, 'height':200 }
 
sct = mss()


list_of_clicks = []
list_of_mouse_positions = []
def record_clicks(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Record_click: '+str(x)+', '+str(y))
         sbox = [y, x + 240]
         list_of_clicks.append(sbox)





def get_num_of_cards():

    '''
    '''
    # roi = [...]
    # roi_bg = [...]
    # Given coordinates, roi are taken from current screen, roi_bg are loaded from a folder.
    for r, r_bg in zip(roi, roi_bg):
        if r == r_bg:
            counter+=1
    return counter

# out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (bounding_box['width'],bounding_box['height']))
while True:
    sct_img1 = sct.grab(screen)
    # sct_img2 = sct.grab(hand)
    # sc2.img = np.array(sct_img2)
    # sct_img1 = sct.grab(hand)
    # sct_img2 = sct.grab(monsters)
    # sct_img3 = sct.grab(spells)

    cv2.imshow('screen',  np.asarray(sct_img1)[:,:,0:3])

    if (cv2.waitKey(15) & 0xFF) == ord('r'):
        print ("Recording clicks on opencv interface")
        cv2.setMouseCallback('screen', record_clicks, 0)
        
    if (cv2.waitKey(15) & 0xFF) == ord('e'):
        for click in list_of_mouse_positions:
            print ("Clicking ", click)
            pyautogui.click(str(click[0]), str(click[1]))
            time.sleep(0.3)
            # mouse.click(button='left')
        list_of_mouse_positions= []
        # cv2.setMouseCallback('screen', record_clicks, 0)

    if (cv2.waitKey(15) & 0xFF) == ord('m'):
        print ("Recording mouse positions on the screen")
        list_of_mouse_positions +=[pyautogui.position()]
        print('Position is {}'.format(pyautogui.position()))

    if (cv2.waitKey(15) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

        # cv2.destroyAllWindows()
        # break
    