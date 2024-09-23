def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
# Вызов inner_function вне функции test_function выдает ошибку при результате выполнения программы
test_function()
