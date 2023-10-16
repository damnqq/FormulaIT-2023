ONE_SYMBOL_BYTE = 4

disk_size_mbyte = 1.44
disk_size_byte = disk_size_mbyte * 1024 * 1024

book = {
    "pages": 100,
    "lines in one page": 50,
    "symbols in one line": 25
}

symbols_in_one_book_byte = book["symbols in one line"] * book["lines in one page"] * book["pages"] * ONE_SYMBOL_BYTE
books_on_disk = int(disk_size_byte // symbols_in_one_book_byte)


print("Количество книг, помещающихся на дискету:", books_on_disk)