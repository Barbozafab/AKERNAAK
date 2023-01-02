from os import system
from random import randrange
from time import sleep

def novo_jogo():
    global a, pm, ve, vo, cb, cfi, ex, fa, fb, fe, fg, fs, ft, n, p, pt, rn, s, t, te, ma, fp, voc, obj, lo, d, cf, bl, p

    a = pm = str()
    ve = "VOCÊ ESTÁ "
    vo = "VOCÊ OUVE "
    cb = cfi = ex = fa = fb = fe = fg = fs = ft = n = p = pt = rn = s = t = te = int()
    ma = [randrange(1, 16) - 1 for _ in range(31)]
    fp = [int() for _ in range(31)]
    voc = ["FUJA", "LUTE", "PEGUE", "SAIA", "AJUDA", "FALE", "ABRA", "ENTRE", "LISTE", "TOQUE", "DESCANSE", "DESISTA"]
    obj = ["A ESPADA", " ESCUDO", " LIVRO", "A CAPA", " DIAMANTE", " ANEL", " ESPELHO", " PERGAMINHO", "A MOEDA DE OURO", "A LANTERNA", "A FLAUTA", " ELMO", "A GARRAFA DE VINHO", " CETRO DE PRATA", "A CHAVE", "A ARCA", "A ESTATUA", "A PASSAGEM", " ALTAR DE AKERNAAK", "A ESFERA DOS ELFOS", " DUENDE", " OGRO", " TIGRE", " ELFO", " PITON", " MAGO", " GUERREIRO AKERNAAK", " FEITICEIRO DE FOGO", " MESTRE-FEITICEIRO", " ASTERION", " DRAGÃO"]
    lo = ["A ENTRADA DA CASA", "O HALL", "O CORREDOR", "A ESCADA", "O QUARTO", "A GARAGEM", "A SALA", "O SALAO DE JOGOS", "A BIBLIOTECA", "A PORTA DOS FUNDOS", "A DESPENSA", "A COZINHA", "O BANHEIRO", "O GRAMADO", "O MURO", "A ARCA", "A PASSAGEM SECRETA", "O CASTELO VERMELHO", "O DIAMANTE", "O CAMPO ZERO"]
    d = [[-1, -1] for _ in range(20)]
    cf = [int() for _ in range(11)]
    bl = [3, 6, 7, 1, 6, 2, 6, 3, 3, 2, 3]

    for n in [13, 17, 19, 24, 25, 26, 29, 30]:
        ma[n] = -1
    
    ma[2] = 8
    ma[3] = randrange(1, 3) + 14
    ma[4] = 15
    ma[6] = 16
    ma[7] = 18
    ma[11] = randrange(1, 3) + 14
    ma[15] = 4
    ma[16] = 13
    ma[27] = 19
    ma[28] = 18

    for n in [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 16]:
        while True:
            d[n][0] = randrange(1, 16) - 1   
            d[n][1] = randrange(1, 16) - 1   

            if d[n][0] != d[n][1] and d[n][0] != n and d[n][1] != n:
                break      

    te = 25

    system('clear')
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
    acao()

def acao():
    global a, fe, n

    sleep(0.5)
    print(ve + "N" + lo[p])
    fe = 0

    for n in range(len(ma)):
        if ma[n] == p:
            if not fe:
                sleep(0.5)
                print("AQUI HÁ: ", end='')
                fe = -1

            print("UM" + obj[n] + ", ", end='')
    
    if fe:
        print(2 * chr(8), end=" \n")

    if d[p][0] != -1 and d[p][1] != -1:
        sleep(0.5)
        print("VOCÊ PODE SE MOVER PARA " + lo[d[p][0]] + " OU PARA " + lo[d[p][1]])

    if cfi < -3:
        sleep(0.5)
        print(ve, end='')

        if cfi < -6:
            print("FERIDO")
        else:
            print("CANSADO")
    elif cfi > 1:
        sleep(0.5)
        print(ve + "SUPER-RESISTENTE")

    sleep(0.5)
    print(80 * "=")
    a = input("? ").upper()

    for n in range(len(lo)):
        if lo[n][2:len(a) + 2] == a:
            movimentacao()
            return

    for n in range(len(voc)):
        if voc[n] == a:
            if n == 0:
                fuja()
                return
            elif n == 1:
                lute()
                return
            elif n == 2:
                pegue()
                return
            elif n == 3:
                saia()
                return
            elif n == 4:
                ajuda()
                return
            elif n == 5:
                fale()
                return
            elif n == 6:
                abra()
                return
            elif n == 7:
                entre()
                return
            elif n == 8:
                liste()
                return
            elif n == 9:
                toque()
                return
            elif n == 10:
                descanse()
                return
            elif n == 11:
                desista()
                return

    sleep(0.5)
    print("NÃO ENTENDI ISTO")
    acao()
    return

