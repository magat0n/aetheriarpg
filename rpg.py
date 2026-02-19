import random
import time
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa(seg=2):
    time.sleep(seg)

def narrar(texto):
    print("\n" + texto)
    pausa(2)

# INTRODUÇÃO

def introducao():
    limpar()
    print(r"""
 █████╗ ███████╗████████╗██╗  ██╗███████╗██████╗ ██╗ █████╗ 
██╔══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗██║██╔══██╗
███████║█████╗     ██║   ███████║█████╗  ██████╔╝██║███████║
██╔══██║██╔══╝     ██║   ██╔══██║██╔══╝  ██╔══██╗██║██╔══██║
██║  ██║███████╗   ██║   ██║  ██║███████╗██║  ██║██║██║  ██║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

        ⚔ REINOS DE AETHERIA ⚔
""")

    narrar("O reino de Aetheria vive dias sombrios...")
    narrar("Criaturas emergem das florestas. Vilarejos desaparecem.")
    narrar("E no topo das Montanhas Cinzentas... algo antigo despertou.")
    narrar("Seu destino começa agora.")

# PERSONAGEM

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.level = 1
        self.exp = 0
        self.moedas = 50
        self.reputacao = 0
        self.status = "Vivo"
        self.inventario = ["Poção de Cura"]

        if classe == "Guerreiro":
            self.hp = 150
            self.forca = 30
            self.habilidades = ["Golpe Brutal"]
        elif classe == "Mago":
            self.hp = 100
            self.forca = 20
            self.habilidades = ["Bola de Fogo"]
        elif classe == "Arqueiro":
            self.hp = 120
            self.forca = 25
            self.habilidades = ["Tiro Certeiro"]

        self.hp_max = self.hp

    def mostrar_status(self):
        print(f"""
===== STATUS =====
Nome: {self.nome}
Classe: {self.classe}
Level: {self.level}
HP: {self.hp}/{self.hp_max}
Força: {self.forca}
EXP: {self.exp}
Moedas: {self.moedas}
Reputação: {self.reputacao}
Habilidades: {self.habilidades}
Inventário: {self.inventario}
""")

    def ganhar_exp(self, qtd):
        self.exp += qtd
        if self.exp >= self.level * 100:
            self.level += 1
            self.exp = 0
            self.forca *= 2
            self.hp_max += 40
            self.hp = self.hp_max
            narrar(f"🔥 Você alcançou o level {self.level}!")

# MONSTROS

class Monstro:
    def __init__(self, level):
        nomes = ["Goblin", "Orc", "Lobo Selvagem", "Esqueleto", "Mago Necromante", "Slime"]
        self.nome = random.choice(nomes)
        self.hp = random.randint(80, 120) + level * 10
        self.forca = random.randint(10, 20) + level * 5
        self.exp = random.randint(40, 60)

# COMBATE 

def combate(jogador):
    limpar()
    narrar("Você atravessa os portões da cidade...")
    narrar("A névoa cobre o campo aberto diante de você.")

    inimigo = Monstro(jogador.level)

    narrar(f"Das sombras surge um {inimigo.nome}!")

    while inimigo.hp > 0 and jogador.hp > 0:

        print(f"\nSeu HP: {jogador.hp} | HP do inimigo: {inimigo.hp}")
        print("1 - Atacar")
        print("2 - Usar Habilidade")
        print("3 - Usar Item")
        print("4 - Fugir")

        escolha = input("> ")

        if escolha == "1":
            dano = jogador.forca + random.randint(5, 15)
            inimigo.hp -= dano
            narrar(f"Você atinge o {inimigo.nome} causando {dano} de dano!")

        elif escolha == "2":
            dano = jogador.forca * 2
            inimigo.hp -= dano
            narrar(f"🔥 {jogador.habilidades[0]} explode contra o inimigo!")

        elif escolha == "3":
            if "Poção de Cura" in jogador.inventario:
                jogador.hp += 50
                jogador.inventario.remove("Poção de Cura")
                narrar("Você bebe a poção e sente suas forças retornarem.")
            else:
                print("Sem itens!")

        elif escolha == "4":
            narrar("Você recua estrategicamente...")
            return

        if inimigo.hp > 0:
            jogador.hp -= inimigo.forca
            narrar(f"O {inimigo.nome} contra-ataca!")

    if jogador.hp <= 0:
        narrar("☠ Você morreu em batalha...")
        exit()
    else:
        narrar(f"O {inimigo.nome} cai derrotado.")
        jogador.ganhar_exp(inimigo.exp)
        jogador.moedas += 30
        jogador.reputacao += 5

# NPC SISTEMA

def conversar(nome_npc, falas):
    print(f"\nVocê conversa com {nome_npc}...")
    print(random.choice(falas))

def ferreiro(jogador):
    falas = [
        "Minhas lâminas já derrubaram gigantes.",
        "O aço fala mais alto que palavras.",
        "Se quer sobreviver, invista em sua arma."
    ]

    while True:
        print("\n=== FERREIRO ===")
        print("1 - Conversar")
        print("2 - Comprar Poção (20 moedas)")
        print("3 - Melhorar arma (+10 força / 50 moedas)")
        print("4 - Sair")

        op = input("> ")

        if op == "1":
            conversar("o Ferreiro", falas)

        elif op == "2" and jogador.moedas >= 20:
            jogador.inventario.append("Poção de Cura")
            jogador.moedas -= 20
            print("Você comprou uma poção.")

        elif op == "3" and jogador.moedas >= 50:
            jogador.forca += 10
            jogador.moedas -= 50
            narrar("O ferreiro reforça sua arma com aço rúnico.")

        elif op == "4":
            break

def hotel(jogador):
    narrar("O calor da lareira envolve o ambiente.")
    jogador.hp = jogador.hp_max
    narrar("Você descansa e recupera suas energias.")

# CIDADE COM NARRAÇÃO

def cidade(jogador):
    while True:
        limpar()
        narrar("Você caminha pelas ruas de pedra de Aetheria.")
        narrar("Mercadores gritam ofertas. Guardas vigiam atentos.")

        print("1 - Hotel")
        print("2 - Ferreiro")
        print("3 - Guilda de Missões")
        print("4 - Status")
        print("5 - Sair")

        escolha = input("> ")

        if escolha == "1":
            hotel(jogador)

        elif escolha == "2":
            ferreiro(jogador)

        elif escolha == "3":
            combate(jogador)

        elif escolha == "4":
            jogador.mostrar_status()
            input("Pressione ENTER...")

        elif escolha == "5":
            break

# CRIAÇÃO PERSONAGEM

def criar_personagem():
    nome = input("Qual é o seu nome, aventureiro? ")
    print("Escolha sua classe:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")

    escolha = input("> ")
    classe = ["guerreiro", "mago", "arqueiro"][int(escolha)-1]

    narrar(f"Você escolheu o caminho do {classe}.")
    return Personagem(nome, classe)


introducao()
jogador = criar_personagem()
cidade(jogador)
