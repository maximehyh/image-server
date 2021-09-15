import argparse
from image_process import process


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

    args: argparse.Namespace = parser.parse_args()
    image_path: str = args.image
    output_name: str = args.output

    process.process_image(image_path, output_name)
