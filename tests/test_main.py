import pytest

from main import brackets_check_balanсed


class TestBrackets:
    @pytest.mark.parametrize(
        'input,expected', [
            (r'(((([{}]))))', 'Сбалансированно'),
            (r'[([])((([[[]]])))]{()}', 'Сбалансированно'),
            (r'{{[()]}}', 'Сбалансированно'),
            (r'}{}', 'Несбалансированно'),
            (r'{{[(])]}}', 'Несбалансированно'),
            (r'[[{())}]', 'Несбалансированно')
        ]
    )
    def test_brackets_balance(self, input, expected):
        result = brackets_check_balanсed(input)
        assert result == expected
    
    # @pytest.xfail
    # @pytest.mark.parametrize(
    #     'input,expected', [
    #         (r'', '<ошибка>'),
    #         (r'test', '<ошибка>'),
    #     ]
    # )
    # def test_not_brackets(self, input, expected):
    #     result = brackets_check_balanсed(input)
    #     assert result == expected