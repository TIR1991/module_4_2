def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # ичего не происходит
inner_function() # ыдает ошибку
test_function() # выводит (Я в области видимости функции test_function)