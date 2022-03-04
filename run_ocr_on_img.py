from paddleocr import PaddleOCR,draw_ocr
from PIL import Image
import argparse
# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
def run_inference(frame_path):

    ocr = PaddleOCR(use_angle_cls=True, lang='en') # need to run only once to download and load model into memory
    result = ocr.ocr(frame_path, cls=True)
    return result
    # img_path = '/home/alfredo/yugi_project/Easy-Yolo-OCR/image/test1.jpg'
    # for line in result:
        # print(line)

def vis_result(img_path, result):
    # # draw result
    img = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(img, boxes, txts, scores, font_path='/home/alfredo/yugi_project/PaddleOCR/doc/fonts/simfang.ttf')
    return im_show
    # im_show = Image.fromarray(im_show)
    # im_show.save('result.jpg')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--img", type = str, default = '/home/alfredo/yugi_project/my_project/bb_[21, 170][519, 983].png')
    
    args = parser.parse_args()
    
    
    res = run_inference(args.img)
    im_show = vis_result(args.img, res)
    im_show = Image.fromarray(im_show)
    im_show.show()
