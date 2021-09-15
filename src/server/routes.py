from image_process import process
import os
from server.config import INPUT_FOLDER, OUTPUT_FOLDER, PATH_FROM_PROC_MOD
import logging
from flask import Flask, render_template, request, send_from_directory
from flask import render_template_string


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
            output_name = request.form['outputName']

            input_path: str = os.path.join(INPUT_FOLDER, input_name)
            # Providing path relative to 'image_process' module
            output_path: str = os.path.join(
                PATH_FROM_PROC_MOD, OUTPUT_FOLDER, output_name)

            process.process_image(input_path, output_path)
            return send_from_directory(OUTPUT_FOLDER, output_name)

        except Exception as e:
            logging.error('Error while trying to display result: %s' % (e))
            return render_template_string("""Error, when trying to display
                image: {{ error }}""", error=e)

    return app
