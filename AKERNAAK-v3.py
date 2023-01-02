from os import system
from sys import exit
from random import randrange
from time import sleep

def novo_jogo():
    global vocabulario, objetos, locais, entrada, palavra_magica, selecao, vida, inimigo_pula, inimigo_segue, akon, numero_aleatorio, ataque, pontos, tempo, altar, mago, espada, dano, flauta, arca, garrafa, posicao_objetos, inventario, direcoes, vida_inimigos, buffers_luta, posicao_jogador

    vocabulario = ["FUJA", "LUTE", "PEGUE", "SAIA", "AJUDA", "FALE", "ABRA", "ENTRE", "LISTE", "TOQUE", "DESCANSE", "DESISTA", "AKERNAAK"] # vo
    objetos = ["A ESPADA", " ESCUDO", " LIVRO", "A CAPA", " DIAMANTE", " ANEL", " ESPELHO", " PERGAMINHO", "A MOEDA DE OURO", "A LANTERNA", "A FLAUTA", " ELMO", "A GARRAFA DE VINHO", " CETRO DE PRATA", "A CHAVE", "A ARCA", "A ESTATUA", "A PASSAGEM", " ALTAR DE AKERNAAK", "A ESFERA DOS ELFOS", " DUENDE", " OGRO", " TIGRE", " ELFO", " PITON", " MAGO", " GUERREIRO AKERNAAK", " FEITICEIRO DE FOGO", " MESTRE-FEITICEIRO", " ASTERION", " DRAGÃO"] # obj
    locais = ["A ENTRADA DA CASA", "O HALL", "O CORREDOR", "A ESCADA", "O QUARTO", "A GARAGEM", "A SALA", "O SALÃO DE JOGOS", "A BIBLIOTECA", "A PORTA DOS FUNDOS", "A DESPENSA", "A COZINHA", "O BANHEIRO", "O GRAMADO", "O MURO", "A ARCA", "A PASSAGEM SECRETA", "O CASTELO VERMELHO", "O DIAMANTE", "O CAMPO ZERO"] # lo

    entrada = palavra_magica = str() # a, pm
    selecao = vida = inimigo_pula = inimigo_segue = akon = numero_aleatorio = ataque = pontos = tempo = altar = mago = espada = dano = int() # n, cf/cfi, fb, fs, fa, rn, cb, pt, t, tm, to, te, s
    flauta = arca = garrafa = False # ft, fa%, fg
    posicao_objetos = [randrange(0, 15) for _ in range(31)] # ma
    inventario = [False for _ in range(15)] # fp
    direcoes = [[-1, -1] for _ in range(20)] # d
    vida_inimigos = [int() for _ in range(11)] # cf
    buffers_luta = [3, 6, 7, 1, 6, 2, 6, 3, 3, 2, 3] # bl

    for i in [13, 17, 19, 24, 25, 26, 29, 30]:
        posicao_objetos[i] = -1

    posicao_objetos[2] = 8
    posicao_objetos[3] = randrange(1, 3) + 14
    posicao_objetos[4] = 15
    posicao_objetos[6] = 16
    posicao_objetos[7] = 18
    posicao_objetos[11] = randrange(1, 3) + 14
    posicao_objetos[15] = 4
    posicao_objetos[16] = 13
    posicao_objetos[27] = 19
    posicao_objetos[28] = 18

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]:
        while True:
            direcoes[i][0] = randrange(0, 15)
            direcoes[i][1] = randrange(0, 15)

            if direcoes[i][0] != direcoes[i][1] and direcoes[i][0] != i and direcoes[i][1] != i:
                break

    mago = randrange(21, 26)
    espada = randrange(11, 16)

    system('clear')
    sleep(0.5)
    print(80 * "=")
    sleep(0.5)
    print(30 * " " + "A CASA DE AKERNAAK")
    sleep(0.5)
    print(80 * "=")
    sleep(0.5)
    print("VOCÊ VOLTOU PARA CASA APÓS UM DIA DE TRABALHO. AO CHEGAR NA ENTRADA DA CASA,") 
    sleep(0.5)
    print("PORÉM, VOCÊ SENTIU QUE TUDO SE TORCIA A SUA VOLTA. ERA UMA BARREIRA AKERNAAK...")
    sleep(0.5)
    print("OS ADORADORES DE AKERNAAK TOMARAM POSSE DE SUA CASA E O ISOLARAM DO UNIVERSO.")
    sleep(0.5)
    print("QUANDO VOCÊ NAO SOUBER O QUE FAZER, INTRODUZA 'AJUDA'")
    posicao_jogador = 0 # p
    acao()

