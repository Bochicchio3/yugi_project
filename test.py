import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import mouse
from util_paddle_ocr import *

# _boxes = [[[701, 808], [1873, 1029]], # monsters
#         [[681, 1052], [1884, 1268]], # spells
#         [[694, 1224], [1938, 1436]], # hand
#         [[1849, 572], [2101, 771]], # hand
#         [[524, 835], [668, 1023]]] # button

screen =  {'top': 240, 'left': 0, 'width': 2560, 'height':1440 }
hand = {'top': 1450, 'left': 650, 'width': 1300, 'height':250 }
monsters = {'top': 1050, 'left': 650, 'width': 1250, 'height':200 }
spells =  {'top': 1300, 'left': 650, 'width': 1250, 'height':200 }
turns =  {'top': 1300, 'left': 650, 'width': 1250, 'height':200 }
 
sct = mss()
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('my hand_.avi', fourcc, 10, (bounding_box['width'],bounding_box['height']))

boxes = []
count = 0

class coords:
    
    def __init__(self):
        x1 = 0
        y1 = 0
        
class coords_img:
    
    def __init__(self):
        x1 = 0
        y1 = 0
        img_ = None
        img = None
        w = 0
        h = 0
        
        
list_of_clicks = []

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Start Mouse Position: '+str(x)+', '+str(y))
         sbox = [x, y]
         params.x1 = x
         params.y1 = y
        #  boxes.append(sbox)

    elif event == cv2.EVENT_LBUTTONUP:
        print ('End Mouse Position: '+str(x)+', '+str(y))
        ebox = [x-params.x1, y-params.y1]
        boxes.append([[params.x1, params.y1], ebox])
        
        
        
        
def save_roi(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Start Mouse Position: '+str(x)+', '+str(y))
         sbox = [x, y]
         params.x1 = x
         params.y1 = y
        #  boxes.append(sbox)

    elif event == cv2.EVENT_LBUTTONUP:
        print ('End Mouse Position: '+str(x)+', '+str(y))
        
        params.w = x - params.x1
        params.h = y - params.y1
        
        ebox = [params.w, params.h]
        boxes.append([[params.x1, params.y1], ebox])        
        bb =  {'top': params.x1, 'left': params.y1, 'width': ebox[0], 'height':ebox[1] }
        # sct_img1 = sct.grab(bb)
        print ("saving bb_{}{}".format([params.y1, params.x1], [params.y1 + params.h, params.x1 + params.w]))
        # print (params.y1, params.x1, params.h, params.w)
        params.img = params.img_[params.y1 : params.y1 + params.h , params.x1 : params.x1 + params.w ,0:3]
        cv2.imwrite('bb_{}{}.png'.format([params.x1, params.y1],  [params.y1 + params.h, params.x1 + params.w]),params.img)


def record_clicks(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Record_click: '+str(x)+', '+str(y))
         sbox = [x, y]
         list_of_clicks.append(sbox)

starting_coords = coords()
sc = coords_img()
sc2 = coords_img()
sc2.x1 = 0
sc2.y1 = 0
sc2.h = 0
sc2.w = 0
sc2.img = []
sc2.img_ = None
mouse_clicks = []
cv2.namedWindow('screen')
ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory

# out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (bounding_box['width'],bounding_box['height']))
while True:
    sct_img1 = sct.grab(screen)
    sc.img = np.array(sct_img1)[:,:,0:3]
    sc2.img_= np.array(sct_img1)[:,:,0:3]
    # sct_img2 = sct.grab(hand)
    # sc2.img = np.array(sct_img2)
    # sct_img1 = sct.grab(hand)
    # sct_img2 = sct.grab(monsters)
    # sct_img3 = sct.grab(spells)

    cv2.imshow('screen',  sc.img)
    # cv2.imshow('screen', np.array(sct_img1))
    # cv2.imshow('hand', np.array(sct_img1))

    # cv2.imshow('monster', sc2.img)
    if (len(sc2.img ) > 0):
        result = run_inference(ocr, sc2.img)
        res = vis_result_from_img(sc2.img, result)
        cv2.imshow('monsters', res)

    # cv2.imshow('spells', np.array(sct_img3))
#     out.write(np.array(sct_img)[:,:,0:3])
    if (cv2.waitKey(15) & 0xFF) == ord('m'):
        cv2.setMouseCallback('screen', on_mouse, starting_coords)
        print ("Setting up roi callback")
        # cv2.destroyAllWindows()
        # break
    if (cv2.waitKey(15) & 0xFF) == ord('r'):
        print ("Recording clicks")
        cv2.setMouseCallback('screen', record_clicks, 0)
        
    if (cv2.waitKey(15) & 0xFF) == ord('e'):
        for click in list_of_clicks:
            print ("Clicking ", click)
            mouse.move(str(click[0]), str(click[1]))
            mouse.click(button='left')
            time.sleep(0.1)
        list_of_clicks= []
        # cv2.setMouseCallback('screen', record_clicks, 0)

        
        
    if (cv2.waitKey(15) & 0xFF) == ord('d'):
        cv2.setMouseCallback('screen',  lambda *args : None, 0)
        print (boxes)
        

    if (cv2.waitKey(15) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
    

    if (cv2.waitKey(15) & 0xFF) == ord('s'):
        print ("ready to save")
        cv2.setMouseCallback('screen',  save_roi, sc2)

        # cv2.destroyAllWindows()
        # break
    
    

        
# out.release()

# while True:

#     cv2.imshow('screen', img)
#     if (cv2.waitKey(15) & 0xFF) == ord('q'):
#         cv2.destroyAllWindows()
#         break









# #  Test if ocr works in that region
# def read_hand():
    
    