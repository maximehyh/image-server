
import cv2
import logging
import os
# import numpy as np


def process_image(image_path: str, output_path: str) -> None:
    if not os.path.exists(image_path):
        raise Exception('Path to file does not exist, please check input')

    image = cv2.imread(image_path)
    (B, G, R) = cv2.split(image)
    merged = cv2.merge([B, G, R])
    cv2.imwrite(output_path, merged)
    logging.info("Image")
