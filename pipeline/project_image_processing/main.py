from extract import Payload
from transform import Mapper
from load import Store


def main():
    payload = Payload()

    # Step 1: download (MUST be sequential)
    payload.get()

    # Step 2: unzip (MUST be sequential)
    payload.unzip()

    # Step 3: transform
    mapper = Mapper()
    mapper.run()

    # Step 4: load
    store = Store()
    store.run()


if __name__ == "__main__":
    main()