# inmemory db

class InMemoryDB:

    def __init__(self):
        self.accounts = {}
    
    def get(self, key: str) -> int:
        pass

    def put(self, key: str, val: int):
        pass

    def begin_transaction(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass