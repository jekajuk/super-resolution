import os
import cv2
import random


# ---------------------------------      Methods to find necessary args for conversion frames to video
def find_frames_per_second(input_video_path):
    """ Method to find rate of frames in given video file.
        Input: str(video_path)
        Output: float(frames_per_second)"""

    video = cv2.VideoCapture(input_video_path)

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    video.release()
    return fps


def get_random_file_name(directory):
    """ Method to get random file name in given directory

        Input: str(path_to_directory)
        \nOutput: str(random_file_name)"""
    file_names = os.listdir(directory)
    random_file_name = random.choice(file_names)
    return random_file_name


def get_random_frame_size_from_folder(directory):
    """ Method random choice file in given directory and return size of frame.

            Input: str(path_to_directory_with_frames)
            \nOutput: tuple(height, width)"""
    file_name = get_random_file_name(directory)
    frame_file_path = os.path.join(directory, file_name)
    if os.path.isfile(frame_file_path):
        img = cv2.imread(frame_file_path)
        height, width, layers = img.shape
        size = (height, width)
        return size


# ----------------------    Methods for converting frames to video
def convert_frames_from_directory_to_video(args_for_conversion_frames_to_video):
    """ Method convert frames in given directory to video

        Input: dict args_conversion_frames_to_video = {
                                'input_frames': path to directory with frames,
                                'output_directory': path to directory for output video file,
                                'output_file_name': str output_video_file_name,
                                'codec': cv2.VideoWriter_fourcc(*'DIVX'), for more details and option read manual cv2,
                                'fps': rate of frames of output video,
                                'size': tuple ((height, width))  - frame size of output video
                                }
        Output: video file converted from frames in given directory"""
    w_args = args_for_conversion_frames_to_video
    frame_array = []
    for filename in os.listdir(w_args['input_frames']):
        frame_file_path = os.path.join(w_args['input_frames'], filename)
        # checking if it is a file
        if os.path.isfile(frame_file_path):
            img = cv2.imread(frame_file_path)
            height, width, layers = img.shape
            w_args['size'] = (width, height)
            frame_array.append(img)
    output_video_file_path = os.path.join(w_args['output_directory'], w_args['output_file_name'])
    out = cv2.VideoWriter(output_video_file_path, w_args['codec'], w_args['fps'], w_args['size'])
    for i in range(len(frame_array)):
        # writing to an image array
        out.write(frame_array[i])
    out.release()