def acao():
    global entrada, selecao

    while True:
        aux = False
        sleep(0.5)
        print("VOCÊ ESTÁ N" + locais[posicao_jogador])
        aux = True

        for selecao in range(len(posicao_objetos)):
            if posicao_objetos[selecao] == posicao_jogador:
                if aux:
                    sleep(0.5)
                    print("AQUI HÁ: ", end='')
                    aux = False
                
                print("UM" + objetos[selecao] + ", ", end='')

        if not aux:
            print(2 * chr(8), end=" \n")

        if direcoes[posicao_jogador][0] != -1 and direcoes[posicao_jogador][1] != -1:
            sleep(0.5)
            print("VOCÊ PODE SE MOVER PARA " + locais[direcoes[posicao_jogador][0]] + " OU PARA " + locais[direcoes[posicao_jogador][1]])

        if vida < -6:
            sleep(0.5)
            print("VOCÊ ESTÁ FERIDO")
        elif vida < -3:
            sleep(0.5)
            print("VOCÊ ESTÁ CANSADO")
        elif vida > 1:
            sleep(0.5)
            print("VOCÊ ESTÁ SUPER-RESISTENTE")

        sleep(0.5)
        print(80 * "=")
        sleep(0.5)
        entrada = input("? ").upper()

        while entrada == "":
            sleep(0.5)
            entrada = input("? ").upper()

        for selecao in range(len(locais)):
            if locais[selecao][2:len(entrada) + 2] == entrada:
                aux = True
                movimentacao()
        
        for selecao, palavra in enumerate(vocabulario):
            if entrada == palavra:
                aux = True

                if selecao == 0:
                    fuja()
                elif selecao == 1:
                    lute()
                elif selecao == 2:
                    pegue()
                elif selecao == 3:
                    saia()
                elif selecao == 4:
                    ajuda()
                elif selecao == 5:
                    fale()
                elif selecao == 6:
                    abra()
                elif selecao == 7:
                    entre()
                elif selecao == 8:
                    liste()
                elif selecao == 9:
                    toque()
                elif selecao == 10:
                    descanse()
                elif selecao == 11:
                    desista()
                elif selecao == 12:
                    cheat()

        if not aux:
            sleep(0.5)
            print("NÃO ENTENDI ISTO")

def movimentacao():
    global inimigo_pula, inimigo_segue, selecao, posicao_jogador

    if inimigo_pula > 0:
        selecao = inimigo_pula
        sleep(0.5)
        print("O" + objetos[selecao] + " PULA SOBRE VOCÊ!")
        sub_de_luta()
        acontecimentos_possiveis()
        return

    if direcoes[posicao_jogador][0] == selecao or direcoes[posicao_jogador][1] == selecao:
        posicao_jogador = selecao
    else:
        sleep(0.5)
        print("NÃO HÁ PASSAGEM PARA " + locais[selecao])
        acontecimentos_possiveis()
        return
    
    if inimigo_segue > 0:
        posicao_objetos[inimigo_segue] = posicao_jogador
        inimigo_segue = 0

    acontecimentos_possiveis()
    return

def ajuda():
    global selecao

    sleep(0.5)
    print("O SEU OBJETIVO E LIBERTAR SUA CASA DOS AKERNAAKEN.")
    sleep(0.5)
    print("PARA SE MOVER, USE O NOME DO LOCAL PARA ONDE QUISER IR. EX: 'GARAGEM'.")
    sleep(0.5)
    print("SEU VOCABULARIO É:")
    sleep(0.5)

    for selecao in range(len(vocabulario) - 2):
        print(vocabulario[selecao] + ", ", end='')

    print(vocabulario[-2])
    acontecimentos_possiveis()
    return

