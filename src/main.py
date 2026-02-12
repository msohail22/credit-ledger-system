from .db import init_db

def main():
    init_db()
    print("APP Started")


if __name__ == "__main__":
    main()