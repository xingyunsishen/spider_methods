import re
import numpy as np
from PIL import Image
import tensorflow as tf
from setting import project_path
from utils.tools import get_arr_num

CAPTCHA_LEN = 4

MODEL_SAVE_PATH = project_path + '/captcha/models/'
TEST_IMAGE_PATH = project_path + '/captcha/test/'


class TenOrc(object):
    """ 这个类的作用是用来运行识别图片验证码的模型
    """

    def __init__(self):
        pass

    @staticmethod
    def get_image_data_and_name(file_path):
        """ 这个函数的作用是用来代开一张图片

        :param file_path:输入的是文件的路径
        :return:
        """
        file_name = file_path.split('/')[-1]
        img = Image.open(file_path)
        # 转为灰度图
        img = img.convert("L")
        image_array = np.array(img)
        image_data = image_array.flatten() / 255
        image_name = file_name[0:CAPTCHA_LEN]
        return image_data, image_name

    def orc_start(self, file_path):
        """ 这个函数是这个类的主函数
        :return:
        """

        # 加载graph
        saver = tf.train.import_meta_graph(MODEL_SAVE_PATH + "crack_captcha.model-0.meta")
        graph = tf.get_default_graph()
        # 从graph取得 tensor，他们的name是在构建graph时定义的(查看上面第2步里的代码)
        input_holder = graph.get_tensor_by_name("data-input:0")
        keep_prob_holder = graph.get_tensor_by_name("keep-prob:0")
        predict_max_idx = graph.get_tensor_by_name("predict_max_idx:0")
        with tf.Session() as sess:
            saver.restore(sess, tf.train.latest_checkpoint(MODEL_SAVE_PATH))

            img_data, img_name = self.get_image_data_and_name(file_path)
            predict = sess.run(predict_max_idx, feed_dict={
                input_holder: [img_data], keep_prob_holder: 1.0
            })

            return str(get_arr_num(
                re.findall('\[(.*)\]', str(np.squeeze(predict)))
            )).replace(' ', '')
