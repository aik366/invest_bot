from t_tech.invest import Client

from config import TOKEN


def main():
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts()

        print(accounts)


if __name__ == "__main__":
    main()
