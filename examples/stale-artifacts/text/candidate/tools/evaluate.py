"""Source illustration of the current evaluator entry point."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", required=True)
    args = parser.parse_args()
    print(args.split)


if __name__ == "__main__":
    main()
