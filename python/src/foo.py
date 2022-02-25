import types
import argparse
import inspect


class Foo:
    SAY_AGAINE_PREFIX = 'Say: '

    @staticmethod
    def sayAgain(say: str, callback=None):
        if not isinstance(say, str):
            raise TypeError(f"Can not say again for {type(say)} type.")
        say_again = f"{Foo.SAY_AGAINE_PREFIX}{say}"
        return say_again if not isinstance(callback, types.FunctionType)\
            else callback(say_again)

    @staticmethod
    def sayAgainWrapper(func):
        def sayAgain(say):
            Foo.sayAgain(say, func)
        return sayAgain


class FooUsageExample:
    @staticmethod
    @Foo.sayAgainWrapper
    def say_again(say: str):
        print(say)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', dest='out', required=False, type=str,
                        metavar='filename(.py)', default=None,
                        help='Export method stub to a source code file.'
                        )
    args = parser.parse_args()
    plain = inspect.getsource(FooUsageExample)
    print(plain)
    if args.out is not None:
        with open(f"{args.out}.py", 'w') as f:
            f.write(plain)
