from libelifoot import get_available_providers


def main() -> None:
    providers = get_available_providers()

    print(f"available providers: {', '.join(providers)}")


if __name__ == "__main__":
    main()
