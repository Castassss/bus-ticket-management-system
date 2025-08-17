import psycopg2
import os
import datetime
import calendar 
import time
import getpass

# Estabelece a conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="Projeto - Entrega II",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()
# ----------------- FUNÇÕES --------------------------
def clear():
    os.system('cls')
    
# -----------------Cliente------------
def escreve_cliente():
    print("╔════════════════════════════════════╗")
    print("║                Menu                ║")
    print("╠════════════════════════════════════╣")
    print("║           1. Resgistar             ║")
    print("║           2. Login                 ║")
    print("║           3. Exit                  ║")
    print("╚════════════════════════════════════╝")
    a = int(input("\n"))
    os.system('cls')
    
    if a == 1:
        nome_completo = input("Nome Completo: ")
        nif= input("NIF: ")
        Telefone = input("Telefone: ")
        email = input("email: ")
        password = getpass.getpass("password: ")
        #ADICIONAR UM EXIT
        registar(nome_completo, nif, Telefone, email, password) #guardar na tabela

    elif a == 2:
        verdade = 0
        while verdade == 0:
            print("╔════════════════════════════════════╗")
            print("║               Login                ║")
            print("╚════════════════════════════════════╝")
            print("Se quiser regressar, digite 0")
            email = input("email: ")
            if email == "0":
                break
            password = getpass.getpass("password: ")
            #ADICIONAR UM EXIT

            verdade = verificar_login_cliente(email, password)  #verificar se ja existe e se bate certo
            #se bater certo ele sai do while (fica valor 1)

        #menu do cliente
        if verdade != 0:
            menu_cliente(verdade)


    elif a == 3:
        breakpoint

# -----------REGISTAR-----------------
def registar(nome_completo, nif, Telefone, email, password):
    goldd = input("Pretende comprar estatuto gold?(s/n)")
    if goldd == "n":
        query = 'INSERT INTO cliente (nome, nif, telefone, email, password, gold, numero_viagens) VALUES (%s, %s,%s,%s, %s, False, 0)'
        val = (nome_completo, nif, Telefone, email, password)
        cur.execute(query,val)
        conn.commit()
    elif goldd == "s":
        query = 'INSERT INTO cliente (nome, nif, telefone, email, password, gold, numero_viagens) VALUES (%s, %s,%s,%s, %s, True, 0)'
        val = (nome_completo, nif, Telefone, email, password)
        cur.execute(query,val)
        conn.commit()
    os.system('cls')
    escreve_cliente()
    # Executa um comando SQL para selecionar dados de uma tabela
    #cur.execute("SELECT * FROM cliente")
    # Recupera os dados selecionados usando o método fetchall()
    #data = cur.fetchall()
    # Imprime os dados selecionados
    #for row in data:
    #   print(row)
    # Fecha o cursor e a conexão
    #cur.close()
    #conn.close()
# -----------FIM_REGISTAR------------

# -----------LOGIN-------------------
def verificar_login_cliente(email, password):
    # Executa um comando SQL para selecionar dados de uma tabela
    cur.execute("SELECT * FROM cliente")
    # Recupera os dados selecionados usando o método fetchall()
    data = cur.fetchall()
    # Imprime os dados selecionados
    for row in data:
       id, nome, nif, num, email2, pas, gold, num_via = row
       if email == email2 and password == pas:
            return id
    
    os.system('cls')
    print("Palavra pass ou email incorretos!")
    return 0
                
# -----------FIM_LOGIN---------------

# -----------Menu_cliente---------------
def menu_cliente(id):
    clear()
    cur.execute("SELECT * FROM cliente")
    data = cur.fetchall()
    for row in data:
       id2, nome, nif, num, email2, pas, gold, num_via = row
       if id == id2:
           global e_gold
           e_gold = gold
           break
    print("╔════════════════════════════════════╗")
    print("║               Menu                 ║ Cliente: %s" % nome)
    print("╠════════════════════════════════════╝══════════════════╗")
    print("║ 1- Viagens                                            ║")
    print("║ 2- Bilhetes                                           ║")
    print("║ 3- Cancelar bilhetes                                  ║")
    print("║ 4- Mensagens                                          ║")
    print("║ 5- Gold                                               ║")
    print("║ 6- Pesquisa livre                                     ║")
    print("║ 7- Logout                                             ║")
    print("╚═══════════════════════════════════════════════════════╝")

    print("\n")
    es = input()
    if es == "7":
        return
    elif es == "1":
        ver_destinos(nome,id2)
        menu_cliente(id)
    elif es == "5":
        comprar_gold(nome, id2)
        menu_cliente(id)
    elif es == "4":
        ver_menssagens(nome,id2)
        menu_cliente(id)
    elif es == "2":
        ver_Bilhetes(nome,id2)
        menu_cliente(id)
    elif es == "3":
        cancelar_bilhetes(nome,id2)
        menu_cliente(id)
    elif es == "6":
        pesuisa_livre(nome,id2)
        menu_cliente(id)

