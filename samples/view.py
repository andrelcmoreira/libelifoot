from sys import argv

from libelifoot import view_equipa


def main(equipa: str) -> None:
    print(view_equipa(equipa))


if __name__ == "__main__":
    main(argv[1])
