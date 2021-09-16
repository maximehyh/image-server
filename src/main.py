import argparse
from image_process import process
import os
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image",
                        type=str,
                        help="path to the input image",
                        required=True)
    parser.add_argument("-o", "--output",
                        type=str,
                        help="path to the output image",
                        required=True)

    parser.add_argument("-f", "--function",
                        type=str,
                        help="function to apply on image: RGB_SPLIT",
                        required=True)

    args: argparse.Namespace = parser.parse_args()
    image_path: str = args.image
    output_folder: str = args.output
    image_operation: str = args.function

    try:
        if not os.path.exists(image_path):
            raise Exception('Path to file does not exist, please check input')
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        process.function_dict[image_operation](
            image_path, output_folder)

    except Exception as e:
        logging.error('Error: %s' % (e))
