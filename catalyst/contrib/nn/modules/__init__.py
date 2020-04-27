# flake8: noqa
from torch.nn.modules import *

from catalyst.contrib.nn.modules.common import Flatten, Lambda, Normalize
from catalyst.contrib.nn.modules.lama import (
    LamaPooling,
    TemporalAttentionPooling,
    TemporalConcatPooling,
)
from catalyst.contrib.nn.modules.pooling import (
    GlobalAttnPool2d,
    GlobalAvgAttnPool2d,
    GlobalAvgPool2d,
    GlobalConcatAttnPool2d,
    GlobalConcatPool2d,
    GlobalMaxAttnPool2d,
    GlobalMaxPool2d,
)
from catalyst.contrib.nn.modules.rms_norm import RMSNorm