def fale():
    global entrada, akon, numero_aleatorio, vida

    sleep(0.5)
    entrada = input("O QUÊ? ").upper()
    sleep(0.5)
    print("-- " + entrada + "!!")

    if entrada == "AKON":
        akon += 1

        if randrange(1, 5) > akon:
            while True:
                direcoes[posicao_jogador][0] = randrange(0, 15)
                direcoes[posicao_jogador][1] = randrange(0, 15)

                if direcoes[posicao_jogador][0] != direcoes[posicao_jogador][1] and direcoes[posicao_jogador][0] != posicao_jogador and direcoes[posicao_jogador][1] != posicao_jogador:
                    break

            sleep(0.5)
            print("VOCÊ CONSEGUIU TORCER A BERREIRA NESSE PONTO")
            acontecimentos_possiveis()
            return
        elif randrange(1, 4) == 3:
            sleep(0.5)
            print("A PALAVRA 'AKON' ORIGINOU-SE NA PRIMEIRA BARALHA ENTRE AKERNAAK E AS FORÇAS DO BEM CHEFIADAS POR WORIEL. ")
            sleep(0.5)
            print("AO PERCEBER QUE A BATALHA NÃO TERMINARIA, WORIEL PRONUNCIOU-A CINCO VEZES. O CAOS GERADO DEU ORIGEM AO UNIVERSO.")
            sleep(0.5)
            print("DECIDIRAM ENTÃO QUE ESTA PALAVRA SÓ SERIA DITA NO FIM DOS TEMPOS...")
            sleep(0.5)
            print("VOCÊ DESTRUIU O UNIVERSO...")
            fim_do_jogo()
            return
        else:
            sleep(0.5)
            print("A BARREIRA SOFREU UMA SATURAÇÃO... O UNIVERSO PODERIA TER SIDO DESTRUÍDO COM ESSE USO DE PALAVRAS MÁGICAS. FELIZMENTE SÓ VOCÊ SOFREU.")
            sleep(0.5)
            print("A CONSEQUÊNCIA DE SUA IMPRUDÊNCIA: SURGE UM DOS SETE ASTERIONS...")
            posicao_objetos[29] = posicao_jogador
            buffers_luta[9] = 8
            acontecimentos_possiveis()
            return
    elif entrada == palavra_magica and posicao_objetos[30] == posicao_jogador:
        sleep(0.5)
        print("O DRAGÃO SOME NUM VÓRTICE... SUA CASA ESTÁ LIVRE DA BARREIRA. VOCÊ VENCEU!")
        fim_do_jogo()
        return
    elif entrada.isdigit():
        if int(entrada) == numero_aleatorio:
            numero_aleatorio = 0
            sleep(0.5)
            print("VOCÊ ESTÁ SUPER-RESISTENTE POR ALGUM TEMPO")
            vida += 5
        else:
            sleep(0.5)
            print("NÃO DIGA QUALQUER NÚMERO NUMA CASA DE AKERNAAK!")
            vida -= 8

        acontecimentos_possiveis()
        return
    else:
        sleep(0.5)
        print("NADA ACONTECE...")
        acontecimentos_possiveis()
        return

def pegue():
    global entrada, selecao

    sleep(0.5)
    entrada = input("O QUÊ? ").upper()

    for selecao in range(len(objetos)):
        if (objetos[selecao][1:len(entrada) + 1] == entrada or objetos[selecao][2:len(entrada) + 2] == entrada) and posicao_objetos[selecao] == posicao_jogador:
            if selecao > 14:
                if selecao > 19:
                    sleep(0.5)
                    print("VOCÊ ESTÁ DOIDO OU VOCÊ NÃO SABE O QUE É UM" + objetos[selecao] + "?")
                else:
                    sleep(0.5)
                    print("VOCÊ NÃO PODE CARREGAR UM" + objetos[selecao])
                
                acontecimentos_possiveis()
                return

            inventario[selecao] = True
            posicao_objetos[selecao] = -1
            liste()
            return

    sleep(0.5)
    print("NÃO HÁ " + entrada + " AQUI")
    acontecimentos_possiveis()
    return

def liste():
    global selecao

    aux = True

    for selecao in range(len(inventario)):
        if inventario[selecao]:
            if aux:
                sleep(0.5)
                print("VOCÊ ESTÁ LEVANDO ", end='')
                aux = False
            
            print("UM" + objetos[selecao] + ", ", end='')

    if not aux:
        print(2 * chr(8), end=" \n")
    else:
        sleep(0.5)
        print("VOCÊ NÃO CARREGA NADA")

    acontecimentos_possiveis()
    return

