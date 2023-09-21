# import theater_module_prac
# theater_module_prac.price(3)
# theater_module_prac.price_morning(4)
# theater_module_prac.price_soldier(5)

# import theater_module_prac as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module_prac import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module_prac import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5) <- 쓸수 없음

from theater_module_prac import price_soldier as price
price(3)