import os
import cv2
from ModelsArgs import *


# def update_frames_from_directory(splitted_video_to_frames_directory_path, updated_frames_directory_path):
def update_frames_from_directory(update_frames_args):
    w_args = update_frames_args
    temp = get_upscale_model_args(int(w_args['model_index']))
    # temp = upscaling_models_args[w_args['model_index']]
    w_args.update(temp)
    frame_num = 0
    # iterate over files in that directory
    for filename in os.listdir(w_args['input_frames']):
        frame_file_path = os.path.join(w_args['input_frames'], filename)
        # checking if it is a file
        if os.path.isfile(frame_file_path):
            img = cv2.imread(frame_file_path)
            sr = cv2.dnn_superres.DnnSuperResImpl_create()
            path = w_args['model_path']
            sr.readModel(path)
            sr.setModel(w_args['model_index'], w_args['ratio'])  # set the model by passing the value and
                                                                        # the upsampling ratio
            result = sr.upsample(img)  # upscale the input image
            frame_filename = os.path.join(w_args['output_directory'], f"updated_frame_{frame_num:05d}.jpg")
            cv2.imwrite(frame_filename, result)
            frame_num = frame_num + 1
