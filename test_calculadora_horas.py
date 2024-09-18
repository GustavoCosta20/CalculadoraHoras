import unittest
from calculadora_horas import CalculadoraHoras

class TestCalculadoraHoras(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraHoras()

    def test_calculo_horas_trabalhadas(self):
        self.calculadora.inserir_horarios('08:00', '17:00')
        self.calculadora.inserir_intervalo('01:00')
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 8)

    def test_formato_invalido(self):
        with self.assertRaises(ValueError):
            self.calculadora.inserir_horarios('8', '1700')

    def test_inversao_horarios(self):
        self.calculadora.inserir_horarios('17:00', '08:00')
        self.calculadora.inserir_intervalo('01:00')
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 8)

    def test_inserir_horarios_sem_dois_pontos_hhmm(self):
        self.calculadora.inserir_horarios_flexiveis('0800', '1700')
        self.calculadora.inserir_intervalo('0100')
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 8)

    def test_inserir_horarios_sem_dois_pontos_h_mm(self):
        self.calculadora.inserir_horarios_flexiveis('800', '1700')
        self.calculadora.inserir_intervalo('0100')
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 8)

    def test_inserir_intervalo_sem_dois_pontos(self):
        self.calculadora.inserir_horarios('08:00', '17:00')
        self.calculadora.inserir_intervalo('0100')  #intervalo sem :
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 8)

    def test_calculo_sem_intervalo(self):
        self.calculadora.inserir_horarios('08:00', '17:00')
        horas_trabalhadas = self.calculadora.calcular_horas_trabalhadas()
        self.assertEqual(horas_trabalhadas, 9)

if __name__ == '__main__':
    unittest.main()