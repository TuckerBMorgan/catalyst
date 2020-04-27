# flake8: noqa
import logging
import os

from catalyst.contrib.dl.callbacks.criterion import CriterionAggregatorCallback
from catalyst.contrib.dl.callbacks.cutmix_callback import CutmixCallback
from catalyst.contrib.dl.callbacks.knn import KNNMetricCallback
from catalyst.contrib.dl.callbacks.optimizer import SaveModelGradsCallback
from catalyst.contrib.dl.callbacks.telegram_logger import TelegramLogger
from catalyst.utils.tools import settings

logger = logging.getLogger(__name__)

try:
    import alchemy
    from catalyst.contrib.dl.alchemy import AlchemyLogger
except ImportError as ex:
    if settings.alchemy_logger_required:
        logger.exception(
            "alchemy not available, to install alchemy,"
            " run `pip install alchemy`."
        )
        raise ex

try:
    import neptune
    from catalyst.contrib.dl.neptune import NeptuneLogger
except ImportError as ex:
    if settings.neptune_logger_required:
        logger.exception(
            "neptune not available, to install neptune,"
            " run `pip install neptune-client`."
        )
        raise ex

try:
    import wandb
    from catalyst.contrib.dl.wandb import WandbLogger
except ImportError as ex:
    if settings.wandb_logger_required:
        logger.exception(
            "wandb not available, to install wandb,"
            " run `pip install wandb`."
        )
        raise ex

try:
    import imageio
    import skimage.color
    from catalyst.contrib.dl.cv.inference import InferMaskCallback
except ImportError as ex:
    if settings.cv_required:
        logger.exception(
            "some of catalyst-cv dependencies not available,"
            " to install dependencies, run `pip install catalyst[cv]`."
        )
        raise ex
