class User:
    """A sample USER class"""

    def __init__(self, idx, first, last, email):
        self.idx = idx
        self.first = first
        self.last = last
        self.email = email
        self.rating = 0
        self.review_cnt = 0
