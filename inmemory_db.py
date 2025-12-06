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
        self.inTransaction = True

    def commit(self):
        if not self.inTransaction:
            raise Exception("No open transaction.")
        else:
            if self.current_transaction:
                for key, val in self.current_transaction.items():
                    self.accounts[key] = val
                self.current_transaction = {}
            self.inTransaction = False

    def rollback(self):
        if not self.inTransaction:
            raise Exception("No ongoing transaction.")
        else:
            self.current_transaction = {}


def main():
    imdb = InMemoryDB

    imdb.get("A")

    return 0

# main()