def lute():
    global entrada, selecao, ataque

    sleep(0.5)
    entrada = input("COM QUEM? ").upper()

    for selecao in range(len(objetos)):
        if (objetos[selecao][1:len(entrada) + 1] == entrada or objetos[selecao][2:len(entrada) + 2] == entrada) and posicao_objetos[selecao] == posicao_jogador:
            if selecao < 20:
                sleep(0.5)
                print("VOCÊ QUER LUTAR CONTRA UM" + objetos[selecao] + "???")
            else:
                ataque = 2
                sub_de_luta()

            acontecimentos_possiveis()
            return

    sleep(0.5)
    print("NÃO HÁ " + entrada + " AQUI")
    acontecimentos_possiveis()
    return

def toque():
    global flauta

    if not inventario[10]:
        sleep(0.5)
        print("VOCÊ NÃO LEVA NENHUM INSTRUMENTO")
    else:
        sleep(0.5)
        print("VOCÊ COMEÇA A TOCAR A FLAUTA")
        flauta = True

    acontecimentos_possiveis()
    return

def fuja():
    global entrada, selecao, inimigo_pula, posicao_jogador, ataque, inimigo_segue

    sleep(0.5)
    entrada = input("PARA ONDE? ").upper()

    for selecao in range(len(locais)):
        if locais[selecao][2:len(entrada) + 2] == entrada:
            if selecao > 14:
                if selecao == 15:
                    if arca:
                        inimigo_pula = 0
                        posicao_jogador = selecao
                    else:
                        sleep(0.5)
                        print("A ARCA ESTÁ TRANCADA")
                elif selecao == 16:
                    inimigo_pula = 0
                    posicao_jogador = selecao
                elif selecao == 18:
                    inventario[4] = False
                    posicao_objetos[4] = posicao_jogador
                    inimigo_pula = 0
                    posicao_jogador = selecao
                else:
                    sleep(0.5)
                    print("VOCÊ NÃO PODE ENTRAR N" + locais[selecao])

                acontecimentos_possiveis()
                return

            if not inimigo_pula:
                movimentacao()
                return

            if randrange(1, 6) == 3:
                ataque = -2
                selecao = inimigo_pula
                sleep(0.5)
                print("VOCÊ TROPEÇA E O " + objetos[selecao] + " O ATACA PELAS COSTAS")
                sub_de_luta()
                acontecimentos_possiveis()
                return

            if randrange(1, 4) < 3:
                sleep(0.5)
                print("O" + objetos[inimigo_pula] + " O SEGUE")
                inimigo_segue = inimigo_pula

            inimigo_pula = 0
            movimentacao()
            return

    sleep(0.5)
    print("O QUE É ISSO?")
    fuja()
    return

def descanse():
    global vida

    aux = False
    sleep(0.5)
    print("VOCÊ ", end='')

    if inventario[0]:
        inventario[0] = False
        posicao_objetos[0] = posicao_jogador
        aux = True

    if inventario[1]:
        inventario[1] = False
        posicao_objetos[1] = posicao_jogador
        aux = True

    if inventario[11]:
        inventario[11] = False
        posicao_objetos[11] = posicao_jogador
        aux = True

    if aux:
        print(" LARGOU SUAS ARMAS E ", end='')

    print("ESTÁ DESCANSANDO")
    vida += 2

    if vida > 0:
        vida = 0

    acontecimentos_possiveis()
    return

