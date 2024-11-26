import cv2
import os

class VideoFrameExtraction:
    """
    A class for extracting frames from a video file.
    
    Attributes:
        output_dir (str): The directory where extracted frames will be saved.
        
    Methods:
        __init__(output_dir):
            Initializes the VideoFrameExtraction object with the given output directory and number of frames to extract.
        extract_frames(self, video_path, file_prefix):
            Extracts frames from the video file and saves them to the output directory.
    """
    
    def __init__(self, output_dir):
        """
        Initializes the VideoFrameExtraction object with the given output directory.
        
        Args:
            output_dir (str): The directory where extracted frames will be saved.
        """
        self.output_dir = output_dir
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def extract_frames(self, video_path, file_prefix=""):
        """
        Extracts frames from the video file and saves them to the output directory.
        
        Args:
            video_path (str): The path to the video file.
            file_prefix (str): The prefix to use for the extracted frame filenames.
        """
        
        # verify video path
        if not os.path.exists(video_path):
            print(f"Video file not found: {video_path}")
            return 0, []
        
        video = cv2.VideoCapture(video_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        formatted_duration = self._format_time(duration * 1000)
        
        saved_frame_count = 0
        timestamps = []
        interval = 10  # 10 seconds interval

        # Extract frame at each 10-second interval
        current_time = 0
        while current_time <= duration:
            # Set video position to the exact frame we want
            frame_position = int(current_time * fps)
            video.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
            
            ret, frame = video.read()
            if not ret:
                break
                
            formatted_time = f"{self._format_time(current_time * 1000)} / {formatted_duration}"
            timestamps.append(formatted_time)
            
            if file_prefix:
                frame_filename = os.path.join(self.output_dir, f"{file_prefix}_{saved_frame_count}.jpg")
            else: 
                frame_filename = os.path.join(self.output_dir, f"{self._format_time(current_time * 1000)}.jpg")
            
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1
            
            # Move to next 10-second interval
            current_time += interval
            
        video.release()
        cv2.destroyAllWindows()
        return saved_frame_count, timestamps
    
    def _format_time(self, milliseconds):
        seconds = int(milliseconds // 1000)
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02}:{seconds:02}"
        
