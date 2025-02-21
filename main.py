from src.test_vton import test_vton
from src.inference import test_image
import argparse


def terminal_args():
    parser = argparse.ArgumentParser(description="Simple example of a training script.")
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--inference--url="https://cdn11.bigcommerce.com/s-405b0/images/stencil/590x590/products/97/20409/8000-gildan-tee-t-shirt.ca-model__66081.1724276210.jpg"
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