def abra():
    global entrada, selecao, numero_aleatorio, palavra_magica, garrafa, arca, inimigo_pula, posicao_jogador

    sleep(0.5)
    entrada = input("O QUÊ? ").upper()

    for selecao in range(len(objetos)):
        if (objetos[selecao][1:len(entrada) + 1] == entrada or objetos[selecao][2:len(entrada) + 2] == entrada) and (posicao_objetos[selecao] == posicao_jogador or inventario[selecao]):
            if selecao == 2:
                if not inventario[selecao]:
                    sleep(0.5)
                    print("O LIVRO NÃO ESTÁ COM VOCÊ")
                else:
                    inventario[selecao] = 0
                    posicao_objetos[selecao] = randrange(0, 15)
                    sleep(0.5)
                    print("ANTES QUE O LIVRO DESAPAREÇA DE SUAS MÃOS, VOCÊ LÊ: ")
                    aux = randrange(1, 6)

                    if aux == 1:
                        numero_aleatorio = randrange(1, 101)
                        sleep(0.5)
                        print("-- O NÚMERO MÁGICO É: " + str(numero_aleatorio))
                    elif aux == 2:
                        sleep(0.5)
                        print("-- PORQUE OS MAGOS DETESTAM VINHO")
                    elif aux == 3:
                        direcoes[15][0] = randrange(0, 15)
                        sleep(0.5)
                        print("HÁ UMA PASSAGEM DA ARCA PARA " + locais[direcoes[15][0]])
                    elif aux == 4:
                        sleep(0.5)
                        print("-- 'AKON' É A PALAVRA DAS DIREÇÕES")
                    else:
                        sleep(0.5)
                        print("-- ...O PERGAMINHO QUE ESTÁ DENTRO DO DIAMANTE TEM O SEGREDO")
            elif selecao == 7:
                if not inventario[selecao]:
                    sleep(0.5)
                    print("O PERGAMINHO NÃO ESTÁ COM VOCÊ")
                else:
                    palavra_magica = "" + chr(65 + randrange(1, 4)) + chr(61 + 4 * randrange(1, 4)) + chr(73 + randrange(1, 6)) +  chr(61 + 4 * randrange(1, 4)) + chr(75 + randrange(1, 4))
                    sleep(0.5)
                    print("VOCÊ LÊ: -- A PALAVRA SECRETA É " + palavra_magica)
                    sleep(0.5)
                    print("O PERGAMINHO DESAPARECE...")
                    inventario[selecao] = False
            elif selecao == 12:
                if not inventario[selecao]:
                    sleep(0.5)
                    print("A GARRAFA NÃO ESTÁ COM VOCÊ")
                else:
                    garrafa = True
                    sleep(0.5)
                    print("A GARRAFA ESTÁ ABERTA")
            elif selecao == 15:
                if inventario[14]:
                    sleep(0.5)
                    print("VOCÊ ABRIU A ARCA", end='')
                    arca = True

                    if randrange(1, 4) == 2:
                        print(" E FOI SUGADO POR ELA. SUA CHAVE ESTÁ FORA")
                        arca = False
                        posicao_jogador = selecao
                        inventario[14] = 0
                        posicao_objetos[14] = randrange(0, 15)
                        inimigo_pula = 0
                    else:
                        print()
                else:
                    sleep(0.5)
                    print("A ARCA ESTÁ TRANCADA")
            else:
                sleep(0.5)
                print("VOCÊ NÃO PODE ABRIR UM" + objetos[selecao])

            acontecimentos_possiveis()
            return

    sleep(0.5)
    print("NÃO HÁ " + entrada + " AQUI")
    acontecimentos_possiveis()
    return

def saia():
    global inimigo_pula, posicao_jogador

    if posicao_jogador == 15:
        if randrange(1, 4) == 2:
            posicao_objetos[15] = 19
            sleep(0.5)
            print("ERA UMA EMBOSCADA...")
        else:
            if randrange(1, 6) < 3:
                posicao_objetos[15] = randrange(0, 15)
                sleep(0.5)
                print("A ARCA SE MOVEU")

        inimigo_pula = 0
        posicao_jogador = posicao_objetos[15]
    elif posicao_jogador == 18:
        posicao_jogador = posicao_objetos[4]
        inimigo_pula = 0
    else:
        sleep(0.5)
        print("O QUE VOCÊ QUER DIZER COM 'SAIR'?")

    acontecimentos_possiveis()
    return

def entre():
    global entrada, selecao, posicao_jogador, inimigo_pula

    sleep(0.5)
    entrada = input("ONDE? ").upper()

    for selecao in range(len(locais)):
        if locais[selecao][2:len(entrada) + 2] == entrada:
            if selecao < 15:
                movimentacao()
                return
            elif selecao == 15:
                if arca:
                    inimigo_pula = 0
                    posicao_jogador = selecao
                else:
                    sleep(0.5)
                    print("A ARCA ESTÁ TRANCADA")
            elif selecao == 16:
                inimigo_pula = 0
                posicao_jogador = selecao
            elif selecao == 18:
                inventario[4] = 0
                posicao_objetos[4] = posicao_jogador
                inimigo_pula = 0
                posicao_jogador = selecao
            else:
                sleep(0.5)
                print("VOCÊ NÃO PODE ENTRAR N" + locais[selecao])

            acontecimentos_possiveis()
            return

    sleep(0.5)
    print("NÃO HÁ " + entrada + " AQUI")
    acontecimentos_possiveis()
    return

def cheat():
    global selecao, vida

    for selecao in range(len(inventario)):
        inventario[selecao] = False
        posicao_objetos[selecao] = -1

    vida = 32000
    sleep(0.5)
    print("VOCÊ INVOCA OS MAGOS DO SÉTIMO REINO...")
    acontecimentos_possiveis()
    return

