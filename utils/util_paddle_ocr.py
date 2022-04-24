from paddleocr import PaddleOCR,draw_ocr
from PIL import Image

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
def run_inference(ocr, frame_path):

    result = ocr.ocr(frame_path, cls=True)
    return result
    # img_path = '/home/alfredo/yugi_project/Easy-Yolo-OCR/image/test1.jpg'
    # for line in result:
        # print(line)

def vis_result_from_path(img_path, result):
    # # draw result
    img = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(img, boxes, txts, scores, font_path='/home/alfredo/yugi_project/PaddleOCR/doc/fonts/simfang.ttf')
    return im_show
    # im_show = Image.fromarray(im_show)
    # im_show.save('result.jpg')
    
def vis_result_from_img(img, result):
    # # draw result
    # image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(img, boxes, txts, scores, font_path='/home/alfredo/yugi_project/PaddleOCR/doc/fonts/simfang.ttf')
    return im_show
    