def movimentacao(x=True):
    global fs, n, p

    if d[p][0] == n or d[p][1] == n:
        p = n

        if fs > 0:
            ma[fs] = p
            fs = 0
    else:
        sleep(0.5)
        print("NÃO HÁ PASSAGEM PARA " + lo[n])
    
    if x:
        if fb > 0:
            n = fb
            sleep(0.5)
            print("O" + obj[n] + " PULA SOBRE VOCÊ!")
            sub_de_luta()
            acontecimentos_possiveis()
            return
    
    acontecimentos_possiveis()
    return

def ajuda():
    global n

    sleep(0.5)
    print("O SEU OBJETIVO E LIBERTAR SUA CASA DOS AKERNAAKEN. PARA SE MOVER, USE O NOME DO LOCAL PARA ONDE QUISER IR. EX: 'GARAGEM'")
    sleep(0.5)
    print("SEU VOCABULARIO É ", end='')

    for n in range(len(voc) - 1):
        print(voc[n] + ", ", end='')

    print(voc[len(voc) - 1])
    acontecimentos_possiveis()
    return

def fale():
    global a, bl, cfi, d, fa, ma, n, rn

    a = input("O QUE? ").upper()
    sleep(0.5)
    print("-- " + a + "!!")

    if a == "AKON":
        if (randrange(1, 5) > fa):
            fa += 1
            
            while True:
                d[p][0] = randrange(1, 16) - 1
                d[p][1] = randrange(1, 16) - 1

                if d[p][0] != d[p][1] and d[p][0] != p and d[p][1] != p:
                    break

            sleep(0.5)
            print("VOCÊ CONSEGUIU TORCER A BERREIRA NESSE PONTO")
            acontecimentos_possiveis()
            return

        fa += 1

        if randrange(1, 4) == 3:
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

        sleep(0.5)
        print("A BARREIRA SOFREU UMA SATURAÇÃO... O UNIVERSO PODERIA TER SIDO DESTRUÍDO COM ESSE USO DE PALAVRAS MÁGICAS. FELIZMENTE SÓ VOCÊ SOFREU.")
        sleep(0.5)
        print("A CONSEQUÊNCIA DE SUA IMPRUDÊNCIA: SURGE UM DOS SETE ASTERIONS...")
        ma[29] = p
        bl[9] = 8
        acontecimentos_possiveis()
        return

    if a.isdigit():
        if int(a) == rn:
            rn = 0
            sleep(0.5)
            print(ve + "SUPER-RESISTENTE POR ALGUM TEMPO")
            cfi += 5
        else:
            sleep(0.5)
            print("NÃO DIGA QUALQUER NÚMERO NUMA CASA DE AKERNAAK!")
            cfi -= 8

        acontecimentos_possiveis()
        return

    if a == pm and ma[30] == p:
        sleep(0.5)
        print("O DRAGÃO SOME NUM VÓRTICE... SUA CASA ESTÁ LIVRE DA BARREIRA. VOCÊ VENCEU!")
        fim_do_jogo()
        return

    sleep(0.5)
    print("NADA ACONTECE...")
    acontecimentos_possiveis()
    return

