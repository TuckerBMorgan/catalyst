from argparse import ArgumentParser, RawTextHelpFormatter
from collections import OrderedDict
import logging

from catalyst.contrib.scripts import find_thresholds
from catalyst.utils.tools import settings

logger = logging.getLogger(__name__)

COMMANDS = OrderedDict([("find-thresholds", find_thresholds)])

try:
    import nmslib  # noqa: F401
    from catalyst.contrib.scripts import check_index_model, create_index_model

    COMMANDS["check-index-model"] = check_index_model
    COMMANDS["create-index-model"] = create_index_model
except ImportError as ex:
    if settings.ml_required:
        logger.exception(
            "some of catalyst-ml dependencies not available,"
            " to install dependencies, run `pip install catalyst[ml]`."
        )
        raise ex


def build_parser() -> ArgumentParser:
    """@TODO: Docs. Contribution is welcome."""
    parser = ArgumentParser(
        "catalyst-contrib", formatter_class=RawTextHelpFormatter
    )
    all_commands = ", \n".join(map(lambda x: f"    {x}", COMMANDS.keys()))

    subparsers = parser.add_subparsers(
        metavar="{command}",
        dest="command",
        help=f"available commands: \n{all_commands}",
    )
    subparsers.required = True

    for key, value in COMMANDS.items():
        value.build_args(subparsers.add_parser(key))

    return parser


def main():
    """@TODO: Docs. Contribution is welcome."""
    parser = build_parser()

    args, uargs = parser.parse_known_args()

    COMMANDS[args.command].main(args, uargs)


if __name__ == "__main__":
    main()
