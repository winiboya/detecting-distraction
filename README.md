# Computer Vision for Education

This repository contains the code for the paper "A Computer Vision Approach For Assessing Audience Distraction In Educational Settings" by Carolina Zubler and Winiboya Aboyure.

# Getting Started

Create a virtual environment and install the required packages using the following command:

```
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
brew install ffmpeg
```

# Running the code

## Extracting Test Data
```
cd src
python extract_test_data.py --input_dir "small_vids" --frame_output_dir "output_frames" --face_output_dir "output_faces"
```

## Training the Model