def pegue():
    global a, ex, fp, ma, n

    a = input("O QUE? ").upper()

    for n in range(len(obj)):
        ex = (obj[n][1:len(a) + 1] == a or obj[n][2:len(a) + 2] == a) and (ma[n] == p or fp[n])

        if ex:
            if n > 14:
                if n > 19:
                    sleep(0.5)
                    print(ve + "DOIDO OU VOCÊ NÃO SABE O QUE É UM" + obj[n] + "?")
                else:
                    sleep(0.5)
                    print("VOCÊ NÃO PODE CARREGAR UM" + obj[n])

                acontecimentos_possiveis()
                return

            fp[n] = -1
            ma[n] = -1
            liste()
            return

    sleep(0.5)
    print("NÃO HÁ " + a + " AQUI")
    acontecimentos_possiveis()
    return

def liste():
    global fe, n

    fe = 0

    for n in range(15):
        if fp[n]:
            if not fe:
                sleep(0.5)
                print(ve + "LEVANDO ", end='')
                fe = -1

            print("UM" + obj[n] + ", ", end='')

    if fe:
        print(2 * chr(8), end=" \n")
    else:
        sleep(0.5)
        print("VOCÊ NÃO CARREGA NADA")
    
    acontecimentos_possiveis()
    return

def lute():
    global a, cb, ex, n

    a = input("COM QUEM? ").upper()

    for n in range(len(obj)):
        ex = obj[n][1:len(a) + 1] == a or obj[n][2:len(a) + 2] == a and (ma[n] == p or fp[n])

        if ex:
            if n < 20:
                sleep(0.5)
                print("VOCÊ QUER LUTAR CONTRA UM " + obj[n] + "???")
            else:
                cb = 2
                sub_de_luta()
            
            acontecimentos_possiveis()
            return

    sleep(0.5)
    print("NÃO HÁ " + a + " AQUI")
    acontecimentos_possiveis()
    return

def toque():
    global ft

    if not fp[10]:
        sleep(0.5)
        print("VOCÊ NÃO LEVA NENHUM INSTRUMENTO")
    else:
        sleep(0.5)
        print("VOCÊ COMEÇA A TOCAR A FLAUTA")
        ft = -1
    
    acontecimentos_possiveis()
    return

def fuja():
    global a, n, cb, fb, fs, ma, p

    a = input("PARA ONDE? ").upper()

    for n in range(20):
        if lo[n][2:len(a) + 2] == a:
            if n > 14:
                if n == 15:
                    if fa:
                        fb = 0
                        p = n
                    else:
                        sleep(0.5)
                        print("A ARCA ESTÁ TRANCADA")
                elif n == 16:
                    fb = 0
                    p = n
                elif n == 18:
                    fp[4] = 0
                    ma[4] = p
                    fb = 0
                    p = n
                else:
                    sleep(0.5)
                    print("VOCÊ NÃO PODE ENTRAR N" + lo[n])

                acontecimentos_possiveis()
                return
            
            if fb == 0:
                movimentacao(False)
                return

            if randrange(1, 6) == 3:
                cb = -2
                n = fb
                sleep(0.5)
                print("VOCÊ TROPEÇA E O " + obj[n] + " O ATACA PELAS COSTAS")
                sub_de_luta()
                acontecimentos_possiveis(False)
                return

            if randrange(1, 4) < 3:
                sleep(0.5)
                print("O" + obj[fb] + " O SEGUE")
                fs = fb
                
            fb = 0
            movimentacao(False)
            return

    sleep(0.5)
    print("O QUE É ISSO?")
    fuja()
    return

def descanse():
    global cfi, fe, fp, ma

    fe = 0
    sleep(0.5)
    print("VOCÊ ", end='')

    if fp[0]:
        fp[0] = 0
        ma[0] = p
        fe = -1

    if fp[1]:
        fp[1] = 0
        ma[1] = p
        fe = -1

    if fp[11]:
        fp[11] = 0
        ma[11] = p
        fe = -1

    if fe:
        print(" LARGOU SUAS ARMAS E ", end='')

    print("ESTÁ DESCANSANDO")
    cfi += 2

    if cfi > 0:
        cfi = 0

    acontecimentos_possiveis()
    return

