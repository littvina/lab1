# TODO Найдите количество книг, которое можно разместить на дискете


ob_in_mbait = 1.44
ob_in_bait = ob_in_mbait * 1024 * 1024
pages = 100
lines = 50
simbols = 25
ob_of_simbol = 4
ob_of_book = pages * lines * simbols * ob_of_simbol

print("Количество книг, помещающихся на дискету:", int(ob_in_bait // ob_of_book))