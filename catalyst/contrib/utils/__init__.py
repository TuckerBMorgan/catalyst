# flake8: noqa
# isort:skip_file

import logging
import os

logger = logging.getLogger(__name__)

from catalyst.utils.tools import settings
from catalyst.contrib.utils.argparse import boolean_flag
from catalyst.contrib.utils.compression import (
    pack,
    pack_if_needed,
    unpack,
    unpack_if_needed,
)
from catalyst.contrib.utils.confusion_matrix import (
    calculate_tp_fp_fn,
    calculate_confusion_matrix_from_arrays,
    calculate_confusion_matrix_from_tensors,
)
from catalyst.contrib.utils.dataset import (
    create_dataset,
    split_dataset_train_test,
    create_dataframe,
)
from catalyst.contrib.utils.misc import (
    args_are_not_none,
    make_tuple,
    pairwise,
)
from catalyst.contrib.utils.pandas import (
    dataframe_to_list,
    folds_to_list,
    split_dataframe_train_test,
    split_dataframe_on_folds,
    split_dataframe_on_stratified_folds,
    split_dataframe_on_column_folds,
    map_dataframe,
    separate_tags,
    get_dataset_labeling,
    split_dataframe,
    merge_multiple_fold_csv,
    read_multiple_dataframes,
    read_csv_data,
    balance_classes,
)
from catalyst.contrib.utils.parallel import (
    parallel_imap,
    tqdm_parallel_imap,
    get_pool,
)
from catalyst.contrib.utils.serialization import deserialize, serialize

try:
    from catalyst.contrib.utils.image import (
        has_image_extension,
        imread,
        imwrite,
        imsave,
        mask_to_overlay_image,
        mimread,
        mimwrite_with_meta,
        tensor_from_rgb_image,
        tensor_to_ndimage,
    )
    from catalyst.contrib.utils.visualization import (
        plot_confusion_matrix,
        render_figure_to_tensor,
    )
except ImportError as ex:
    if settings.cv_required:
        logger.exception(
            "some of catalyst-cv dependencies not available,"
            " to install dependencies, run `pip install catalyst[cv]`."
        )
        raise ex

try:
    from catalyst.contrib.utils.plotly import (
        plot_tensorboard_log,
        plot_metrics,
    )
except ImportError as ex:
    if os.environ.get("USE_PLOTLY", "0") == "1":
        logger.warning(
            "plotly not available, to install plotly,"
            " run `pip install plotly`."
        )
        raise ex

try:
    from catalyst.contrib.utils.text import tokenize_text, process_bert_output
except ImportError as ex:
    if settings.nlp_required:
        logger.exception(
            "some of catalyst-nlp dependencies not available,"
            " to install dependencies, run `pip install catalyst[nlp]`."
        )
        raise ex
