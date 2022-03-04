from util_paddle_ocr import *

import os

src_dir = '/home/alfredo/yugi_project/my_project/imgs'
dst_dir = '/home/alfredo/yugi_project/my_project/imgs_result'


ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory


for img_path in os.listdir(src_dir):
    
    print ("Processing: {}".format(img_path))
    
    result = run_inference(ocr, os.path.join(src_dir,img_path))
    img = vis_result_from_path(os.path.join(src_dir,img_path), result)

    im_show = Image.fromarray(img)
    im_show.save(os.path.join(dst_dir,(img_path + '.jpg')))