# -----------------Ver_Destinos------------
def ver_destinos(nome,id_c):
    clear()
    cur.execute("SELECT * FROM tipo_viagem")
    data = cur.fetchall()
    print("Destinos disponives:                                                Cliente:",nome, "\n")
    k = 0
    print("╔══════════════════════════════════════════╗")
    print("║            Escolha um destino            ║")
    print("╚══════════════════════════════════════════╝")
    for row in data:
       k = k +1
       id, distancia, destino, partida, tempoviagem = row
       print(id,"- ",partida,"->",destino)
    des = int(input("Escolha um destino: "))
    ver_viagens(nome, des,id_c)
# -----------------FIM_Ver_Destinos------------

# -----------------Ver_Viagens------------
def ver_viagens(nome, id2, id_c):
    clear()
    dt = datetime.date.today()
    cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
    data = cur.fetchall()
    t = False
    print("╔════════════════════════════════════╗")
    print("║         Viagens Disponiveis        ║ Cliente: %s" % nome)
    print("╚════════════════════════════════════╝")
    while t == False:  
     k = 0
     verificar = 0
     for row in data:
        k = k +1
        id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
        if id == id2 and dt < data_partida.date():
            verificar = verificar + 1
            print("--------------------------------------------------------------------")
            print(id_viagem,":")
            if e_gold == True:
                print("  -Preco:",float(preco)*0.9)
            else:
                print("  -Preco:",preco)
            print("  -Data partida: ",data_partida)
            print("  -Lugares disponiveis: ",lotacao)
            print("  -Autocarro: ",autocarros_id_autocarro)
            print("  -Distancia: ",distancia)
            print("  -Destino: ",destino)
            print("  -Partida: ",partida)
            print("  -Tempo deviagem: ",tempoviagem)   
     cur.close 
     if verificar == 0:
         print("\nNao ha viagens disponiveis para esse destino")
         input()
         return   
     V = int(input("\nQual viagem deseja comprar?(0 se quiser sair): "))
     if V == 0:
         return
     cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
     data = cur.fetchall()
     for row in data:
         idd = row[0]
         if idd == V:
          t = True
     comprar(nome,V,id_c)
# -----------------FIM_Ver_Viagens------------

# -----------------Comprar------------
def comprar(nome,id2,id_c):
     clear()
     print("╔════════════════════════════════════╗")
     print("║          Comprar Bilhetes          ║ Cliente: %s" % nome)
     print("╚════════════════════════════════════╝")
     cur.execute("SELECT lotacao FROM viagem WHERE id_viagem = %d" % id2)
     data = cur.fetchone()
     if int(data[0]) == 0:
         l = input("Lotacao cheia, deseja ficar em lista de espera?(s/n)")
         if l == "s":
             dt = datetime.date.today()
             query = 'INSERT INTO bilhete (hora_compra, fila_espera, cliente_id_cliente, viagem_id_viagem) VALUES (%s,True,%s, %s)'
             val = (dt,id_c,id2)
             cur.execute(query,val)
             conn.commit()
             return
         elif l == "n":
             return
     elif int(data[0]) > 0:
         dt = datetime.date.today()
         query = 'INSERT INTO bilhete (hora_compra, fila_espera, cliente_id_cliente, viagem_id_viagem) VALUES (%s,False,%s, %s)'
         val = (dt,id_c,id2)
         cur.execute(query,val)
         conn.commit()
         nova_lotacao = int(data[0]) - 1
         cur.execute("UPDATE viagem SET lotacao = lotacao-1 WHERE id_viagem = %d" % id2)
         conn.commit()
         cur.execute("UPDATE cliente SET numero_viagens = numero_viagens+1 WHERE id_cliente = %d" % id_c)
         conn.commit()
         print("Bilhete comprado com sucesso!")
         input()
