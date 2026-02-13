# image-downscaler
A python script i wrote to downscale pictures to a specific size while keeping the aspect ratio.

## About
The python script downscales either a picture/photo directly or an entire folder/directory depending on the path you have provided.  
Downscaling is done to the specific dimensions you provide to the script (can be either height or width only or it can be both), all the while keeping the aspect ratio to not obtain weird pictures. 

## Requirements
- Have python installed on your machine to be able to execute the script

## Dependencies
The script uses the PILLOW python package for handling images.

## How to Use
- Having python installed on your machine, you can either create a virtual environment and then use the script from within or proceed to make the script accessible from anywhere by installing it using `pipx`.
  - Create the virtual env and then install the dependencies needed:
    ```
    pip install -r requirements.txt
    ```
    Run using:
    ```
    python image-downscaler.py "<path to picture/folder>" -ht 1080 -wt 1920 -o "<path to output folder if you want to specify (optional)>"
    ```
    `-ht` --> height  
    `-wt` --> width  
    `-o`  --> output folder (optional), if not specified, it will create a new folder in the directory you are in when executing the script  
  - Or install using `pipx`
    - Install pipx (if you haven't):
      ```
      pip install pipx
      ```
      then
      ```
      pipx ensurepath
      ```
    - Install the tool (Navigate to the folder where the .py and .toml file are):
      ```
      pipx install .
      ```
    - Run the script with:
      ```
      image-downscaler "<path to picture/folder>" -ht 1080 -wt 1920 -o "<path to output folder if you want to specify (optional)>"
      ```
      `-ht` --> height  
      `-wt` --> width  
      `-o`  --> output folder (optional), if not specified, it will create a new folder in the directory you are in when executing the script  
