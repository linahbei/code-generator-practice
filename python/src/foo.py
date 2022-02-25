import types


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