def acontecimentos_possiveis():
    global selecao, ataque, altar, mago, espada, dano, vida, posicao_jogador, garrafa, inimigo_pula, numero_aleatorio, flauta, tempo

    for selecao in range(20, len(objetos)):
        if posicao_objetos[selecao] == posicao_jogador and randrange(1, 11) <= buffers_luta[selecao - 20]:
            sleep(0.5)
            print("O" + objetos[selecao] + " O ATACA!")
            ataque = 0
            sub_de_luta()

    for selecao in range(20, len(objetos)):
        if inimigo_pula == 0 and randrange(1, 7) >= 4 and posicao_objetos[selecao] >= 0:
            aux = posicao_objetos[selecao]
            posicao_objetos[selecao] = direcoes[posicao_objetos[selecao]][randrange(0, 2)]

            if posicao_objetos[selecao] == -1:
                posicao_objetos[selecao] = aux
            else:
                if posicao_jogador == aux:
                    sleep(0.5)
                    print("O" + objetos[selecao] + " VAI PARA " + locais[posicao_objetos[selecao]])
                
                if posicao_objetos[selecao] == posicao_jogador:
                    sleep(0.5)
                    print("UM" + objetos[selecao] + " APARECE VINDO D" + locais[aux])

    if tempo > 30 and posicao_objetos[24] == -1 and randrange(1, 11) == 7:
        sleep(0.5)
        print("VOCÊ OUVE UM GRITO ESTRANHO...")
        posicao_objetos[24] = randrange(0, 15)

    if altar > 0:
        if posicao_objetos[18] == posicao_jogador and altar == 0:
            altar = randrange(1, 31)
            sleep(0.5)
            print("VOCÊ OUVE: -- NÃO DEVERIA TER ENTRADO AQUI, MORTAL")
        else:
            altar -= 1
    else:
        altar = 0

    if mago == 0:
        mago -= 1
        sleep(0.5)
        print("VOCÊ OUVE: -- DEMOREI A CHEGAR, MORTAL, MAS AGORA VOCÊ PAGARÁ POR TER INVADIDO O SANTUÁRIO DE AKERNAAK!")
        posicao_objetos[25] = posicao_jogador
        buffers_luta[5] = 7
    else:
        mago -= 1

    if espada > 0:
        espada -= 1

    if espada == 0 and not inventario[0]:
        posicao_objetos[0] = randrange(0, 20)

    if pontos > 100 and posicao_objetos[26] == -1 and randrange(1, 11) == 1:
        sleep(0.5)
        print("VOCÊ OUVE: -- VOCÊ JÁ CAUSOU MUITOS PROBLEMAS, VERME. SURGE UM GUERREIRO")
        posicao_objetos[26] = posicao_jogador
        acontecimentos_possiveis()
        return

    if posicao_jogador == posicao_objetos[19]:
        if randrange(1, 4) == 1:
            sleep(0.5)
            print("A ESFERA EXPLODE")
            dano = - randrange(1, 8)

            if dano < -4:
                sleep(0.5)
                print("VOCÊ FOI ATINGIDO SERIAMENTE")
                vida -= 4
            else:
                sleep(0.5)
                print("VOCÊ FOI ATINGIDO")
                vida -= 2

            posicao_objetos[19] = -1
        elif randrange(1, 5) == 3:
            sleep(0.5)
            print("A ESFERA BRILHA FORTEMENTE...")
            posicao_jogador = 19

    if posicao_jogador == posicao_objetos[16] and not inventario[13] and randrange(1, 8) == 5:
        sleep(0.5)
        print("VOCÊ OUVE: -- EU, A ESTÁTUA, SÍMBOLO DE ANIK, DOU-LHE UM PRESENTE...")
        posicao_objetos[13] = posicao_jogador

    if posicao_jogador == posicao_objetos[26] and inventario[13] and buffers_luta[6] > 0:
        sleep(0.5)
        print("VOCÊ OUVE: -- EU, O GUERREIRO DE ANIK, SAÚDO O PORTADOR DO CETRO")
        buffers_luta[6] = 0

    if garrafa and posicao_jogador == posicao_objetos[25]:
        sleep(0.5)
        print("VOCÊ OUVE: -- FRAAAAGH! NYOK! O CHEIRO DO VINHO ", end='')

        if randrange(1, 5) == 3:
            print("ENFURECE O MAGO")
            buffers_luta[5] = 9
        else:
            print("ENFRAQUECE O MAGO")
            vida_inimigos[5] -= 4

        sleep(0.5)
        print("ELE QUEBRA SU" + objetos[12])
        inventario[12] = False
        garrafa = 0

    if tempo > 60 and posicao_objetos[17] == -1 and randrange(1, 6) == 1:
        posicao_objetos[17] = randrange(0, 15)

    if pontos > 200 and posicao_objetos[28] == 18 and randrange(1, 9) == 3:
        sleep(0.5)
        print("VOCÊ OUVE: -- ATÉ AGORA VOCÊ ENFRENTOU OS APRENDIZES, MEU CARO...")
        buffers_luta[8] = 7
        posicao_objetos[28] = posicao_jogador

    if inventario[6] and posicao_objetos[28] == posicao_jogador:
        sleep(0.5)
        print("SEU ESPELHO DRENA UM POUCO DA MAGIA DO MESTRE")
        vida_inimigos[8] -= 2

    if posicao_jogador == 14 and randrange(1, 11) == 8:
        sleep(0.5)
        print("DO ALTO DO MURO SURGE UMA LUZ CINZA")
        posicao_jogador = 15
        inimigo_pula = 0

    if posicao_objetos[17] != -1 and randrange(1, 11) == 6:
        sleep(0.5)
        print("VOCÊ OUVE: -- " + objetos[17] + " ESTÁ N" + locais[posicao_objetos[17]])

    if numero_aleatorio == 0 and posicao_jogador == 7 and randrange(1, 21) == 2:
        numero_aleatorio = randrange(1, 101)
        sleep(0.5)
        print("VOCÊ LÊ NUMA CARTA DE BARALHO: O NÚMERO MÁGICO É " + str(numero_aleatorio))

    if vida < 0:
        vida += 1

        if inventario[11] and vida < -1:
            sleep(0.5)
            print("VOCÊ SE RECUPERA MAIS DEPRESSA, GRAÇAS A SEU ELMO MÁGICO")
            vida += 2

    flauta = False
    tempo += 1

    if tempo % 10 == 0:
        sleep(0.5)
        print("TEMPO = " + str(tempo) + " MINUTOS")

    return

