# Código copiado e colado deste link apenas para fins de exemplo.
# https://dev.to/womakerscode/testes-em-python-parte-1-introducao-43ei

from unittest import main, TestCase


def square(x):
    return x ** 2


class TestSquare(TestCase):
    def test_if_returns_square_of_2(self):
        result = square(2)
        expected = 4

        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
