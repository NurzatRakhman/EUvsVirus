import sqlite3
from user import User

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE user ( 
            idx  integer,
            first text,
            last text, 
            email text
            )""")


def insert_user(user):
    with conn:
        c.execute("INSERT INTO user VALUES (:idx, :first, :last, :email)", {'idx': user.idx, 'first': user.first, 'last': user.last, 'email': user.email})


def get_user_by_id(idx):
    c.execute("SELECT * FROM user WHERE idx=:idx", {'idx': idx})
    return c.fetchall()


if __name__ == '__main__':
    user_1 = User('0', 'John', 'Doe', 'john@gmail.com')
    user_2 = User(1, 'Jane', 'Smith', 'smith@gmail.com')

    insert_user(user_1)
    insert_user(user_2)

    user = get_user_by_id(1)
    print(user)
