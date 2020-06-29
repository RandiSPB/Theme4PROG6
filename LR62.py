order = int(''.join(i for i in input(': ') if i.isdigit()))
fib = [0, 1]
fib += [fib.append(fib[_-2] + fib[_-1]) for _ in range(2, order)]
fib = [item for item in fib if isinstance(item, int)]
print(fib)