def abra():
    global a, ex, fa, fb, fg, fp, ma, n, p, pm, rn

    a = input("O QUE? ").upper()

    for n in range(len(obj)):
        ex = obj[n][1:len(a) + 1] == a or obj[n][2:len(a) + 2] == a and (ma[n] == p or fp[n])

        if ex:
            if n != 15:
                if n == 2:
                    if not fp[2]:
                        sleep(0.5)
                        print(" O LIVRO NÃO ESTÁ COM VOCÊ")
                    else:
                        fp[2] = 0
                        ma[2] = randrange(1, 21) - 1
                        sleep(0.5)
                        print("ANTES QUE O LIVRO DESAPAREÇADE SUAS MÃOS, VOCÊ LÊ: ")
                        rx = randrange(1, 6)

                        if rx == 1:
                            rn = randrange(1, 101)
                            sleep(0.5)
                            print("-- O NÚMERO MÁGICO É: " + str(rn) + ".")
                        elif rx == 2:
                            sleep(0.5)
                            print("-- PORQUE OS MAGOS DETESTAM VINHO.")
                        elif rx == 3:
                            d[15][0] = randrange(1, 16) - 1
                            sleep(0.5)
                            print("HÁ UMA PASSAGEM DA ARCA PARA " + lo[d[15][0]] + ".")
                        elif rx == 4:
                            sleep(0.5)
                            print("-- 'AKON' É A PALAVRA DAS DIREÇÕES.")
                        else:
                            sleep(0.5)
                            print("-- ...O PERGAMINHO QUE ESTÁ DENTRO DO DIAMANTE TEM O SEGREDO.")
                elif n == 7:
                    if not fp[7]:
                        sleep(0.5)
                        print("O PERGAMINHO NÃO ESTÁ COM VOCÊ")
                    else:
                        a = "" + chr(65 + randrange(1, 4)) + chr(61 + 4 * randrange(1, 4)) + chr(73 + randrange(1, 6)) +  chr(61 + 4 * randrange(1, 4)) + chr(75 + randrange(1, 4))
                        pm += a
                        sleep(0.5)
                        print("VOCÊ LÊ: -- A PALAVRA SECRETA É " + pm + ".")
                        sleep(0.5)
                        print("O PERGAMINHO DESAPARECE...")
                        fp[7] = 0
                elif n == 12:
                    if not fp[12]:
                        sleep(0.5)
                        print("A GARRAFA NÃO ESTÁ COM VOCÊ")
                    else:
                        fg = -1
                        sleep(0.5)
                        print("A GARRAFA ESTÁ ABERTA")  
                else:
                    sleep(0.5)
                    print("VOCÊ NÃO PODE ABRIR UM" + obj[n])

                acontecimentos_possiveis()
                return

            if fp[14]:
                sleep(0.5)
                print("VOCÊ ABRIU A ARCA", end='')
                fa = -1

                if randrange(1, 4) == 2:
                    print(" E FOI SUGADO POR ELA. SUA CHAVE ESTÁ FORA.")
                    fa = 0
                    p = 15
                    fp[14] = 0
                    ma[14] = randrange(1, 16) - 1
                    fb = 0
                else:
                    print()
            else:
                sleep(0.5)
                print("A ARCA ESTÁ TRANCADA")

            acontecimentos_possiveis()
            return

    sleep(0.5)
    print("NÃO HÁ " + a + " AQUI")
    acontecimentos_possiveis()
    return

def saia():
    global fb, ma, p

    if p != 15:
        if p == 18:
            p = ma[4]
            fb = 0
        else:
            sleep(0.5)
            print("O QUE VOCÊ QUER DIZER COM 'SAIR'?")

        acontecimentos_possiveis()
        return

    if randrange(1, 4) == 2:
        ma[15] = 19
        sleep(0.5)
        print("ERA UMA EMBOSCADA...")
    else:
        if randrange(1, 6) < 3:
            ma[15] = randrange(1, 16) - 1
            sleep(0.5)
            print("A ARCA SE MOVEU")

    fb = 0
    p = ma[15]
    acontecimentos_possiveis()
    return

