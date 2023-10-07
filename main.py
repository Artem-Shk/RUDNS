import argparse
parser = argparse.ArgumentParser(description='PreView Generator')

parser.add_argument(
    "prompt",
    help="Запрос для генерации",
    type=str
)

parser.add_argument(
    "--count",
    default=1,
    type=int,
    help="Количество генерируемых картинок"
)

args = parser.parse_args()
