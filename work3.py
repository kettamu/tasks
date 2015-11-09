__author__ = 'mityagov_vi'


def dec(fun_dec):
    def dec_fun(*args):
        print('begin')
        fun_dec(*args)
        print('end')

    return dec_fun()


@dec
def add(*args):
    result = (sum(args))
    print(result)


"""
a = 10
if str(type(a)).find('int'):
    print a ** 2"""
