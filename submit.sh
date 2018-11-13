#!/bin/bash

python submission.py --maxdisp 192 \
                   --model stackhourglass \
                   --KITTI 2015 \
                   --datapath ./data_scene_flow/custom-testing/ \
                   --loadmodel ./pretrained/pretrained_model_KITTI2015.tar

