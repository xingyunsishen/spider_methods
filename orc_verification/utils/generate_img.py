import os
import shutil
import random
import time
import sys
from captcha.image import ImageCaptcha
# captcha是用于生成验证码图片的库，可以 pip install captcha 来安装它

# 用于生成验证码的字符集
from setting import project_path

CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 字符集的长度
CHAR_SET_LEN = 10
# 验证码的长度，每个验证码由4个数字组成
CAPTCHA_LEN = 4

# 验证码图片的存放路径
CAPTCHA_IMAGE_PATH = project_path + '/captcha/images/'

# 用于模型测试的验证码图片的存放路径，它里面的验证码图片作为测试集
TEST_IMAGE_PATH = project_path + '/captcha/test/'

# 用于模型测试的验证码图片的个数，从生成的验证码图片中取出来放入测试集中
TEST_IMAGE_NUMBER = 50


# 生成验证码图片，4位的十进制数字可以有10000种验证码
def generate_captcha_image(
        char_set=CHAR_SET, char_set_len=CHAR_SET_LEN,
        captcha_img_path=CAPTCHA_IMAGE_PATH):
    k = 0
    total = 1
    for i in range(CAPTCHA_LEN):
        total *= char_set_len

    for i in range(char_set_len):
        for j in range(char_set_len):
            for m in range(char_set_len):
                for n in range(char_set_len):
                    captcha_text = char_set[i] + char_set[j] + char_set[m] + char_set[n]
                    image = ImageCaptcha()

                    file_path = captcha_img_path + captcha_text + '.jpg'

                    image.write(captcha_text, file_path)
                    k += 1
                    sys.stdout.write("\rCreating %d/%d" % (k, total))
                    sys.stdout.flush()


# 从验证码的图片集中取出一部分作为测试集，这些图片不参加训练，只用于模型的测试
def prepare_test_set():
    file_name_list = []
    for filePath in os.listdir(CAPTCHA_IMAGE_PATH):
        captcha_name = filePath.split('/')[-1]
        file_name_list.append(captcha_name)
    random.seed(time.time())
    random.shuffle(file_name_list)
    for i in range(TEST_IMAGE_NUMBER):
        name = file_name_list[i]
        shutil.move(CAPTCHA_IMAGE_PATH + name, TEST_IMAGE_PATH + name)


if __name__ == '__main__':
    generate_captcha_image(CHAR_SET, CHAR_SET_LEN, CAPTCHA_IMAGE_PATH)
    prepare_test_set()
    sys.stdout.write("\nFinished")
    sys.stdout.flush()
