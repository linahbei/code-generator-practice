from foo import Foo


@Foo.sayAgainWrapper
def say_again(say: str):
    print(say)


if __name__ == '__main__':
    say = 'bar'
    print(Foo.sayAgain(say))
    say_again(say)
