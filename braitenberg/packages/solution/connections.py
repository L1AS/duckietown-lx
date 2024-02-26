from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    height = int(res.shape[0] / 2)
    width = int(res.shape[1] / 2)
    for i in range(height + 50):
        res[i + height - 50, width - int(width / (height + 50) * i) : width] = 1
        res[i + height - 50, width : width + int(width / (height + 50) * i)] = -1
    res[height - 10:, width - 30: width + 30] = 1


    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    height = int(res.shape[0] / 2)
    width = int(res.shape[1] / 2)
    for i in range(height + 50):
        res[i + height - 50, width - int(width / (height + 50) * i) : width] = -1
        res[i + height - 50, width : width + int(width / (height + 50) * i)] = 1
    res[height - 10:, width - 30: width + 30] = -1

    return res
