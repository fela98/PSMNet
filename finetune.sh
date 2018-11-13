#!/bin/bash

python finetune.py --maxdisp 192 \
                   --model stackhourglass \
                   --datatype 2015 \
                   --datapath ./data_scene_flow/training/ \
                   --epochs 30 \
                   --loadmodel ./pretrained/pretrained_sceneflow.tar \
                   --savemodel ./trained/KITTI_2015/

