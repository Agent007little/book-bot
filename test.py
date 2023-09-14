def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = 0
    if start + size > len(text):
        end = len(text) - 1
    elif text[start + size] in ',.?!:;':
        end = start + size - 3
    else:
        end = start + size - 1
    for i in range(end, start, -1):
        if text[i] in ',.?!:;':
            return text[start:i + 1], len(text[start:i + 1])


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_simbol = ['.', ',', '!', ':', ';', '?']
    end = start + page_size
    while text[end:][:1] in end_simbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_simbol)) + 1]
    return text, len(text)

# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 1050


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    pass
