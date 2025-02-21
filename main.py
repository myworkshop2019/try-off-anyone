from src.test_vton import test_vton
from src.inference import test_image
import argparse


def terminal_args():
    parser = argparse.ArgumentParser(description="Simple example of a training script.")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--inference--url="https://www.quiksilver.com/cdn/shop/products/aqbwr03064_quiksilver_2Cw_wbb0_frt1.jpg?v=1716587633&width=825"
", action="store_true")
    return parser.parse_known_args()[0]


def main():
    args = terminal_args()
    if args.test:
        test_vton()
    elif args.inference:
        test_image()


if __name__ == '__main__':
    main()
