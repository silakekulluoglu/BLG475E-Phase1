def check(candidate):
    assert candidate("Hello world!") == ["Hello", "world!"]
    assert candidate("Hello,world!") == ["Hello", "world!"]
    assert candidate("Hello world,!") == ["Hello", "world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world", "!"]
    assert candidate("abcdef") == 3
