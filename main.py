# @Time    : 18-4-24 下午4:52
# @File    : main.py
# @Software: PyCharm

import time
from datetime import datetime
import cv2
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', type=str,
                        help='输入路径')
    parser.add_argument('output_dir', type=str,
                        help='输出路径')
    args = parser.parse_args()
    folder_name = args.input_dir
    for root, dirs, files in os.walk(folder_name, topdown=False):
        for name in files:
            video_name = os.path.join(root, name)
            # 填写视频的绝对路径
            vidcap = cv2.VideoCapture(video_name)
            success, image = vidcap.read()
            start_time = time.time()
            #
            while success:
                cv2.imshow('', image)
                end_time = time.time()
                file_name = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f')
                # 每隔三秒截屏
                if 3 == int(end_time - start_time):
                    start_time = end_time
                    # 保存JGP  的绝对路径
                    cv2.imwrite(args.output_dir+'/'+ file_name + ".jpg", image)  # save frame as JPEG file
                    print('writing :{}'.format(file_name + ".jpg"))
                success, image = vidcap.read()
                if cv2.waitKey(10) == 27:  # exit if Escape is hit
                    break
