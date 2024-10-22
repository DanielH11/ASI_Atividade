import unittest

def calc (a, b, op):
    if type (op) is not str:
        return None
    #if type (a) is not float and int:
    if not isinstance(a, int) and not isinstance(a, float):
        print('Erro! O primeiro número não é racional.')
        return None
    #if type (b) is not float and int:
    if not isinstance(b, int) and not isinstance(b, float):
        print('Erro! O segundo número não é racional.')
        return None
    if (op=="+"):
        return a+b
    if(op=="-"):
        return a-b
    if(op=="*"):
        return a*b
    if(op=="/"):
        if(b==0):
            print("Divisão por zero!")
            return None
        return a/b
    if(op=="^"):
        return a**b
    return None

class TestCalc(unittest.TestCase):
    
    # Teste com adição
    def test_add_positive_numbers(self):
        self.assertEqual(calc(10, 5, '+'), 15)
    
    def test_add_negative_numbers(self):
        self.assertEqual(calc(-10, -5, '+'), -15)
    
    def test_add_positive_and_negative(self):
        self.assertEqual(calc(10, -5, '+'), 5)

    # Teste com subtração
    def test_subtract_positive_numbers(self):
        self.assertEqual(calc(10, 5, '-'), 5)
    
    def test_subtract_negative_numbers(self):
        self.assertEqual(calc(-10, -5, '-'), -5)
    
    def test_subtract_positive_and_negative(self):
        self.assertEqual(calc(10, -5, '-'), 15)
    
    def test_subtract_resulting_in_negative(self):
        self.assertEqual(calc(5, 10, '-'), -5)

    # Teste com multiplicação
    def test_multiply_positive_numbers(self):
        self.assertEqual(calc(10, 5, '*'), 50)
    
    def test_multiply_negative_numbers(self):
        self.assertEqual(calc(-10, -5, '*'), 50)
    
    def test_multiply_positive_and_negative(self):
        self.assertEqual(calc(10, -5, '*'), -50)

    def test_multiply_by_zero(self):
        self.assertEqual(calc(10, 0, '*'), 0)
    
    # Teste com divisão
    def test_divide_positive_numbers(self):
        self.assertEqual(calc(10, 5, '/'), 2)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(calc(-10, -5, '/'), 2)
    
    def test_divide_positive_and_negative(self):
        self.assertEqual(calc(10, -5, '/'), -2)
    
    # Divisão por zero
    def test_divide_by_zero(self):
        self.assertEqual(calc(10, 0, '/'), None)
    
    # Teste com exponencial
    def test_exponentiation_positive_numbers(self):
        self.assertEqual(calc(2, 3, '^'), 8)
    
    def test_exponentiation_negative_exponent(self):
        self.assertEqual(calc(2, -3, '^'), 0.125)
    
    def test_exponentiation_zero_exponent(self):
        self.assertEqual(calc(2, 0, '^'), 1)

    def test_exponentiation_base_zero(self):
        self.assertEqual(calc(0, 5, '^'), 0)

    # Teste com operador inválido
    def test_invalid_operation(self):
        self.assertEqual(calc(10, 5, '%'), None)

# Running the tests
if __name__ == '__main__':
    unittest.main()

print(calc(1, 2.4, "-"))