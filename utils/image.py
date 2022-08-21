from pathlib import Path

import cv2 as cv
import numpy as np
from PIL import Image


def read_image_from_path(image_path: Path) -> np.ndarray:
    """Reads image and returns numpy ndarray in shape of HWC.

    Args:
        image_path (Path): Path of the image in pathlib.Path type.

    Returns:
        np.ndarray: Returns the image in numpy.ndarray type with the shape of HWC (height, width, channel).
    """
    image = cv.imread(str(image_path))
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image


def crop_image_from_xyxy(
    image: np.ndarray,
    x_left: int,
    y_top: int,
    x_right: int,
    y_bottom: int,
) -> np.ndarray:
    """Crops input image to the destination coordination.
    The destination coordination is xmin, ymin, xmax, ymax (xyxy).

    Args:
        image (np.ndarray): The image as an numpy.ndarray.
        x_left (int): Minimum of crop destination in X dimension (dim 1).
        y_top (int): Minimum of crop destination in Y dimension (dim 0).
        x_right (int): Maximum of crop destination in X dimension (dim 1).
        y_bottom (int): Maximum of crop destination in Y dimension (dim 0).

    Returns:
        np.ndarray: Returns the crop part of the image.
    """
    axis_0_start = y_top
    axis_0_stop = y_bottom
    axis_1_start = x_left
    axis_1_stop = x_right
    return image[axis_0_start:axis_0_stop, axis_1_start:axis_1_stop, :]


def crop_image_from_xywh(
    image: np.ndarray,
    x_left: int,
    y_top: int,
    width: int,
    height: int,
) -> np.ndarray:
    """Crops input image to the destination coordinates.
    The destination coordination is xmin, ymin, width, higth (xywh).
    Args:
        image (np.ndarray): The image as an numpy.ndarray.
        x_left (int): Minimum of crop destination in X dimension (dim 1).
        y_top (int): Minimum of crop destination in Y dimension (dim 0).
        width (int): Width of the crop part (dim 1).
        height (int): height of the crop part (dim 0).

    Returns:
        np.ndarray: Returns the crop part of the image.
    """
    axis_0_start = y_top
    axis_0_stop = y_top + height
    axis_1_start = x_left
    axis_1_stop = x_left + width
    return image[axis_0_start:axis_0_stop, axis_1_start:axis_1_stop, :]


def crop_image_from_xcycwh(
    image: np.ndarray,
    x_center: int,
    y_center: int,
    width: int,
    height: int,
) -> np.ndarray:
    """Crops input image to the destination coordinates.
    The destination coordination is x_center, ymin, width, higth (xywh).

    Args:
        image (np.ndarray): The image as an numpy.ndarray.
        x_center (int): Dim 0 coordination of the center of the crop part.
        y_center (int): Dim 1 coordination of the center of the crop part.
        width (int): Width of the crop part (dim 1).
        height (int): height of the crop part (dim 0).

    Returns:
        np.ndarray: Returns the crop part of the image.
    """
    axis_0_start = y_center - height // 2
    axis_0_stop = y_center + height // 2
    axis_1_start = x_center - width // 2
    axis_1_stop = x_center + width // 2
    return image[axis_0_start:axis_0_stop, axis_1_start:axis_1_stop, :]


def save_image_by_suffix(
    image: np.ndarray,
    image_save_path: Path,
    image_name: str,
    image_suffix: str,
) -> None:
    """Saves image in the given path with the given suffix.

    Args:
        image (np.ndarray): The image in numpy.ndarray type.
        image_save_path (Path): The destination path of the image without ending slash (/).
        image_name (str): The name of the image without suffix.
        image_suffix (str): The suffix of the target image.
    """

    image: Image.Image = Image.fromarray(image)
    image_name_with_suffix = f"{image_name}." + image_suffix
    save_path = image_save_path / image_name_with_suffix
    image.save(save_path)