# -----------------Fim_Comprar------------

# -----------------Comprar_Gold------------
def comprar_gold(nome, id2):
    clear()
    print("╔════════════════════════════════════╗")
    print("║           Estatuto Gold            ║ Cliente: %s" % nome)
    print("╚════════════════════════════════════╝")
    g = input("Deseja comprar Gold?(s/n)")    
    if g == "s":
        cur.execute("SELECT gold FROM cliente WHERE id_cliente = %d" % id2)
        data = cur.fetchone()
        if data[0] == True:
            print("Já possui estatuto gold!")
            input()
            return
        cur.execute("UPDATE cliente SET gold = True WHERE id_cliente = %d" % id2)
        conn.commit()
        print("Comprado com sucesso!")
        input()
    elif g == "n":
        return
# -----------------Fim_Comprar_Gold------------

# -----------------Ver_menssagens------------
def ver_menssagens(nome,id2):
    clear()
    print("╔════════════════════════════════════╗")
    print("║             Mensagens              ║ Cliente: %s" % nome)
    print("╚════════════════════════════════════╝")
    cur.execute("SELECT * FROM cliente_mensagem_cliente AS a, mensagem_cliente AS M WHERE a.cliente_id_cliente = %d AND a.mensagem_cliente_id_mensagem = id_mensagem" % id2)
    data = cur.fetchall()
    k = data
    vis = False
    print("Nao lidas:")
    for row in data:
       cid_c , msc_idm, id_mensagem, visualizacao, texto ,administrador_id_administrador = row
       if visualizacao == False and cid_c == id2:
           vis = True
           print("\t------------------------------------------------------")
           print("\t",id_mensagem,"-",texto)
           cur.execute("UPDATE mensagem_cliente SET visualizacao = True where id_mensagem = %d" % id_mensagem)
           conn.commit()
    print("\t------------------------------------------------------")
    
    if vis == False:
        print("\tNao tem mensagens por ler")
        print("\t------------------------------------------------------")
    print("Lidas:")
    for row1 in k:
       cid_c , msc_idm, id_mensagem, visualizacao, texto ,administrador_id_administrador = row1
       if visualizacao == True:
           print("\t------------------------------------------------------")
           print("\t",id_mensagem,"-", texto)
    print("\t------------------------------------------------------")
    input()
# -----------------Fim_Ver_menssagens------------

