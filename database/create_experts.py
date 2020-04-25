import sqlite3
from experts import Expert

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE expert ( 
            idx  integer,
            first text,
            last text, 
            email text
            )""")


def insert_experts(user):
    with conn:
        c.execute("INSERT INTO expert VALUES (:idx, :first, :last, :email)", {'idx': user.idx, 'first': user.first, 'last': user.last, 'email': user.email})


def get_expert_by_id(idx):
    c.execute("SELECT * FROM expert WHERE idx=:idx", {'idx': idx})
    return c.fetchall()


if __name__ == '__main__':
    user_1 = Expert('0', 'Laura', 'Mullen', 'laura@gmail.com')
    user_2 = Expert(1, 'Lena', 'Gross', 'lena@gmail.com')

    insert_experts(user_1)
    insert_experts(user_2)

    expert = get_expert_by_id(0)
    print(expert)


