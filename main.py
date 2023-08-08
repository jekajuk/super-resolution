from SplitVideo import *
from VideoUpdater import *
from UpscaleFrame import *
import cv2


# -----------------------------     Input path's arguments
# Path to initial video file
path_input_video = r"Input Video/sample_1.mp4"
# Path to folder for splitted tp frames video
path_splitted_frames_directory = r"Splitted frames"
# Path to updated Frames
path_updated_frames_directory = r"Updated frames"
# Path to final video file
path_output_video_file_directory = r"Final Video"
output_video_file_name = 'output_video_2.avi'


# --------------        1. Split video to frames    --------------
# --------------        Arguments for splitting video to frames
args_split_video = {
    'input_video': path_input_video,
    'output_directory': path_splitted_frames_directory}
# ----------------------------- Split video to frames
# Option code 1
# split_video_to_frames_1(split_video_args)

# Option code 2
split_video_to_frames_2(args_split_video)


# --------------        2. Upscale frames   --------------
# --------------        Arguments for updating resolution of frames
args_update_frames = {
    'input_frames': path_splitted_frames_directory,
    'output_directory': path_updated_frames_directory,
    'model_index': 1}   # for details see  ModelsArgs

# ----------------------------- Updating frames in directory
update_frames_from_directory(args_update_frames)


# --------------        3. Conversion frames to video   --------------
# --------------        Arguments for conversion frames to video

codec = cv2.VideoWriter_fourcc(*'DIVX')
frames_per_second = find_frames_per_second(path_input_video)
frame_size = get_random_frame_size_from_folder(path_updated_frames_directory)


args_conversion_frames_to_video = {
    'input_frames': path_updated_frames_directory,
    'output_directory': path_output_video_file_directory,
    'output_file_name': output_video_file_name,
    'codec': codec,
    'fps': frames_per_second,
    'size': frame_size}

# ----------------------------- Convert frames to video
convert_frames_from_directory_to_video(args_conversion_frames_to_video)