# -----------------Ver_Bilhetes------------
def ver_Bilhetes(nome,id2):
    clear()
    dt = datetime.date.today()
    print("╔════════════════════════════════════╗")
    print("║              Bilhetes              ║ Cliente: %s" % nome)
    print("╚════════════════════════════════════╝")
    cur.execute("SELECT b.fila_espera, b.cancelada, v.id_viagem ,v.data_partida, tv.destino, tv.partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo AND cliente_id_cliente = %d"%id2)
    data = cur.fetchall()
    h = 0
    h1 = 0
    h3 = 0
    k = data
    j = data
    print("Bilhetes validos:")
    count = 0
    for row in data:
        l_e, cancelado, id ,d_p , des, prt = row
        if d_p.date() > dt and cancelado != True and l_e != True: 
         h = h+1      
         print("\t",id,"- ",prt,"->",des," -",d_p)
    if h == 0:
        print("\tNao tem viagens por realizar")
    print("--------------------------------------------------")
    print("Em lista de espera:")
    count = 0
    cur.execute("SELECT distinct b.fila_espera, b.cancelada, v.id_viagem ,v.data_partida, tv.destino, tv.partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo AND cliente_id_cliente = %d"%id2)
    j = cur.fetchall()
    for row in j:
        l_e, cancelado, id ,d_p , des, prt = row
        if d_p.date() > dt and cancelado != True and l_e == True: 
         h3 = h3+1      
         print("\t",id,"- ",prt,"->",des," -",d_p)
    if h3 == 0:
        print("\tNao tem viagens em lista de espera")
    print("--------------------------------------------------")
    print("Bilhetes usados:")
    ultimoidviagem = -1
    h2 = 1
    for row1 in k:     
        l_e, cancelado1, id1 ,d_p1 , des1, prt1 = row1
        count = count +1
        if dt > d_p1.date() and cancelado1 != True and l_e != True:
            if ultimoidviagem != id1:
                h2 = h2 + 1  
            h1 = h1+1
            print("\t",id1,"- ",prt1,"->",des1," -",d_p1)
        ultimoidviagem = id1
    if h1 == 0:
        print("\tNao tem viagens realizadas")   
    cur.execute("SELECT numero_viagens from cliente where id_cliente = %d"%id2)
    data = cur.fetchone()
    print("\nJa comprou",data[0],"bilhetes, e realizou",h2,"viagens\t")
    if h1 == 0 and h ==0:
     input()
     return      
    p = int(input("\nQual bilhete deseja ver as informacoes?(0 para sair): "))

    if p == 0:
        clear()
        menu_cliente(id2)

    clear()
    cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
    data = cur.fetchall()
    print("Informacao viagem:                                                Cliente:",nome, "\n")
    k = 0
    for row in data:
       k = k +1
       id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
       if id_viagem == p:
         print("--------------------------------------------------------------------")
         print(id_viagem,":")
         if e_gold == True:
          print("  -Preco:",float(preco)*0.9)
         else:
          print("  -Preco:",preco)
         print("  -Data partida: ",data_partida)
         print("  -Lugares disponiveis: ",lotacao)
         print("  -Autocarro: ",autocarros_id_autocarro)
         print("  -Distancia: ",distancia)
         print("  -Destino: ",destino)
         print("  -Partida: ",partida)
         print("  -Tempo deviagem: ",tempoviagem)
         print("--------------------------------------------------------------------")   
    input()   
# -----------------Fim_Ver_Bilhetes------------

