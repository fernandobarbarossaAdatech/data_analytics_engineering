from datetime import datetime


class AutomovelExemplo:
    pass


class AutomovelAtributos:

    def __init__(self, placa: str, ano: int) -> None:
        self.placa = placa
        self.ano = ano


class Automovel:

    def __init__(self, placa: str, ano: int) -> None:
        self.placa = placa
        self.ano = ano

        self.velocidade = 0

    def aumentar_velocidade(self) -> None:

        self.velocidade += 1

    def diminuir_velocidade(self) -> None:

        self.velocidade -= 1

    @staticmethod
    def paga_ipva_em_sp(ano: int) -> bool:

        if datetime.now().year > ano + 20:
            return False
        return True


class Carro(Automovel):

    def __init__(self, placa: str, ano: int, modelo: str, automatico: bool) -> None:
        super().__init__(placa, ano)

        self.modelo = modelo
        self.automatico = automatico


class Caminhao(Automovel):

    def __init__(self, placa: str, ano: int, eixo: int) -> None:
        super().__init__(placa, ano)

        self.eixo = eixo

    def aumentar_velocidade(self) -> None:

        self.velocidade += 0.75
