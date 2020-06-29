# Программирование (Python)
# 6 семестр, тема 2

# Лабораторная работа 6

"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

def get_fib_nums_lst(n):
	"""
	n - количество чисел в списке 

	"""
	def fib(n):
		a, b = 0, 1
		for _ in range(n):
			yield a
			a, b = b, a + b

	if int(n) == 0:
		return None
	return list(fib(n))


assert get_fib_nums_lst(0) is None, "неверный аргумент n"
assert get_fib_nums_lst('0') is None, "неверный аргумент n"
assert get_fib_nums_lst(1) == [0], "ряд начинается с 0"
assert get_fib_nums_lst(2) == [0, 1], "ряд длины 2"
assert get_fib_nums_lst(3) == [0, 1, 1], "ряд длины 3"
assert get_fib_nums_lst(5) == [0, 1, 1, 2, 3], "ряд длины 5"
assert get_fib_nums_lst(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "ряд длины 10"
