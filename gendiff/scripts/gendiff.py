from gendiff.cli import pars_args
from gendiff.gendiff import gendiff


def main():
    args = pars_args()
    diff = gendiff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