# -----------------Ver_Bilhetes------------
def cancelar_bilhetes(nome,id2):
    clear()
    dt = datetime.date.today()
    dia = dt.day
    ano = dt.year
    mes = dt.month
    id_c = id2
    print("╔════════════════════════════════════╗")
    print("║              Bilhetes              ║ Cliente: %s" % nome)
    print("╚════════════════════════════════════╝")
    cur.execute("SELECT b.fila_espera, v.lotacao, v.id_viagem, b.cancelada, b.id_bilhete ,v.data_partida, tv.destino, tv.partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo AND cliente_id_cliente = %d"%id2)
    data = cur.fetchall()
    h = 0
    k = data
    print("Bilhetes validos:")
    count = 0
    for row in data:
        f_e, lotacao ,id_viagem, b_cancelado,id ,d_p , des, prt = row
        dia1 =d_p.day
        mes1 = d_p.month
        ano1 = d_p.year
        if e_gold == True:
            if d_p.date() > dt and ano < ano1 and b_cancelado != True and f_e != True:
                h = h+1      
                count = count +1
                print("\t",count,"- ",prt,"->",des," -",d_p)
            elif d_p.date() > dt and ano == ano1 and mes < mes1 and b_cancelado != True and f_e != True: 
                h = h+1      
                count = count +1
                print("\t",count,"- ",prt,"->",des," -",d_p)
            elif d_p.date() > dt and ano == ano1 and mes == mes1 and dia <= dia1-2 and b_cancelado != True and f_e != True:
                 h = h+1      
                 count = count +1
                 print("\t",count,"- ",prt,"->",des," -",d_p)
            
        else:
            if d_p.date() > dt and ano < ano1 and b_cancelado != True and f_e != True:
                h = h+1      
                count = count +1
                print("\t",count,"- ",prt,"->",des," -",d_p)
            elif d_p.date() > dt and ano == ano1 and mes < mes1 and b_cancelado != True and f_e != True: 
                h = h+1      
                count = count +1
                print("\t",count,"- ",prt,"->",des," -",d_p)
            elif d_p.date() > dt and ano == ano1 and mes == mes1 and dia <= dia1-7 and b_cancelado != True and f_e != True:
                 h = h+1      
                 count = count +1
                 print("\t",count,"- ",prt,"->",des," -",d_p)
    if h == 0:
        print("\tNao tem viagens por realizar")
    cancelar = int(input("\nQual viagem pretende cancelar?(0 para sair): "))
    if cancelar == 0:
        return
    count = 0
    for row in k:
        f_e, lotacao, id_viagem, b_cancelado, id ,d_p , des, prt = row
        dia1 = d_p.day
        mes1 = d_p.month
        ano1 = d_p.year
        if d_p.date() > dt and ano < ano1 and b_cancelado != True and f_e != True:
            count = count +1
            if count == cancelar :
             id_2 = id_viagem
             id_cancelar = id
             print("\tViagem cancelada: ",count,"- ",prt,"->",des," -",d_p)
        elif d_p.date() > dt and ano == ano1 and mes < mes1 and b_cancelado != True and f_e != True:      
            count = count +1
            if count == cancelar :
             id_2 = id_viagem
             id_cancelar = id
             print("\tViagem cancelada: ",count,"- ",prt,"->",des," -",d_p)
        elif d_p.date() > dt and ano == ano1 and mes == mes1 and dia <= dia1-2 and b_cancelado != True and f_e != True:    
            count = count +1
            if count == cancelar :
             id_2 = id_viagem
             id_cancelar = id
             print("\tViagem cancelada: ",count,"- ",prt,"->",des," -",d_p)               
    cur.execute("UPDATE bilhete SET cancelada = True WHERE id_bilhete = %d" % id_cancelar)
    conn.commit()
    if lotacao == 0:
        cur.execute("SELECT distinct b.cliente_id_cliente FROM viagem AS v,tipo_viagem AS tv,bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo and b.viagem_id_viagem = %d and b.fila_espera = True" % id_viagem)
        data = cur.fetchall()
        #mensagem = "Ha uma nova vaga na viagem:",id_viagem,"-",prt,"->",des,"-",d_p
        mensagem = f"Há uma nova vaga na viagem {id_viagem} com origem {prt} e destino {des} no dia {d_p}"
        
        for row in data:
            cur.execute("INSERT INTO mensagem_cliente (visualizacao, texto, administrador_id_administrador) VALUES (%s, %s, %s)", (False,mensagem, 1))
            conn.commit()
            cur.execute("INSERT INTO cliente_mensagem_cliente (cliente_id_cliente, mensagem_cliente_id_mensagem) VALUES (%s, currval(pg_get_serial_sequence('mensagem_cliente', 'id_mensagem')))", (row,))
            conn.commit()
        input()

    cur.execute("UPDATE viagem SET lotacao = lotacao+1 WHERE id_viagem = %d" % id_2)
    conn.commit()
    cur.execute("UPDATE cliente SET numero_viagens = numero_viagens-1 WHERE id_cliente = %d" % id_c)
    conn.commit()
    input("\n")
# -----------------Fim_Cancelar_Bilhetes------------

