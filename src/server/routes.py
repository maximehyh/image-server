import uuid
from image_process import process
import os
from server.config import INPUT_FOLDER, OUTPUT_FOLDER, PATH_FROM_PROC_MOD
import logging
from flask import Flask, render_template, request
from flask import render_template_string
from .utils import list_folder


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def run():
        try:
            return render_template('index.html')

        except Exception as e:
            logging.error('Unexpected error: %s' % (e))
            return render_template_string('Error: {{ error }}', error=e)

    @app.route('/result', methods=['POST'])
    def result():
        try:
            input_name = request.form['inputName']
            image_operation = request.form['processSelection']
            input_path: str = os.path.join(INPUT_FOLDER, input_name)

            # Using a uuid to make sure images are created in
            # a unique folder
            folder_name: str = str(uuid.uuid1())
            # Providing path relative to 'image_process' module
            output_folder: str = os.path.join(
                PATH_FROM_PROC_MOD, OUTPUT_FOLDER, folder_name)
            os.makedirs(output_folder)

            if not os.path.exists(input_path):
                raise Exception(
                    'Path to file does not exist, please check input')
            process.function_dict[image_operation](
                input_path, output_folder)

            images = list_folder(output_folder)
            # Providing path relative to flask app
            # TODO: use absolute path to make path handling clearer
            image_paths = [os.path.join(OUTPUT_FOLDER, folder_name, name)
                           for name in images]

            return render_template('result.html', image_paths=image_paths)

        except Exception as e:
            logging.error('Error while trying to display result: %s' % (e))
            return render_template_string("""Error, when trying to display
                image: {{ error }}""", error=e)

    return app
