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

```python
python src/main.py -i assets/image_1.jpeg -o test.jpeg
```


## Server

A small flask based server is also provided in order to test the application behind a web service. 
Using docker simply run `docker-compose up` and got to `localhost:SERVER_PORT`. 

Here you will be able to provide a filename of a file that you have previously put in the `/assets` folder, as well as the name and format of the desired ouptput. 

After clicking on submit you should then see the rendered result on the web page. 

## Development

Development can be made easily using `docker-compose`. 
In the `docker-compose.yaml` file, uncomment the volume mount `./src:/app/src` (to allow sync with your local files) and set `DEBUG=true` in the `environment` part (flask live debugging mode).