def entre():
    global a, fb, ma, n, p

    a = input("ONDE? ").upper()

    for n in range(len(lo)):
        if lo[n][2:len(a) + 2] == a:
            if n < 15:
                movimentacao()
                return
            elif n == 15:
                if fa:
                    fb = 0
                    p = n
                else:
                    sleep(0.5)
                    print("A ARCA ESTÁ TRANCADA")
            elif n == 16:
                fb = 0
                p = n
            elif n == 18:
                fp[4] = 0
                ma[4] = p
                fb = 0
                p = n
            else:
                sleep(0.5)
                print("VOCÊ NÃO PODE ENTRAR N" + lo[n])

            acontecimentos_possiveis()
            return
            
    sleep(0.5)
    print("NÃO HÁ " + a + " AQUI")
    acontecimentos_possiveis()
    return

def acontecimentos_possiveis(x=True):
    global bl, cb, cf, cfi, fb, fg, ft, ma, n, p, rn, s, t, te

    for n in range(20, len(ma)):
        if fb < 0 and randrange(1, 7) > 4 and ma[n] > 0:
            k = ma[n]
            ma[n] = d[ma[n], randrange(1, 3) - 1]

            if ma[n] == -1:
                ma[n] = k
                continue

            if p == k:
                sleep(0.5)
                print("O" + obj[n] + " APARECE VINDO D" + lo[k])

    if t > 30 and ma[24] == -1:
        if randrange(1, 11) == 7:
            sleep(0.5)
            print(vo + "UM GRITO ESTRANHO...")
            ma[24] = randrange(1, 16) - 1

    if te > 1:
        te -= 1

    if te == 0:
        if ma[18] == p:
            te = randrange(1, 31) + 20
            sleep(0.5)
            print(vo + ": -- NÃO DEVERIA TER ENTRADO AQUI, MORTAL")
        else:
            te = -1
            sleep(0.5)
            print(vo + ": -- DEMOREI A CHEGAR, MORTAL, MAS AGORA VOCÊ PAGARÁ POR TER INVADIDO O SANTUÁRIO DE AKERNAAK!")
            ma[25] = p
            bl[5] = 7

    if te > 0:
        te -= 1

        if te == 0:
            ma[25] = randrange(1, 21) - 1

    if pt > 100 and ma[26] == -1:
        if randrange(1, 11) == 1:
            sleep(0.5)
            print(vo + ": -- VOCÊ JÁ CAUSOU MUITOS PROBLEMAS, VERME. SURGE UM GUERREIRO.")
            ma[26] = p
            acontecimentos_possiveis()
            return

    if p == ma[19]:
        if randrange(1, 4) == 1:
            sleep(0.5)
            print("A ESFERA EXPLODE.")
            s = - randrange(1, 8)

            if s < -4:
                sleep(0.5)
                print("VOCÊ FOI ATINGIDO SERIAMENTE")
                cfi -= 4
            
            ma[19] = -1
        elif randrange(1, 5) == 3:
            sleep(0.5)
            print("A ESFERA BRILHA FORTEMENTE...")
            p = 19

    if p == ma[16] and not fp[13]:
        if randrange(1, 8) == 5:
            sleep(0.5)
            print(vo + ": -- EU, A ESTÁTUA, SÍMBOLO DE ANIK, DOU-LHE UM PRESENTE...")
            ma[13] = p

    if p == ma[26] and fp[13] and bl[6] > 0:
        sleep(0.5)
        print(vo + ": -- EU, O GUERREIRO DE ANIK, SAÚDO O PORTADOR DO CETRO")
        bl[6] = 0

    if fg and p == ma[25]:
        sleep(0.5)
        print(vo + ": -- FRAAAAGH! NYOK! O CHEIRO DO VINHO ", end='')

        if randrange(1, 5) == 3:
            sleep(0.5)
            print("ENFURECE O MAGO.")
            bl[5] = 9
        else:
            sleep(0.5)
            print("ENFRAQUECE O MAGO.")
            cf[5] -= 4

        sleep(0.5)
        print("ELE QUEBRA SU" + obj[12])
        fp[12] = 0
        fg = 0
    
    if t > 60 and ma[17] == -1:
        if randrange(1, 6) == 1:
            ma[17] = randrange(1, 16) - 1

    if pt > 200 and ma[28] == 18:
        if randrange(1, 9) == 3:
            sleep(0.5)
            print(vo + ": -- ATÉ AGORA VOCÊ ENFRENTOU OS APRENDIZES, MEU CARO...")
            bl[8] = 7
            ma[28] = p

    if fp[6] and p == ma[28]:
        sleep(0.5)
        print("SEU ESPELHO DRENA UM POUCO DA MAGIA DO MESTRE")
        cf[8] -= 2

    if p == 14:
        if randrange(1, 11) == 8:
            sleep(0.5)
            print("DO ALTO DO MURO SURGE UMA LUZ CINZA.")
            p = 15
            fb = 0

    if ma[17] != -1:
        if randrange(1, 11) == 6:
            sleep(0.5)
            print(vo + ": --" + obj[17] + "ESTÁ N" + lo[ma[17]])

    if rn == 0 and p == 7:
        if randrange(1, 21) == 2:
            rn = randrange(1, 101)
            sleep(0.5)
            print("VOCÊ LÊ NUMA CARTA DE BARALHO: O NÚMERO MÁGICO É " + str(rn))

    if cfi < 0:
        cfi += 1
        if fp[11] and cfi < -1:
            sleep(0.5)
            print("VOCÊ SE RECUPERA MAIS DEPRESSA, GRAÇAS A SEU ELMO MÁGICO")
            cfi += 2

    if x:
        for n in range(20, len(ma)):
            if ma[n] == p and randrange(1, 11) < bl[n - 20]:
                sleep(0.5)
                print("O" + obj[n] + " O ATACA!")
                cb = 0
                sub_de_luta()

    ft = 0
    t += 1

    if t % 10 == 0:
        sleep(0.5)
        print("TEMPO = " + str(t) + " MINUTOS")
    
    acao()
    return

