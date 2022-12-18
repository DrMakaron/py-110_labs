import json
import re

BOOKS_FILE = "books.md"
# TODO записать ругулярное выражения для поиска книги
BOOK_REGEX = r"""####\s+(?P<position>\d+)\.\s+\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s+(?P<author>.+?)\s+\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)\s+!\[.*?\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)"""


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    buffer = []
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            data = json.dumps(book.groupdict(), indent=4)
            print(data)

            buffer.append(json.loads(data))

    with open('file.json', 'a') as file:
        json.dump(buffer, file, indent=4)


if __name__ == '__main__':
    task()
