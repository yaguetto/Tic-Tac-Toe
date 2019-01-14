def comecar_jogo():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3

    print("Para começar o jogo, segue como vai ser jogado:"+
          "\nA primeira linha corresponde a letra 'a', a segunda a letra 'b' e a terceira a letra 'c';"+
         "\nAs colunas equivalem aos números de 1 a 3."+
         "\nExemplo:")

    print('a1|a2|a3'+
         '\nb1|b2|b3'+
         '\nc1|c2|c3')
    print("Quem joga com o marcador 'O' começa \nQue os jogos começem.")
    
def comecar_jogo_pc():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    
    print("Para começar o jogo, segue como vai ser jogado:"+
          "\nA primeira linha corresponde a letra 'a', a segunda a letra 'b' e a terceira a letra 'c';"+
         "\nAs colunas equivalem aos números de 1 a 3."+
         "\nExemplo:")

    print('a1|a2|a3'+
         '\nb1|b2|b3'+
         '\nc1|c2|c3')
    print("Que os jogos começem.")
    

def definir_marcador():
    global marcador_jog, marcador_pc
    marcador_pc = ""
    marcador_jog = input("Quer jogar com o 'X' ou 'O'?")
    marcador_jog = marcador_jog.upper()
    
    if marcador_jog != 'X' and marcador_jog != 'O':
        print("Escolha apenas 'X' ou 'O'")
        definir_marcador()
    
    if marcador_jog.upper() == 'X':
        marcador_pc = 'O'
    elif marcador_jog.upper() == 'O':
        marcador_pc = 'X'

def joga_o(pos):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, posi
    if pos == 'a1':
        if a1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            a1 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'a2':
        if a2 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            a2 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'a3':
        if a3 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            a3 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b1':
        if b1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            b1 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b2':
        if b2 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            b2 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b3':
        if b3 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            b3 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c1':
        if c1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_o(tent_2)
        else:
            c1 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c2':
        if c2 != ' ':
           tent_2 = input('Posição já escolhida. Escolha outra:')
           joga_o(tent_2)
        else:
            c2 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c3':
        if c3 != ' ':
           tent_2 = input('Posição já escolhida. Escolha outra:')
           joga_o(tent_2)
        else:
            c3 = 'O'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    else:
        tent_2 = input('Posição inválida! Escolha outra:')
        joga_o(tent_2)
        posi = tent_2



