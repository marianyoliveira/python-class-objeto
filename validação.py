class Cadastro:
        idade = None 
        def __init__(self):
            pass

        def InserirNome(self, idade):
            IdadeCorreta = self.ValidaIdade(idade)
            if IdadePreenchido == True:
                 self.nome = idade
                 print(" O nome não pode estar vazio")

        def ValidaNome(self, idade):
             if len(nome)
                  print ("Cadastrado com sucesso")
                  return False
             else:
                  return True
        def InserirIdade(self,idade):
             idadeCorreta = self.ValidaIdade(idade):
             if idadeCorreta == True:
                  self.idade = idade
                  print("Valor cadastrado com sucesso")
                  return False
             else:
                  return True

        def InserirSaldo(self, saldo):
             SaldoCorreto = self.ValidaSaldo(saldo) 
             if saldoCorreto == True:
                self.saldo = saldo  
                print("valor cadastrado com sucesso")

        def ValidaSaldo(self, saldo):
            if saldo < 0:
                print("O Saldo precisa ser maior que zero")
                return False
            else:
                 return True                 



