import argparse

from tools import accounting


def main(args):
    # input = args.input
    item1 = accounting.Accounting()
    print(item1.val)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("--input", type=str)
    args = parser.parse_args()
    main(args)
