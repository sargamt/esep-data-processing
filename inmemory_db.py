class InMemoryDB:

    def __init__(self):
        self.accounts = {}
        self.inTransaction = False
        self.current_transaction = {}
    
    def get(self, key: str) -> int:
        if key in self.accounts:
            return self.accounts[key]
        else:
            return None

    def put(self, key: str, val: int):
        if not self.inTransaction:
            raise Exception("A transaction is not in progress.")
        else:
            self.current_transaction[key] = val

    def begin_transaction(self):
        pass

    def commit(self):
        if self.current_transaction:
            for key, val in self.current_transaction.items():
                self.accounts[key] = val
            self.current_transaction = {}
        pass

    def rollback(self):
        pass


def main():
    imdb = InMemoryDB

    imdb.get("A")

    pass


main()