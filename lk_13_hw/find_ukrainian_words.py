import re
from collections import Counter


def find_ukr_words(filename: str):
    with open(filename, 'r') as f:
        data = f.read()
    return dict(Counter((re.findall(r'[А-Яа-яЁёЇїІіЄєҐґ]+', data.lower()))))


print(find_ukr_words("AddBuyersPopup.tsx"))
