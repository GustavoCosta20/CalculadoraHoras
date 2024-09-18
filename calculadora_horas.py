from datetime import datetime, timedelta

class CalculadoraHoras:
    def __init__(self):
        self.horario_inicio = None
        self.horario_termino = None
        self.intervalo = 0

    def inserir_horarios(self, inicio, termino):
        formato = "%H:%M"
        try:
            self.horario_inicio = datetime.strptime(inicio, formato)
            self.horario_termino = datetime.strptime(termino, formato)
        except ValueError:
            raise ValueError("Formato de horário inválido. Use HH:mm.")

    def inserir_intervalo(self, duracao_intervalo):
        formato = "%H:%M"
        try:
            intervalo = datetime.strptime(duracao_intervalo, formato)
            self.intervalo = intervalo.hour + intervalo.minute / 60
        except ValueError:
            raise ValueError("Formato de intervalo inválido. Use HH:mm.")

    def calcular_horas_trabalhadas(self):
        if self.horario_termino < self.horario_inicio:
            self.horario_termino += timedelta(days=1)

        horas_trabalhadas = (self.horario_termino - self.horario_inicio).seconds / 3600
        return horas_trabalhadas - self.intervalo

    def inserir_horarios_flexiveis(self, inicio, termino):
        inicio = self._corrigir_formato_horario(inicio)
        termino = self._corrigir_formato_horario(termino)
        self.inserir_horarios(inicio, termino)

    def _corrigir_formato_horario(self, horario):
        if ":" not in horario:
            if len(horario) == 3:
                horario = "0" + horario
            horario = horario[:2] + ":" + horario[2:]
        return horario