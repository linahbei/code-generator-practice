# Lightning Talk -- 《人生第一個 Python “Code Generator”》

###### tags: ``Lightning Talk``

[![License: Public Domain / No Copyright](https://i.creativecommons.org/p/mark/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
___

## 簡報資料

* [Git repo](https://github.com/linahbei/code-generator-practice)
* [投影片](https://docs.google.com/presentation/d/1oCiX8IPvvx2oY2a8F3TZerM3yamMaJURKETHMLigsYA/edit?usp=sharing)


## 說明

### 下載範例專案

```shell
$ git clone https://github.com/linahbei/code-generator-practice
$ cd code-generator-practice/python
```

### User 範例程式

```shell
$ python3 src/foo_example.py      
Say: bar
Say: bar
```

### ``Foo`` package 的 code generator 指令

#### Usage

```shell
$ python3 src/foo.py -h
usage: foo.py [-h] [--out filename.py]

optional arguments:
  -h, --help           show this help message and exit
  --out filename(.py)  Export example code.
```

#### Example

> 從螢幕顯示結果，並產生程式碼檔案

```shell
$ python3 src/foo.py --out example
class FooUsageExample:
    @staticmethod
    @Foo.sayAgainWrapper
    def say_again(say: str):
        print(say)
```

> 查看產生的程式碼檔案

```shell
$ cat example.py 
class FooUsageExample:
    @staticmethod
    @Foo.sayAgainWrapper
    def say_again(say: str):
        print(say)
```

### 跑一下測試

```shell
$ python3 -m unittest tests/test_foo_package.py
```

