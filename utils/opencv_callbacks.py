import cv2

def add_roi_to_list(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Start Mouse Position: '+str(x)+', '+str(y))
         sbox = [x, y]
         params.x1 = x
         params.y1 = y

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
        print ("saving bb_{}{}".format([params.y1, params.x1], [params.y1 + params.h, params.x1 + params.w]))
        params.img = params.img_[params.y1 : params.y1 + params.h , params.x1 : params.x1 + params.w ,0:3]
        cv2.imwrite('bb_{}{}.png'.format([params.x1, params.y1],  [params.y1 + params.h, params.x1 + params.w]),params.img)


def record_clicks(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
         print ('Record_click: '+str(x)+', '+str(y))
         sbox = [x, y]
         list_of_clicks.append(sbox)
