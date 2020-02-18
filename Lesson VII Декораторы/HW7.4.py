"""
4. Написать декоратор, который будет проверять
   тип аргументов при вызове функции согласно аннотации функции.
   Декорирование функции без аннотации или
   с неполной аннотацией (когда аннотированы не все аргументы)
   должно рейзить ошибку. В случае несовпадения переданных
   во время вызова функции аргументов с типами аргументов
   в аннотации - выводить сообщение.

"""


def check_type(func):
    code = func.__code__
    all_args = code.co_varnames[:code.co_argcount]

    def wrapper(*args, **kwargs):
        argchecks = func.__annotations__
        if len(all_args) != len(argchecks):
            print("аннотированы не все аргументы")
            return None
        positionals = list(all_args)[:len(args)]
        print(argchecks)
        for (arg_name, type_arg) in argchecks.items():
            if arg_name in kwargs:
                if not isinstance(kwargs[arg_name], type_arg):
                    print("неверный тип аргумента ключ-значение")
            elif arg_name in positionals:
                position = positionals.index(arg_name)
                if not isinstance(args[position], type_arg):
                    print("неверный тип позиционного аргумента")
        return func(*args, **kwargs)
    return wrapper


@check_type
def foo(a: int, b: int, c: int):
    print(a, b, c)


foo(1, 2, c=3)
