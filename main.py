import numpy as np
import cv2

from mss import mss
from PIL import Image

import time
import pyautogui

from utils.util_paddle_ocr import *
from utils.configuration import screen
from utils.roi import Roi



class Test:
    
    def __init__(self):
                
        self.rois = []  
        self.opencv_clicks = []
        self.screen_clicks = []
        self.screen_img = None
        self.ocr_roi_flag = None
        self.ocr_roi = None
        self.sct = mss()
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
        self.roi = Roi()

    # def read_hand(self):
    #     '''
    #     Return dict with cards in hands?
    #     '''
    # def read monsters()
    
    
    
    
    # def send_state():
        


    def add_roi_to_list(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print ('Start Mouse Position: '+str(x)+', '+str(y))
            sbox = [x, y]
            self.roi.x0 = sbox[0]
            self.roi.y0 = sbox[1]

        elif event == cv2.EVENT_LBUTTONUP:
            print ('End Mouse Position: '+str(x)+', '+str(y))
            ebox = [x-self.roi.x0, y-self.roi.y0]
            self.rois.append([[x, y], ebox])
            
            
    def save_roi(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print ('Start Mouse Position: '+str(x)+', '+str(y))
            sbox = [x, y]
            self.roi.x0 = sbox[0]
            self.roi.y0 = sbox[1]

        elif event == cv2.EVENT_LBUTTONUP:
            print ('End Mouse Position: '+str(x)+', '+str(y))
            
            self.roi.x1 = x
            self.roi.y1 = y
            self.roi.w = x - self.roi.x0
            self.roi.h = y - self.roi.y0
            ebox = [self.roi.w, self.roi.h]
            self.ocr_roi = self.screen_img[ self.roi.y0 : self.roi.y0 + self.roi.h , self.roi.x0 : self.roi.x0 + self.roi.w ,0:3]

            # bb =  {'top': params.x1, 'left': params.y1, 'width': ebox[0], 'height':ebox[1] }
            print ("saving bb_{}{}".format([self.roi.y0, self.roi.x0], [self.roi.y0 + self.roi.h, self.roi.x0 + self.roi.w]))
            cv2.imwrite('bb_{}{}.png'.format([self.roi.x0, self.roi.y0],  [self.roi.y0 + self.roi.h,self.roi.x0 + self.roi.w]), self.ocr_roi)

    def select_ocr_roi(self,event, x, y, flags, params):
        
        if event == cv2.EVENT_LBUTTONDOWN:
            print ('Start Mouse Position: '+str(x)+', '+str(y))
            sbox = [x, y]
            self.roi.x0 = sbox[0]
            self.roi.y0 = sbox[1]

        elif event == cv2.EVENT_LBUTTONUP:
            print ('End Mouse Position: '+str(x)+', '+str(y))
            
            self.roi.x1 = x
            self.roi.y1 = y
            self.roi.w = x - self.roi.x0
            self.roi.h = y - self.roi.y0
            ebox = [self.roi.w, self.roi.h]
            
            # bb =  {'top': params.x1, 'left': params.y1, 'width': ebox[0], 'height':ebox[1] }
            print ("Selecting {}{}".format([self.roi.y0, self.roi.x0], [self.roi.y0 + self.roi.h, self.roi.x0 + self.roi.w]))
            self.ocr_roi = self.screen_img[ self.roi.y0 : self.roi.y0 + self.roi.h , self.roi.x0 : self.roi.x0 + self.roi.w ,0:3]
            self.ocr_roi_flag = True

    def record_click_on_opencv_interface(self,event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print ('Record_click: '+str(x)+', '+str(y))
            sbox = [x, y]
            self.opencv_clicks.append(sbox)


    def record_click_on_screen(self,event, x, y, flags, params):
        # if event == cv2.EVENT_LBUTTONDOWN:
        sbox = pyautogui.position()
        x = sbox[0]
        y = sbox[1]
        print ('Record_click: {}, {}'.format(x, y))
        self.screen_clicks.append(sbox)
        
        
    def acquire_screen(self):
        
        cv2.namedWindow('screen')
        cv2.resizeWindow('screen', 2560//2, 1440//2)
        # out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (bounding_box['width'],bounding_box['height']))
        while True:


            self.screen_img = self.sct.grab(screen)
            self.screen_img = np.array(self.screen_img)[:,:,0:3]


            cv2.imshow('screen',  self.screen_img)

            if self.ocr_roi_flag:
                ocr_result = run_inference(self.ocr, self.ocr_roi)
                img_result = vis_result_from_img(self.ocr_roi, ocr_result)
                cv2.imshow('ocr_roi', img_result)
                
                
                
                
                
                
            #! Activate all callbacks
                
            if (cv2.waitKey(15) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                break

            if (cv2.waitKey(15) & 0xFF) == ord('w'):
                print ("Recording clicks")
                cv2.setMouseCallback('screen', self.record_click_on_opencv_interface)
                
            if (cv2.waitKey(15) & 0xFF) == ord('e'):
                cv2.setMouseCallback('screen', self.add_roi_to_list)
                print ("Add roi to list")

            if (cv2.waitKey(15) & 0xFF) == ord('r'):
                print ("Save roi")
                cv2.setMouseCallback('screen',  self.save_roi)

            if (cv2.waitKey(15) & 0xFF) == ord('t'):
                print ("Save roi")
                cv2.setMouseCallback('screen',  self.select_ocr_roi)
                
            
            # if (cv2.waitKey(15) & 0xFF) == ord('e'):
            #     for click in list_of_clicks:
            #         print ("Clicking ", click)
            #         mouse.move(str(click[0]), str(click[1]))
            #         mouse.click(button='left')
            #         time.sleep(0.1)
            #     list_of_clicks= []
                # cv2.setMouseCallback('screen', record_clicks, 0)
                
            # if (cv2.waitKey(15) & 0xFF) == ord('d'):
            #     cv2.setMouseCallback('screen',  lambda *args : None, 0)
            #     print (boxes)
                


                # cv2.destroyAllWindows()
                # break
            
                




if __name__ == '__main__':
    # main()
    test = Test()
    test.acquire_screen()
        