def joga_x(pos):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, posi
    if pos == 'a1':
        if a1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            a1 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'a2':
        if a2 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            a2 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'a3':
        if a3 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            a3 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b1':
        if b1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            b1 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b2':
        if b2 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            b2 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'b3':
        if b3 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            b3 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c1':
        if c1 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            c1 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c2':
        if c2 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            c2 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    elif pos == 'c3':
        if c3 != ' ':
            tent_2 = input('Posição já escolhida. Escolha outra:')
            joga_x(tent_2)
        else:
            c3 = 'X'
            print(a1+'|'+a2+'|'+a3+
                  '\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    else:
        tent_2 = input('Posição inválida! Escolha outra:')
        joga_x(tent_2)
        posi = tent_2



def verif_ganhou():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, winner
    
    if a1 != ' ':
        if a1 == a2 == a3 or a1 == b1 == c1 or a1 == b2 == c3:
            winner = a1
            print('Acabou o jogo, o marcador %s ganhou' %a1)
            return True
        
    if b2 != ' ':
        if b1 == b2 == b3 or a2 == b2 == c2 or a3 == b2 == c1:
            winner = b2
            print('Acabou o jogo, o marcador %s ganhou' %b2)
            return True
    
    if c3 != ' ':
        if c1 == c2 == c3 or a3 == b3 == c3:
            winner = c3
            print('Acabou o jogo, o marcador %s ganhou' %c3)
            return True


def jogada_pc():
    global posis, c_rand
    from random import randint
    rand = randint(0, c_rand)
    
    posi_pc = posis[rand]
    
    tent_jog_pc(posi_pc)

def tent_jog_pc(posicao_do_pc):
    global c_rand
    global posis
    global marcador_jog
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if posicao_do_pc == 'a1':
        if a1 != ' ':
            ta_aq = posis.index('a1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            a1 = marcador_pc
            ta_aq = posis.index('a1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    
    elif posicao_do_pc == 'a2':   
        if a2 != ' ':
            ta_aq = posis.index('a2')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            a2 = marcador_pc
            ta_aq = posis.index('a2')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    
    elif posicao_do_pc == 'a3':
        if a3 != ' ':
            ta_aq = posis.index('a3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            a3 = marcador_pc
            ta_aq = posis.index('a3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    
    elif posicao_do_pc == 'b1':
        if b1 != ' ':
            ta_aq = posis.index('b1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            b1 = marcador_pc
            ta_aq = posis.index('b1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
        
    elif posicao_do_pc == 'b2':
        if b2 != ' ':
            ta_aq = posis.index('b2')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            b2 = marcador_pc
            ta_aq = posis.index('b2')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
     
    elif posicao_do_pc == 'b3':   
        if b3 != ' ':
            ta_aq = posis.index('b3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            b3 = marcador_pc
            ta_aq = posis.index('b3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
            
    elif posicao_do_pc == 'c1':
        if c1 != ' ':
            ta_aq = posis.index('c1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            c1 = marcador_pc
            ta_aq = posis.index('c1')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
        
    elif posicao_do_pc == 'c2':
        if c2 != ' ':
            ta_aq = posis.index('c2')   
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            c2 = marcador_pc
            ta_aq = posis.index('c2')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
     
    elif posicao_do_pc == 'c3':   
        if c3 != ' ':
            ta_aq = posis.index('c3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            from random import randint
            tent_rand = randint(0, c_rand)
            tent_jog_pc(tent_rand)

        else:
            c3 = marcador_pc
            ta_aq = posis.index('c3')
            posis.pop(ta_aq)
            c_rand = c_rand - 1
            print("Jogada do PC:")
            print(a1+'|'+a2+'|'+a3+'\n'+b1+'|'+b2+'|'+b3+'\n'+c1+'|'+c2+'|'+c3)
    else:
        print("erro")
        print(posicao_do_pc)


def tic_tac_two_players():
    comecar_jogo()
    cont = 0
    while cont != 4.5:
        
        posi = ""
        posi = input("Marcador 'O' escolha a posição: ")
        joga_o(posi)
        verif_ganhou()
        
        if verif_ganhou() == True:
            break
        
        cont += 0.5
        
        if cont == 4.5:
            print('Deu velha!')
            break
        
        posi = ""
        posi = input("Marcador 'X' escolha a posição: ")
        joga_x(posi)
        verif_ganhou()
        
        if verif_ganhou() == True:
            break
        
        cont += 0.5

def tic_tac_player_pc():
    
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    
    global marcador_jog, marcador_pc, c_rand, posi
    
    comecar_jogo_pc()
    
    definir_marcador()
    
    if marcador_jog == "O":
        cont = 0
        while cont != 4.5:
            posi = ""
            posi = input("Marcador 'O' escolha a posição: ")
            joga_o(posi)
            ta_aq = posis.index(posi)
            posis.pop(ta_aq)
            c_rand = c_rand - 1                
            verif_ganhou()
            
            if verif_ganhou() == True:
                break
                
            cont += 0.5
                
            if cont == 4.5:
                print('Deu velha!')
                break
                    
            jogada_pc()
            verif_ganhou()
            if verif_ganhou() == True:
                break
            
            cont += 0.5
            
    elif marcador_jog == "X":
        cont = 0
        while cont != 4.5:
            posi = ""
            posi = input("Marcador 'X' escolha a posição: ")
            joga_x(posi)
            ta_aq = posis.index(posi)
            posis.pop(ta_aq)
            c_rand = c_rand - 1                
            verif_ganhou()
            
            if verif_ganhou() == True:
                break
                
            cont += 0.5
                
            if cont == 4.5:
                print('Deu velha!')
                break
                    
            jogada_pc()
            verif_ganhou()
            if verif_ganhou() == True:
                break
            
            cont += 0.5
    
    
def tic_tac_fkn_toe():
    
    global a1, a2, a3, b1, b2, b3, c1, c2, c3 , posis, c_rand
    
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    c_rand = 8
    posis = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    
    resposta1 = input("Quer jogar com o PC ou com Amigo? (Responda 'PC ou Amigo, pff'):")
    
    resposta1 = resposta1.upper()
    
    if resposta1 == "AMIGO":
        
        tic_tac_two_players()
    
    elif resposta1 == "PC":
        
        tic_tac_player_pc()
    
    resposta2 = input('Quer jogar novamente?(Sim ou Não)')
    resposta2 = resposta2.upper()
    
    
    if resposta2 == 'SIM':
        tic_tac_fkn_toe()
    
    else:
        print("Foi bom enquanto durou...")

if __name__ == '__main__':
    tic_tac_fkn_toe()
