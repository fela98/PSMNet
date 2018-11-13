import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import argparse

class OpenCVSM():
    def compute_disparity(self, imgL, imgR):

        window_size = 3

        left_matcher = cv2.StereoSGBM.create(
            preFilterCap=63,
            blockSize=window_size,
            P1=window_size*window_size * 4,
            P2=window_size*window_size * 32,
            minDisparity=0,
            numDisparities=128,
            uniquenessRatio=10,
            speckleWindowSize=100,
            speckleRange=32,
            mode=1
        )

        right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)

        wls_filter = cv2.ximgproc.createDisparityWLSFilter(left_matcher)

        wls_filter.setLambda(7000)
        wls_filter.setSigmaColor(1)

        disp = dispL = np.int16(left_matcher.compute(imgL, imgR))
        dispR = np.int16(right_matcher.compute(imgR, imgL))

        filtered_disp = wls_filter.filter(dispL, imgL, None, dispR)

        disp = filtered_disp

        disp[disp < 0] = 0

        return disp

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='OpenCV-Disparity')

    parser.add_argument('--KITTI', default='2015',
                    help='KITTI version')
    parser.add_argument('--datapath', default='/media/jiaren/ImageNet/data_scene_flow_2015/testing/',
                        help='select model')

    args = parser.parse_args()

    if args.KITTI == '2015':
        from dataloader import KITTI_submission_loader as DA
    else:
        from dataloader import KITTI_submission_loader2012 as DA  


    test_left_img, test_right_img = DA.dataloader(args.datapath)

    for i in range(len(test_left_img)):
        filename = test_left_img[i].split('/')[-1]

        imgL = cv2.imread(test_left_img[i], 0)
        imgR = cv2.imread(test_right_img[i], 0)

        start_time = time.time()

        stereo_matcher = OpenCVSM()
        disp = stereo_matcher.compute_disparity(imgL, imgR)

        print(filename + ': time = %.2f' %(time.time() - start_time))

        disp = (disp*16).astype('uint16')

        cv2.imwrite(filename, disp)