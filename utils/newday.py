from argparse import ArgumentParser
from pathlib import Path
import shutil

parser = ArgumentParser()
parser.add_argument('year')
parser.add_argument('day')
args = parser.parse_args()

root = Path(__file__).parent.parent
template = root.joinpath('utils/_newday')
newday = root.joinpath(f'{args.year}/day{args.day}')

if not newday.exists():
  newday.mkdir(parents=True)
  shutil.copy2(template.joinpath('day{n}.py'), newday.joinpath(f'day{args.day}.py'))
  shutil.copy2(template.joinpath('input.txt'), newday)
