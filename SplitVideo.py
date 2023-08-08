import cv2
import os


# ---------------------------    Option 1
# def split_video_to_frames_1(video_path, output_directory):
def split_video_to_frames_1(split_video_args):
    # Open the video file
    video_capture = cv2.VideoCapture(split_video_args['input_video'])

    # Get the total number of frames in the video
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(split_video_args['output_directory']):
        os.makedirs(split_video_args['output_directory'])

    # Loop through each frame and save it as an image
    for frame_num in range(total_frames):
        # Read the next frame
        ret, frame = video_capture.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        # Save the frame as an image
        frame_filename = os.path.join(split_video_args['output_directory'], f"frame_{frame_num:05d}.jpg")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    video_capture.release()


# ---------------------------    Option 2
# def split_video_to_frames_2(video_path, output_directory):
def split_video_to_frames_2(split_video_args):
    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(split_video_args['output_directory']):
        os.makedirs(split_video_args['output_directory'])

    capture = cv2.VideoCapture(split_video_args['input_video'])
    frame_num = 0
    while True:
        success, frame = capture.read()
        if success:
            frame_filename = os.path.join(split_video_args['output_directory'], f"frame_{frame_num:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
        else:
            break

        frame_num = frame_num + 1
    capture.release()
