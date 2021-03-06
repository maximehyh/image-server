from PIL import Image
import logging
import os
import numpy as np
import uuid
from typing import List


def split_pix(image_path: str,
              output_folder: str,
              M: int = 128,
              N: int = 128) -> None:
    im = np.array(Image.open(image_path))

    tiles = [im[x:x+M, y:y+N]
             for x in range(0, im.shape[0], M)
             for y in range(0, im.shape[1], N)]

    for index, image in enumerate(tiles, start=1):
        save_image(index, output_folder, image, "jpeg")

    return


def split_image_half(image_path: str, output_folder: str) -> None:
    image = np.array(Image.open(image_path))

    split_images = split_image(image)

    for index, image in enumerate(split_images, start=1):
        save_image(index, output_folder, image, "jpeg")

    return


def split_rgb(image_path: str, output_folder: str) -> None:
    image: np.ndarray = np.array(Image.open(image_path))
    (B, G, R) = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    named_axis: dict = {"blue": B, "green": G, "red": R}

    for axis in named_axis.keys():
        save_image(axis, output_folder, named_axis[axis], "jpeg")


def rotate(image_path: str, output_folder: str):
    im = np.array(Image.open(image_path))

    rotated = np.rot90(im)
    save_image("rotated", output_folder, rotated, "png")


def save_pics(image_path: str, output_folder: str):
    im = np.array(Image.open(image_path))
    for i in range(0, 10):
        name = "frame_0%s" % i
        save_image(name, output_folder, im, "png")


def calculate(image_path: str, output_folder: str):
    A = np.matrix([[10, -9, -12], [7, -12, 11]])
    B = np.matrix([[7, 3], [12, 25], [0, 36]])
    C = np.matrix([[2, 2], [-6, -7]])

    D = np.dot(A, B)
    E = np.dot(A, B, C)
    F = np.dot(np.transpose(A), C)
    print("D =", D)
    print("E =", E)
    print("F =", F)


def save_image(name: str,
               output_folder: str,
               image: np.ndarray,
               extension: str):
    path: str = os.path.join(output_folder, "%s_%s.%s" %
                             (name, str(uuid.uuid1())[:8], extension))
    output_image = Image.fromarray(image)
    output_image.save(path)
    logging.info("Image created at %s", path)


def split_image(image: np.ndarray) -> dict:
    xs = image.shape[0]//2
    ys = image.shape[1]//2

    split_images: List = [image[0:xs, 0:ys],
                          image[0:xs, ys:],
                          image[xs:, 0:ys],
                          image[xs:, ys:]]

    return split_images


function_dict = {
    "RGB_SPLIT": split_rgb,
    "SPACE_SPLIT": split_image_half,
    "SPLIT_PIX": split_pix,
    "ROTATE": rotate,
    # main.py only
    "SAVE_PICS": save_pics,
    "CALCULATE": calculate
}
