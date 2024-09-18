import argparse
from calculadora_horas import CalculadoraHoras

def main():
    parser = argparse.ArgumentParser(description='Calculadora de horas trabalhadas.')
    
    parser.add_argument('--inicio', type=str, required=True, help='Horário de início (formato HH:mm ou HHmm)')
    parser.add_argument('--termino', type=str, required=True, help='Horário de término (formato HH:mm ou HHmm)')
    parser.add_argument('--intervalo', type=str, help='Intervalo de almoço (formato HH:mm ou HHmm)', default="00:00")
    
    args = parser.parse_args()
    
    calculadora = CalculadoraHoras()
    
    inicio = corrigir_formato(args.inicio)
    termino = corrigir_formato(args.termino)
    intervalo = corrigir_formato(args.intervalo)

    calculadora.inserir_horarios(inicio, termino)
    calculadora.inserir_intervalo(intervalo)
    
    horas_trabalhadas = calculadora.calcular_horas_trabalhadas()
    
    print(f"Horas trabalhadas (descontando intervalo): {horas_trabalhadas:.2f} horas")

def corrigir_formato(horario):
    if ":" not in horario:
        if len(horario) == 3:  
            horario = "0" + horario  
        horario = horario[:2] + ":" + horario[2:] 
    return horario

if __name__ == "__main__":
    main()