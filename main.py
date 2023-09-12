from moviepy.editor import VideoFileClip
import os

newFileType = input("Please insert the type you want to convert \n : ").replace('.', '')
folder_path = './video'
# Loop through the list of files
for filename in os.listdir(folder_path):
    try:
        # Print the filename
        nFileName = filename[:filename.rfind('.')] + '.' + newFileType
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join('./output', nFileName)

        # Load the video clip
        video_clip = VideoFileClip(input_path)

        # Convert and write the video clip as MP4
        video_clip.write_videofile(output_path , codec='libx264')

        # Close the video clip
        video_clip.close()

        # remove the old file 
        os.remove(input_path)
    except FileNotFoundError:
        print(f"{filename} does not exist.")
    except Exception as e:
        print(f"An error occurred : {e}")