#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

    if num_args == 0:
        print(".")
