def make_string_upper(fn):
    def wrapper():
        # TODO перевести результат исходной функции в верхний регистр
        return fn().upper()
    return wrapper


@make_string_upper
def get_text() -> str:
    return "Hello, World!!!"


if __name__ == "__main__":
    print(get_text())
