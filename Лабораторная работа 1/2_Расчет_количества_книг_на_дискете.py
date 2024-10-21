# TODO Найдите количество книг, которое можно разместить на дискете
disket_volume_MB = 1.44
disket_volume_bytes = disket_volume_MB*(1024**2)
bytes_for_symbol = 4
pages_by_book = 100
rows_by_page = 50
symbols_by_row = 25
qty_of_symbols = pages_by_book*rows_by_page*symbols_by_row
qty_of_books = ((disket_volume_bytes)//(qty_of_symbols*bytes_for_symbol))
print("Количествоs книг, помещающихся на дискету:", qty_of_books)
