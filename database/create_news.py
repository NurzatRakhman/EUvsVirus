import sqlite3
from news import News

conn = sqlite3.connect(':memory:')

c = conn.cursor()


c.execute("""CREATE TABLE news ( 
            idx  integer,
            title text,
            url text 
            )""")


def insert_news(news):
    with conn:
        c.execute("INSERT INTO news VALUES (:idx, :title, :url)", {'idx': news.idx, 'title': news.title, 'url': news.url})


def get_news_by_id(idx):
    c.execute("SELECT * FROM news WHERE idx=:idx", {'idx': idx})
    return c.fetchall()


if __name__ == '__main__':
    news_1 = News(0, 'Beer helps for corona virus', 'nonsense.com')
    news_2 = News(1, 'EU helping each other out',  'eu-gov.com')

    insert_news(news_1)
    insert_news(news_2)

    news = get_news_by_id(0)
    print(news)


