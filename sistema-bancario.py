
### Sistema Bancário OOP - Python ###

class Conta:
    def __init__(self, n_conta, cpf, agencia):
        self.__n_conta = n_conta
        self.__cpf = cpf
        self.__agencia = agencia
    
    @property
    def n_conta(self):
        return self.__n_conta
    @n_conta.setter
    def n_conta(self, n_conta):
        self.__n_conta = n_conta
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia



class ContaCorrente(Conta):
    def __init__(self, n_conta, cpf, agencia):
        super().__init__(n_conta, cpf, agencia)
    
    def saque(self):
        pass
    def deposito(self):
        pass
    def trasnferencia(self):
        pass

class ContaPoupança(Conta):
    def __init__(self, n_conta, cpf, agencia):
        super().__init__(n_conta, cpf, agencia)
    
    def rendimento(self):
        pass