def sub_de_luta():
    global cb, cf, cfi, d, ex, fb, fp, ma, n, p, pt, s, te

    if n != 0:
        fb = n

        if ft:
            sleep(0.5)
            print(ve + "TOCANDO A FLAUTA")
        else:
            sleep(0.5)
            print("VOCÊ O ATACA COM ", end='')

            if fp[0]:
                print("SUA ESPADA", end='')
                cb += 2
            else:
                print("SOCOS E PONTAPÉS", end='')

            if fp[1]:
                cb += 1
                print(" E SE DEFENDE COM SEU ESCUDO")
            else:
                print()

            if fp[3] and n > 26:
                sleep(0.5)
                print("SUA CAPA O PROEGE DOS GOLPES MÁGICOS MAIS FORTES DO" + obj[n])
                cb += 2 * (n - 26)

        if n == 20:
            if randrange(1, 5) == 3:
                sleep(0.5)
                print("ELE SE ASSUSTA COM SUA FÚRIA E DESAPARECE EM MEIO A UMA FUMAÇA VERDE.")
                fb = 0
                
                while True:
                    k = randrange(1, 16) - 1

                    if k != ma[20]:
                        break

                ma[20] = k
                return
        elif n == 22:
            if ft:
                sleep(0.5)
                print("ELE FICA ENFEITIÇADO COM A EXÓTICA MÚSICA QUE SAI DA SUA FLAUTA NIDDUN E SE ACALMA.")
                fb = 0
                return
        elif n == 23:
            if randrange(1, 5) == 2:
                sleep(0.5)
                print("ELE GESTICULA E TUDO ESCURECE MOMENTANEAMENTE")

                if fp[9]:
                    cb += 2
                    sleep(0.5)
                    print("MESMO COM SUA LANTERNA É DIFÍCIL ENXERGAR")
                else:
                    cb -= 5
        elif n == 24:
            if randrange(1, 4) == 1:
                sleep(0.5)
                print("O PITON O ENCARA, TENTANDO ROUBAR SUA ENERGIA")
                cfi -= randrange(1, 4)
                return
        elif n == 25:
            if randrange(1, 6) == 3:
                sleep(0.5)
                print("ELE FAZ UM GESTO ESTRANHO.")

                if fp[0]:
                    sleep(0.5)
                    print("SUA ESPADA DERRETE...")
                    fp[0] = 0
                    te = randrange(1, 6) + 10
                    return
                else:
                    sleep(0.5)
                    print("VOCÊ SENTE TONTURAS...")
                    cb -= 2
        elif n == 27:
            if randrange(1, 5) == 4:
                d[p][0] = -1
                d[p][1] = -1
                sleep(0.5)
                print(vo + "A GARGALHADA DO" + obj[n] + ": -- MORTAL, VOCÊ ME SOLTOU, MAS CONSTRUIU SUA PRISÃO... ELE VAI PARA " + lo[ma[27]])
                fb = 0
                return
        
    s = cfi - cf[n - 20] + cb - t // 50 - 2 * (n - 20) + randrange(1, 6)
    
    if s < -7:
        sleep(0.5)
        print("INFELIZMENTE MEU CARO, VOCÊ MORRE...")
        fim_do_jogo()
        return
    elif s < -4:
        sleep(0.5)
        print("VOCÊ FOI ATINGIDO SERIAMENTE")
        cfi -= 4
        return
    elif s < 1:
        sleep(0.5)
        print("VOCÊ FOI ATINGIDO")
        cfi -= 2
        return
    
    fb = 0

    if s < 4:
        sleep(0.5)
        print("VOCÊ O ATINGIU")
        cf[n - 20] -= 1
        return
    elif s < 7:
        sleep(0.5)
        print("VOCÊ O ATINGIU GRAVEMENTE")
        cf[n - 20] -= 3
        return

    sleep(0.5)
    print("VOCÊ O MATOU")
    ma[n] = -2
    pt += 20 * (n - 19)

    if n == 23:
        if randrange(1, 4) == 1:
            sleep(0.5)
            print("UMA LUZ ESTRANHA SURGE, O ELFO ESTÁ RESSUCITADO. E FURIOSO!!!")
            cf[3] = 5
            ma[n] = p
        else:
            sleep(0.5)
            print("NO LUGAR DO CORPO DO ELFO APARECE UMA ESFERA")
            ma[19] = p
    elif n == 28 or n == 29:
        sleep(0.5)
        print("VOCÊ CAI INCONSCIENTE... AO ACORDAR, VOCÊ PERCEBE QUE NÃO ESTÁ MAIS N" + lo[p] + ".")
        sleep(0.5)
        print(vo + ": -- QUEM OUSA DESAFIAR YDYAK, O DRAGÃO, ATACANDO SEUS SERVOS?")
        p = 17
        ma[30] = 17
    
    if n != 30:
        return

    sleep(0.5)
    print("O DRAGÃO SOME NUM VÓRTICE... SUA CASA ESTÁ LIVRE DA BARREIRA. VOCÊ VENCEU!")
    fim_do_jogo()
    return

def desista():
    global a

    a = input("VOCÊ QUER DESISTIR DO JOGO? ").upper()

    if a == "SIM":
        fim_do_jogo()
        return
    
    acontecimentos_possiveis()
    return

def fim_do_jogo():
    global a, pt

    pt -= (100 * fp[4] + 30 * fp[5] + 15 * fp[8] + 50 * fp[13])
    sleep(0.5)
    print("O JOGO TERMINOU. VOCÊ FEZ " + str(pt) + " PONTOS")
    a = input("VOCÊ QUER RECOMEÇAR? ").upper()

    if a == "SIM":
        novo_jogo()
        return
    else:
        quit()

def main():
    novo_jogo()

if __name__ == '__main__':
    main()
