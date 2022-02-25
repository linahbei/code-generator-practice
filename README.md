# *閃電秀/短講*題目構想 -- 《如何讓自己的 SDK / API 可以自動生出 Method Stub》

###### tags: ``閃電秀``
___

## 問題背景

*注意：本文的 **stub**，指的是 [Method **Stub**](https://en.wikipedia.org/wiki/Method_stub)，不是 [Test Double](https://en.wikipedia.org/wiki/Test_double) 的 **stub**。*

使用過 framework、platform 的開發人員，應該都有用過*自動產生基礎程式碼 (Method Stub , stub)* 的功能。例如 MVC 框架自動產生 Controller，還幫你*寫好*基本的 CRUD member function。又或者是使用 IDE 開發時，也有利用 refactor 工具，自動 override 父類別方法、生出基礎程式碼的功能。

也許我 (們) 還沒有能力開發一個 framework，但是工作上總有和別人合作，提供 SDK / API 的機會，如果想要讓自己的 SDK / API，也有自己生出一段 Method Stub 的能力，該怎麼做呢？

## 從一個 Python 套件開始

*挖坑：之後當然是希望能補充其他程式語言的版本。*

### 設計示範用的套件

我們會從一個簡單的 ``foo`` 套件開始 (也只有這個簡單的套件)，其中包含 ``sayAgain`` 與 ``sayAgainWrapper`` (annotation-style) methods，功能是接受一個傳入字串，並回傳 ``Say: {字串}`` 。重點是這個套件需要提供 Method Stub 的功能，使用者可以指定 method、*生出* Method Stub (程式碼)。


### 如何生出 Method Stub

小目標：實作 "產生*示範用套件*範例程式碼 method stub" 的功能。

為了實現這個小目標，我們先用最簡單直白的方式，就是直接 *hardcode* 一個範例程式 (``FooUsageExample`` Class)。再用[序列化](https://zh.wikipedia.org/wiki/%E5%BA%8F%E5%88%97%E5%8C%96)的方式 -- 只不過我們序列化的目標是程式碼，再加上一些簡單的命令列參數，讓使用者可以透過螢幕、程式碼檔案...，輸出 method stub。

在 Python 中，可以用 ``inspect.getsource(object)``  將*程式*序列化為*程式碼*  (plain text)，以下是範例專案的說明。

#### 下載範例專案

```shell
$ git clone git@github.com:linahbei/method-stub-practice.git
$ cd method-stub-practice/python
```

#### *示範用套件*的使用範例

```shell
python3 src/foo_example.py      
Say: bar
Say: bar
```

#### *生出* Method Stub 程式碼

##### Usage

```shell
 python3 src/foo.py -h
usage: foo.py [-h] [--out filename.py]

optional arguments:
  -h, --help           show this help message and exit
  --out filename(.py)  Export method stub to a source code file.
```

##### Example

> 從螢幕顯示結果，並指定要輸出的程式碼檔案

```shell
$ python3 src/foo.py --out example
class FooUsageExample:
    @staticmethod
    @Foo.sayAgainWrapper
    def say_again(say: str):
        print(say)
```

> 查看輸出的 Method Stub 程式碼檔案

```shell
$ cat example.py 
class FooUsageExample:
    @staticmethod
    @Foo.sayAgainWrapper
    def say_again(say: str):
        print(say)
```

##### 無聊的話可以跑一下測試 ...

```shell
$ python3 -m unittest tests/test_foo_package.py
```

### 其他討論

#### Q. 那個 "Method Stub 程式碼檔案"，為什麼不直接用檔案操作的方式，列印、複製給使用者就好了？

> 如果只是要提供範例*程式碼*，當然用檔案操作的方式就好了，看要把範例放在 assets、網路 ... 都可以。
> 
> 不過我們好奇的是 *Method Stub* 的解決方案。意思是使用者可能會需要動態增減指定的 methods、支援選用 APIs 的範例*程式*，然後取得範例*程式碼*。因此最後實作的方式，用的是將*程式*序列化為*程式碼*的方法。
> 
> 另外，*序列化*使用在這裡的確不太精確，後續會研究要怎麼更正確的表達。

