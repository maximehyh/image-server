# image-server

## Depedencies
- Numpy
- OpenCV
- Tested with Python >= 3.9

## Setup

Setup a virtual environment (virtualenv, pyenv, conda...), install depedency and you should be good to go. 
Example:

```python
virtualenv venv-image-server -p python3
source venv-image-server/bin/activate
pip install -r requirements.txt
```

You can also add a .env file at the root of the project in order to set the following variables:

`IMAGE_PATH` - The path where you want the pictures to be saved, defaults to `/assets`
`DEBUG` - Flask debug mode 
`SERVER_PORT` - Server port

## Test

A main file is provided if you want to directly test the image processing functions:

```python
python src/main.py -i assets/image_1.jpeg -o output_folder -f RGB_SPLIT
```

## Server

A small flask based server is also provided in order to test the application behind a web service. 
Using docker simply run `docker-compose build && docker-compose up` and got to `localhost:SERVER_PORT`. 

Here you will be able to provide a filename of a file that you have previously put in the `/assets` folder, as well as the name and format of the desired ouptput. 

After clicking on submit you should then see the rendered result on the web page. 

## Development

Development can be made easily using `docker-compose`. 
In the `docker-compose.yaml` file, uncomment the volume mount `./src:/app/src` (to allow sync with your local files) and set `DEBUG=true` in the `environment` part (flask live debugging mode).

## Known issues

- If you get the following error on MACOS while trying to run main.py: 
```
Traceback (most recent call last):
  File "src/main.py", line 2, in <module>
    from image_process import process
  File "/Users/ac60095/dev/image-server/src/image_process/process.py", line 1, in <module>
    import cv2
  File "/Users/ac60095/dev/image-server/venv-image-server/lib/python3.8/site-packages/cv2/__init__.py", line 5, in <module>
    from .cv2 import *
ImportError: numpy.core.multiarray failed to import
```
Try the following command: `pip install numpy --upgrade --ignore-installed`



