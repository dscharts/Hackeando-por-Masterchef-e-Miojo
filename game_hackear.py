#coding: utf-8
from random import randint

class Usuario:
    def __init__(self):
        self.username = ""
        self.barras_wifi = 42
        self.conexao_maxima = 42
    def rastrear(self, vizinho):
        piora_conexao = min(max(randint(0, self.barras_wifi) - randint(0, vizinho.barras_wifi), 0), vizinho.barras_wifi)
        vizinho.barras_wifi = vizinho.barras_wifi - piora_conexao
        if piora_conexao == 0: print "%s põe senha na wifi, para se defender de %s" %(vizinho.username, self.username)
        else: print "%s hackeia %s!" %(self.username, vizinho.username)
        return vizinho.barras_wifi <= 0

class Com_wifi(Usuario):
    def __init__(self, usuario):
        Usuario.__init__(self)
        if randint(0, 1):
            self.username = "Vizinho rico"
        else:
            self.username = "Vizinho chato"
        self.barras_wifi = randint(int(usuario.conexao_maxima * 0.8), usuario.conexao_maxima)

class TV():
    def __init__(self, tv):
        if randint(0, 2):
            self.username = "Masterchef"
        else if:
            self.username = "AHS"
        else:
            self.username = "The Flash"

class Sua_conta(Usuario):
    def __init__(self):
        Usuario.__init__(self)
        self.mensagem_de_humor = 'bored'
        self.barras_wifi = 42
        self.conexao_maxima = 42
    def desistir(self):
        print "Megafilmes caiu de novo, agora %s nem precisa mais de net" % self.username
        self.barras_wifi = 0
    def trending_topics(self): print Comandos.keys()
    def mensagem_de_humor(self): print "Conexão de %s: %d/%d" % (self.username, self.barras_wifi, self.conexao_maxima)
    def fome(self):
        print "%s quer comer logo o miojo" % self.username
        self.barras_wifi = max(1, self.barras_wifi - 1)
    def comer(self):
        if self.mensagem_de_humor != 'bored': print "%s não pode comer o miojo ainda!" % self.username; self.conexaoRuim()
        else:
            print "%s come seu miojo." % self.username
            if randint(0, 1):
                self.vizinho = Com_wifi(self)
                print "%s tem seu download parado por %s!" % (self.username, self.vizinho.username)
                self.mensagem_de_humor = 'FIGHT'
                self.conexaoRuim()
            else:
                if self.barras_wifi < self.conexao_maxima:
                    self.barras_wifi = self.barras_wifi + 1
                else: print "Deu dor de barriga, e derrubou água no PC"; self.barras_wifi = self.barras_wifi - 1
    def baixar(self):
        if self.mensagem_de_humor != 'bored':
            print "%s ainda não acessou uma rede!" % self.username
            self.conexaoRuim()
        else:
            print "%s encontra o download, e agora quer ver %s" % (self.username, tv.username)
            if randint(0, 1):
                self.vizinho = Com_wifi(self)
                print "%s percebe Wifi do %s!"  % (self.username, self.vizinho.username)
                self.mensagem_de_humor = 'FIGHT'
            else:
                if randint(0, 1): self.fome()
    def procurar_nova_rede(self):
        if self.mensagem_de_humor != 'FIGHT':
            print "%s não encontra nenhuma rede" % self.username
            self.fome()
        else:
            if randint(1, self.barras_wifi + 5) > randint(1, self.vizinho.barras_wifi):
                print "%s vai procurar uma rede que não de %s" %(self.username, self.vizinho.username)
                self.vizinho = None
                self.mensagem_de_humor = 'bored'
            else:
                print "%s não encontra outra rede, vai ter que hackear a do %s mesmo" % (self.username, self.vizinho.username)
                self.conexaoRuim()
    def hack(self):
        if self.mensagem_de_humor != 'FIGHT':
            print "%s precisa de tratamento mental" % self.username
            self.fome()
        else :
            if self.rastrear(self.vizinho):
                print "%s tomou conta da rede de %s forevah" % (self.username, self.vizinho.username)
                self.vizinho = None
                self.mensagem_de_humor = 'bored'
                if randint(0, self.barras_wifi) <  42:
                    self.barras_wifi = self.barras_wifi + 2
                    self.conexao_maxima = self.conexao_maxima + 2
                    print "%s expande sua rede ilegal de hacking!" % self.username
            else: self.conexaoRuim()
    def conexaoRuim(self):
        if self.vizinho.rastrear(self):
            print "%s teve o IP rastreado por %s, e vai ter que voltar a morar com os pais" %(self.username, self.vizinho.usernmae)

Comandos = {
    'desistir': Sua_conta.desistir,
    'ajuda': Sua_conta.trending_topics,
    'mensagemDeHumor': Sua_conta.mensagem_de_humor,
    'comerMiojo': Sua_conta.comer,
    'rastrear': Sua_conta.baixar,
    'outraRede': Sua_conta.procurar_nova_rede,
    'hackear': Sua_conta.hack,
    }

p = Sua_conta()
p.username = raw_input("Qual o username do seu hacker no twitter? ")
print "(digite ajuda para obter lista de ações)"
print "%s chega em casa, querendo baixar o episódio do Mar Vermelho" % p.username

while p.barras_wifi > 0:
    linha = raw_input("> ")
    args = linha.split()
    if len(args) > 0:
        comandoEncontrado = False
        for c in Comandos.keys():
            if args[0] == c[:len(args[0])]:
                Comandos[c](p)
                comandoEncontrado = True
                break
        if not comandoEncontrado:
            print "%s gostaria que você aprendesse a escrever direito" %p.username
