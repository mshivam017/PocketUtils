import cv2
import os

def video_to_images(video_path, output_folder, interval_sec):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval_frames = int(fps * interval_sec)
    
    # Read and process each frame at specified interval
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame as an image at specified intervals
        if frame_count % interval_frames == 0:
            frame_name = f"frame_{frame_count:04d}.jpg"  # Customize the naming convention as desired
            frame_path = os.path.join(output_folder, frame_name)
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video capture object and close the output folder
    cap.release()
    cv2.destroyAllWindows()

    print(f"Successfully converted video to images with {interval_sec} sec interval.")

if __name__ == "__main__":
    video_file = "input_video.mp4"  # Provide path to your input video file
    output_folder = "output_images_interval_10s"  # Output folder where images will be saved
    interval_seconds = 10  # Interval in seconds
    
    video_to_images(video_file, output_folder, interval_seconds)
