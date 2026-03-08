from sys import argv

from libelifoot import get_equipa_data


def main(equipa: str) -> None:
    print(get_equipa_data(equipa))


if __name__ == "__main__":
    main(argv[1])
