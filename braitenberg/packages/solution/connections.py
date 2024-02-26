from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    height = int(res.shape[0] / 2)
    width = int(res.shape[1] / 2)
    for i in range(height + 100):
        res[i + height - 100, width - int(width / (height + 100) * i) : width] = 1
        res[i + height - 100, width : width + int(width / (height + 100) * i)] = -1
    # res[:, 0 : res.shape[1] // 2] = 1
    # res[:, res.shape[1] // 2 : res.shape[1]] = -1
    # res[height - 80 - 40: res.shape[0] // 2 - 40, res.shape[1] // 2 - 80: res.shape[1] // 2 + 80] = 0
    res[height - 60:, width - 30: width + 30] = 1


    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.zeros(shape=shape, dtype="float32")
    height = int(res.shape[0] / 2)
    width = int(res.shape[1] / 2)
    for i in range(height + 100):
        res[i + height - 100, width - int(width / (height + 100) * i) : width] = -1
        res[i + height - 100, width : width + int(width / (height + 100) * i)] = 1
    res[height - 60:, width - 30: width + 30] = -1
    # res[:, 0 : res.shape[1] // 2] = -1
    # res[:, res.shape[1] // 2 : res.shape[1]] = 1
    # res[res.shape[0] // 2 - 80 - 40: res.shape[0] // 2, res.shape[1] // 2 - 80: res.shape[1] // 2 + 80] = 0

    return res