# -----------------Pesuisa_livre------------
def pesuisa_livre(nome,id2):
    clear()
    print("╔════════════════════════════════════╗")
    print("║               Menu                 ║ Cliente: %s" % nome)
    print("╠════════════════════════════════════╝══════════════════╗")
    print("║   1- Distância                                        ║")
    print("║   2- Destino                                          ║")
    print("║   3- Data                                             ║")
    print("║   4- Gama de datas                                    ║")                           
    print("╚═══════════════════════════════════════════════════════╝")
    escolha = int(input("\nEscolha uma opcao ou 0 para sair: "))
    if escolha == 0:
        return
    if escolha == 1:
        clear()
        print("Distancias disponiveis:                                            Cliente:",nome)
        cur.execute("SELECT DISTINCT tv.distancia FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        count = 0
        while data != None:
            for row in data:
                dist = row
            count = count +1
            print(count,"-",dist)
            data = cur.fetchone()
        escolha = int(input("\nEscolha uma opcao ou 0 para sair: "))
        if escolha == 0:
            return
        count = 0
        cur.execute("SELECT DISTINCT tv.distancia FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        while data != None:
            for row in data:
                dist = row
            count = count +1
            if escolha == count:
                real_dist = dist
            data = cur.fetchone()
        #-------------------------------------------------------------------------
        clear()
    
        cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
        data = cur.fetchall()
        t = False
        print("Viagens disponives:                                                Cliente:",nome, "\n")
        while t == False:  
         k = 0
         for row in data:
            k = k +1
            id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
            if real_dist == distancia:
                print("--------------------------------------------------------------------")
                print(id_viagem,":")
                if e_gold == True:
                    print("  -Preco:",float(preco)*0.9)
                else:
                    print("  -Preco:",preco)
                print("  -Data partida: ",data_partida)
                print("  -Lugares disponiveis: ",lotacao)
                print("  -Autocarro: ",autocarros_id_autocarro)
                print("  -Distancia: ",distancia)
                print("  -Destino: ",destino)
                print("  -Partida: ",partida)
                print("  -Tempo deviagem: ",tempoviagem)   
         cur.close    
         V = int(input("\nQual viagem deseja comprar?(0 se quiser sair): "))
         if V == 0:
             return
         cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
         data = cur.fetchall()
         for row in data:
             idd = row[0]
             if idd == V:
              t = True
         comprar(nome,V,id2)
    elif escolha == 2:
        clear()
        print("Destinos disponiveis:                                            Cliente:",nome)
        cur.execute("SELECT DISTINCT tv.destino FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        count = 0
        while data != None:
            for row in data:
                dist = row
            count = count +1
            print(count,"-",dist)
            data = cur.fetchone()
        escolha = int(input("\nEscolha uma opcao ou 0 para sair: "))
        if escolha == 0:
            return
        count = 0
        cur.execute("SELECT DISTINCT tv.destino FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        while data != None:
            for row in data:
                dist = row
            count = count +1
            if escolha == count:
                real_dist = dist
            data = cur.fetchone()
        #-------------------------------------------------------------------------
        clear()
    
        cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
        data = cur.fetchall()
        t = False
        print("Viagens disponives:                                                Cliente:",nome, "\n")
        while t == False:  
         k = 0
         for row in data:
            k = k +1
            id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
            if real_dist == destino:
                print("--------------------------------------------------------------------")
                print(id_viagem,":")
                if e_gold == True:
                    print("  -Preco:",float(preco)*0.9)
                else:
                    print("  -Preco:",preco)
                print("  -Data partida: ",data_partida)
                print("  -Lugares disponiveis: ",lotacao)
                print("  -Autocarro: ",autocarros_id_autocarro)
                print("  -Distancia: ",distancia)
                print("  -Destino: ",destino)
                print("  -Partida: ",partida)
                print("  -Tempo deviagem: ",tempoviagem)   
         cur.close    
         V = int(input("\nQual viagem deseja comprar?(0 se quiser sair): "))
         if V == 0:
             return
         cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
         data = cur.fetchall()
         for row in data:
             idd = row[0]
             if idd == V:
              t = True
         comprar(nome,V,id2)
    elif escolha == 3:
        clear()
        print("Destinos disponiveis:                                            Cliente:",nome)
        cur.execute("SELECT DISTINCT v.data_partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        count = 0
        while data != None:
            for row in data:
                dist = row
            count = count +1
            print(count,"-",dist)
            data = cur.fetchone()
        escolha = int(input("\nEscolha uma opcao ou 0 para sair: "))
        if escolha == 0:
            return
        count = 0
        cur.execute("SELECT DISTINCT v.data_partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        while data != None:
            for row in data:
                dist = row
            count = count +1
            if escolha == count:
                real_dist = dist
            data = cur.fetchone()
        #-------------------------------------------------------------------------
        clear()
    
        cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
        data = cur.fetchall()
        t = False
        print("Viagens disponives:                                                Cliente:",nome, "\n")
        while t == False:  
         k = 0
         for row in data:
            k = k +1
            id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
            if real_dist == data_partida:
                print("--------------------------------------------------------------------")
                print(id_viagem,":")
                if e_gold == True:
                    print("  -Preco:",float(preco)*0.9)
                else:
                    print("  -Preco:",preco)
                print("  -Data partida: ",data_partida)
                print("  -Lugares disponiveis: ",lotacao)
                print("  -Autocarro: ",autocarros_id_autocarro)
                print("  -Distancia: ",distancia)
                print("  -Destino: ",destino)
                print("  -Partida: ",partida)
                print("  -Tempo deviagem: ",tempoviagem)   
         cur.close    
         V = int(input("\nQual viagem deseja comprar?(0 se quiser sair): "))
         if V == 0:
             return
         cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
         data = cur.fetchall()
         for row in data:
             idd = row[0]
             if idd == V:
              t = True
         comprar(nome,V,id2)
    elif escolha == 4:
        clear()
        while True:
            ano = int(input("Ano: "))
            if ano < 2023 or ano > 2025:
                print("Ainda só é possível criar viagens entre 2023 e 2025")
                time.sleep(2)
                os.system('cls')
            else:
                break

        while True:
            mes = int(input("Mês: "))
            if mes < 1 or mes > 12:
                print("Selecione um mês entre 1 e 12")
                time.sleep(2)
                os.system('cls')
            else:
                break

        # Define o primeiro dia do mês
        primeiro_dia = datetime.date(ano, mes, 1)
        data_inicio = primeiro_dia.strftime('%Y-%m-%d')

        # Define o último dia do mês
        dias_no_mes = calendar.monthrange(ano, mes)[1]
        ultimo_dia = datetime.date(ano, mes, dias_no_mes)
        data_fim = ultimo_dia.strftime('%Y-%m-%d')

        #--------------------------------
        clear()
        print("Destinos disponiveis:                                            Cliente:",nome)
        cur.execute("SELECT DISTINCT v.data_partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo AND v.data_partida BETWEEN %s AND %s", (primeiro_dia, ultimo_dia))
        data = cur.fetchone()
        count = 0
        verificar = 0
        while data != None:
            verificar = verificar + 1
            for row in data:
                dist = row
            count = count +1
            print(count,"-",dist)
            data = cur.fetchone()
        if verificar == 0:
         print("\nNao ha viagens disponiveis para esse mes")
         input()
         return   
        escolha = int(input("\nEscolha uma opcao ou 0 para sair: "))
        if escolha == 0:
            return
        count = 0
        cur.execute("SELECT DISTINCT v.data_partida FROM viagem AS v,tipo_viagem AS tv, bilhete AS b WHERE b.viagem_id_viagem = v.id_viagem AND v.tipo_viagem_id_tipo = tv.id_tipo")
        data = cur.fetchone()
        while data != None:
            for row in data:
                dist = row
            count = count +1
            if escolha == count:
                real_dist = dist
            data = cur.fetchone()
        #-------------------------------------------------------------------------
        clear()
    
        cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
        data = cur.fetchall()
        t = False
        print("Viagens disponives:                                                Cliente:",nome, "\n")
        while t == False:  
         k = 0
         for row in data:
            k = k +1
            id_viagem, preco, data_partida, lotacao, autocarros_id_autocarro, tipo_viagem_id_tipo,id, distancia, destino, partida, tempoviagem = row
            if real_dist == data_partida:
                print("--------------------------------------------------------------------")
                print(id_viagem,":")
                if e_gold == True:
                    print("  -Preco:",float(preco)*0.9)
                else:
                    print("  -Preco:",preco)
                print("  -Data partida: ",data_partida)
                print("  -Lugares disponiveis: ",lotacao)
                print("  -Autocarro: ",autocarros_id_autocarro)
                print("  -Distancia: ",distancia)
                print("  -Destino: ",destino)
                print("  -Partida: ",partida)
                print("  -Tempo deviagem: ",tempoviagem)   
         cur.close    
         V = int(input("\nQual viagem deseja comprar?(0 se quiser sair): "))
         if V == 0:
             return
         cur.execute("SELECT * FROM viagem, tipo_viagem WHERE tipo_viagem.id_tipo = viagem.tipo_viagem_id_tipo")
         data = cur.fetchall()
         for row in data:
             idd = row[0]
             if idd == V:
              t = True
         comprar(nome,V,id2)
# -----------------Pesuisa_livre------------

# -----------------FIM_Cliente------------

# -----------------Administrador------------





# Cria um cursor para executar comandos SQL
#novo = conn.cursor()
   

# Executa um comando SQL para selecionar dados de uma tabela
#novo.execute("SELECT * FROM cliente")

# Recupera os dados selecionados usando o método fetchall()
#data = novo.fetchall()

# Imprime os dados selecionados
#for row in data:
 #   print(row)

# Fecha o cursor e a conexão
#novo.close()
#conn.close()