def sub_de_luta():
    global selecao, inimigo_pula, ataque, vida, espada, dano, pontos, posicao_jogador

    if selecao != 0:
        inimigo_pula = selecao

        if flauta:
            sleep(0.5)
            print("VOCÊ ESTÁ TOCANDO A FLAUTA")
        else:
            sleep(0.5)
            print("VOCÊ O ATACA COM ", end='')

            if inventario[0]:
                print("SUA ESPADA", end='')
                ataque += 2
            else:
                print("SOCOS E PONTAPÉS", end='')

            if inventario[1]:
                ataque += 1
                print(" E SE DEFENDE COM SEU ESCUDO")
            else:
                print()

            if inventario[3] and selecao > 26:
                sleep(0.5)
                print("SUA CAPA O PROTEGE DOS GOLPES MÁGICOS MAIS FORTES DO" + objetos[selecao])
                ataque += 2 * (selecao - 26)

        if selecao == 20:
            if randrange(1, 5) == 3:
                sleep(0.5)
                print("ELE SE ASSUSTA COM SUA FÚRIA E DESAPARECE EM MEIO A UMA FUMAÇA VERDE")
                inimigo_pula = 0

                while True:
                    aux = randrange(0, 15)

                    if aux != posicao_objetos[20]:
                        break

                posicao_objetos[20] = aux
                return
        elif selecao == 22:
            if flauta:
                sleep(0.5)
                print("ELE FICA ENFEITIÇADO COM A EXÓTICA MÚSICA QUE SAI DA SUA FLAUTA NIDDUN E SE ACALMA")
                inimigo_pula = 0
                return
        elif selecao == 23:
            if randrange(1, 5) == 2:
                sleep(0.5)
                print("ELE GESTICULA E TUDO ESCURECE MOMENTANEAMENTE")

                if inventario[9]:
                    ataque += 2
                    sleep(0.5)
                    print("MESMO COM SUA LANTERNA É DIFÍCIL ENXERGAR")
                else:
                    ataque -= 5

        elif selecao == 24:
            if randrange(1, 4) == 1:
                sleep(0.5)
                print("O PITON O ENCARA, TENTANDO ROUBAR SUA ENERGIA")
                vida -= randrange(1, 4)
                return

        elif selecao == 25:
            if randrange(1, 6) == 3:
                sleep(0.5)
                print("ELE FAZ UM GESTO ESTRANHO")

                if inventario[0]:
                    sleep(0.5)
                    print("SUA ESPADA DERRETE...")
                    inventario[0] = False
                    espada = randrange(11, 16)
                    return
                else:
                    sleep(0.5)
                    print("VOCÊ SENTE TONTURAS...")
                    ataque -= 2

        elif selecao == 27:
            if randrange(1, 5) == 4:
                direcoes[posicao_jogador][0] = 19
                direcoes[posicao_jogador][1] = -1
                sleep(0.5)
                print("VOCE OUVE A GARGALHADA DO" + objetos[selecao] + ": -- MORTAL, VOCÊ ME SOLTOU, MAS CONSTRUIU SUA PRISÃO... ELE VAI PARA " + locais[posicao_objetos[27]])
                inimigo_pula = 0
                return

    dano = vida - vida_inimigos[selecao - 20] + ataque - tempo // 50 - 2 * (selecao - 20) + randrange(1, 6)

    if dano < -7:
        sleep(0.5)
        print("INFELIZMENTE, MEU CARO, VOCÊ MORRE...")
        fim_do_jogo()

    if dano < -4:
        sleep(0.5)
        print("VOCÊ FOI ATINGIDO SERIAMENTE")
        vida -= 4
        return

    if dano < 1:
        sleep(0.5)
        print("VOCÊ FOI ATINGIDO")
        vida -= 2
        return

    inimigo_pula = 0

    if dano < 4:
        sleep(0.5)
        print("VOCÊ O ATINGIU")
        vida_inimigos[selecao - 20] -= 1
        return

    if dano < 7:
        sleep(0.5)
        print("VOCÊ O ATINGIU GRAVEMENTE")
        vida_inimigos[selecao - 20] -= 3
        return

    sleep(0.5)
    print("VOCÊ O MATOU")
    posicao_objetos[selecao] = -2
    pontos += 20 * (selecao - 20)

    if selecao == 23:
        if randrange(1, 4) == 1:
            sleep(0.5)
            print("UMA LUZ ESTRANHA SURGE, O ELFO ESTÁ RESSUCITADO. E FURIOSO!!!")
            vida_inimigos[3] = 5
            posicao_objetos[selecao] = posicao_jogador
        else:
            sleep(0.5)
            print("NO LUGAR DO CORPO DO ELFO APARECE UMA ESFERA")
            posicao_objetos[19] = posicao_jogador
    elif selecao == 28 or selecao == 29:
        sleep(0.5)
        print("VOCÊ CAI INCONSCIENTE... AO ACORDAR, VOCÊ PERCEBE QUE NÃO ESTÁ MAIS N" + locais[posicao_jogador] + ".")
        sleep(0.5)
        print("VOCÊ OUVE: -- QUEM OUSA DESAFIAR YDYAK, O DRAGÃO, ATACANDO SEUS SERVOS?")
        posicao_jogador = 17
        posicao_objetos[30] = 17
    elif selecao == 30:
        sleep(0.5)
        print("O DRAGÃO SOME NUM VÓRTICE... SUA CASA ESTÁ LIVRE DA BARREIRA. VOCÊ VENCEU!")
        fim_do_jogo()

    return

def desista():
    global entrada

    sleep(0.5)
    entrada = input("VOCÊ QUER DESISTIR DO JOGO? ").upper()

    if entrada == "SIM"[0:len(entrada)]:
        fim_do_jogo()
        return

    acontecimentos_possiveis()
    return

def fim_do_jogo():
    global pontos, entrada

    if inventario[4]:
        pontos += 100

    if inventario[5]:
        pontos += 30

    if inventario[8]:
        pontos += 15

    if inventario[13]:
        pontos += 50

    sleep(0.5)
    print("O JOGO TERMINOU. VOCÊ FEZ " + str(pontos) + " PONTOS")
    sleep(0.5)
    entrada = input("VOCÊ QUER RECOMEÇAR? ").upper()

    if entrada == "SIM"[0:len(entrada)]:
        novo_jogo()
    else:
        exit(0)

if __name__ == '__main__':
    novo_jogo()

# TODO 
# COLOCAR ACENTO EM ESTÁTUA
# TIRAR AKERNAAK DO VOCABULÁRIO E COLOCAR EM FALE()