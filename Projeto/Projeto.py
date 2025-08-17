import psycopg2
import os
import time
import datetime
import calendar
import getpass



import Cliente


#--------------------------------------------------------------minha parte -----------------------------------------------------------------------------------

def escreve_administrador():
    print("╔═════════════════════╗")
    print("║        Menu         ║")
    print("╠═════════════════════╣")
    print("║ 1. Login            ║")
    print("║ 2. Exit             ║")
    print("╚═════════════════════╝")
    a = int(input("\n"))
    os.system('cls')

    if a == 1:
        verdade = False
        while verdade == False:
            os.system('cls')
            print("╔══════════════════════════════════════════╗")
            print("║                  Login                   ║")
            print("╚══════════════════════════════════════════╝")
            print("\nCaso queira regressar, digite somente 's' em qualquer um dos campos\n")

            while True:
                email = input("email: ")
                if email == '':
                    os.system('cls')
                    continue
                elif email == 's':
                    return
                else:
                    break


            while True:
                password = getpass.getpass("password: ")
                if password == '':
                    os.system('cls')
                    continue
                elif password == 's':
                    return
                else:
                    break

            verdade = verificar_login_administrador(email, str(password))  #verificar se ja existe e se bate certo
            #se bater certo ele sai do while (fica valor 1) - dar return 1 na funçao

            os.system('cls')

            if verdade == False:
                print("O email ou password estão incorretos")
                time.sleep(2)
                os.system('cls')
            

        
        #menu do administrador
        if verdade == True:
            print("A carregar...")
            time.sleep(3)
            os.system('cls')
            
            menu_administrador()
    

    
    elif a == 2:
        breakpoint


def verificar_login_administrador(email, password):
    cursor.execute("SELECT * FROM administrador WHERE email=%s AND password=%s", (email, password))

    # obtém o resultado da consulta    
    resultado = cursor.fetchone()


    #se o resultado for igual ao introduzido pelo utilizador return True
    if resultado is not None:
        global id_administrador_login
        id_administrador_login = resultado[0]
        return True

    else:
        return False


def menu_administrador():
    while True:
        os.system('cls')
        print("╔════════════════════════════════════════════╗")
        print("║                   Menu                     ║")
        print("╠════════════════════════════════════════════╣")
        print("║ 1. Adicionar nova viagem ou Autocarro      ║")
        print("║ 2. Estatuto Gold dos clientes              ║")
        print("║ 3. Visualizar/Alterar todas as viagens     ║")
        print("║ 4. Alteração de Preços                     ║")
        print("║ 5. Remover Viagens                         ║")
        print("║ 6. Enviar mensagem                         ║")
        print("║ 7. Ver estatisticas                        ║")
        print("║ 8. Logout/Exit                             ║") 
        print("╚════════════════════════════════════════════╝")

        opcao = input("\n")
        opcao = int(opcao) if opcao.isdigit() else 0 #converte a string num número inteiro
                                                     #Se 'opcao' não for composto por numeros, a expressão retorna 0
        if opcao < 1 or opcao > 8:
            continue
        else:
            break

    if opcao == 1:
        adicionar()
    
    elif opcao == 2:
        selecionar_cliente()
        #estatuto_gold(id_cliente)

    elif opcao == 3:
        menu_viagens()

    elif opcao == 4:
        alterar_preco()

    elif opcao == 5:
        remover_viagem()

    elif opcao == 6:
        enviar_mensagem()

    elif opcao == 7:
        estatisticas()


def adicionar (): #adicionar nova viagem ou autocarro
    os.system('cls')
    print("╔════════════════════════════════════╗")
    print("║             Adicionar              ║")
    print("╚════════════════════════════════════╝")
    print("1. Um novo autocarro")
    print("2. Uma nova viagem")
    print("3. Voltar atras")

    opcao = 0

    while opcao != 1 and opcao != 2 and opcao != 3:
        opcao = int(input("\n"))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("Digite uma opção válida")
            os.system('cls')
        if opcao == 1:
            os.system('cls')
            adicionar_autocarro()
            menu_administrador()


        elif opcao == 2:
            os.system('cls')
            id_viagem = nova_viagem()
            #print (id_viagem)

            preco = int(input("Preço: "))

            meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            while True:
                ano_partida = int(input("Ano da viagem: "))
                if ano_partida < 2023 or ano_partida > 2025:
                    print("Ainda so é possivel criar viagens entre 2023 e 2025")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break
            
            while True:
                mes_partida = int(input("Mês da viagem: "))
                if mes_partida < 1 or mes_partida > 12:
                    print("Selecione um mês entre 1 e 12")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break
                    
            if (ano_partida % 4 == 0 and ano_partida % 100 != 0) or ano_partida % 400 == 0:
                meses[2] = 29  # ano bissexto
            else:
                meses[2] = 28  # ano não bissexto

            while True:
                dia_partida = int(input("Dia da viagem: "))
                if dia_partida < 1 or dia_partida > meses[mes_partida]:
                    print("Selecione um dia válido para o mês selecionado")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break

            while True:      
                horas_partida = int(input("Horas da viagem: "))
                if horas_partida < 0 or horas_partida > 23:
                    print("O horario escolhido tem de ser entre as 00 horas e as 23 horas")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break
            while True:
                minutos_partida =int(input("Minutos da viagem: "))
                if minutos_partida < 0 or minutos_partida > 59:
                    print("O horario escolhido tem de ser entre as 00 minutos e os 59 minutos")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break

            data_partida = datetime.datetime(ano_partida, mes_partida, dia_partida, horas_partida, minutos_partida)

            print(data_partida)
            time.sleep(3)

            autocarros_id_autocarro, lotacao_autocarros = escolher_autocarro(ano_partida, mes_partida, dia_partida, horas_partida, minutos_partida)

            cursor.execute("INSERT INTO viagem (tipo_viagem_id_tipo, preco, data_partida, lotacao, autocarros_id_autocarro) VALUES (%s, %s, %s, %s, %s)", (id_viagem, preco, data_partida, lotacao_autocarros, autocarros_id_autocarro))

            conn.commit()
            menu_administrador()

        elif opcao == 3:
            os.system('cls')
            menu_administrador()


def adicionar_autocarro():
    print("╔════════════════════════════════════╗")
    print("║           Novo Autocarro           ║")
    print("╚════════════════════════════════════╝")
    marca = input("Marca do autocarro: ")
    lugares = int(input("Lugares: "))

    while True:
        matricula = input("Matricula: ")

        #Ve todas as matriculas presentes na base de dados
        cursor.execute("SELECT COUNT(*) FROM autocarros WHERE matricula = %s", (matricula,))
        result = cursor.fetchone()

        #verifica se existe alguma matricula igual 
        if result[0] > 0:
            print("Matricula ja existente na base de dados. Insira uma nova matricula.\n")
        else:
            cursor.execute("INSERT INTO autocarros (marca, matricula, lugares) VALUES (%s, %s, %s)", (marca, matricula, lugares))
            break

    conn.commit()

    os.system('cls')
    print("Adicionado com sucesso!")
    time.sleep(2)

    os.system('cls')
    

def nova_viagem():
    #aqui optou se pelo administrador poder escolher uma partida e origem ja predefinidas ou entao criar uma nova viagem
    #print("1. Quero criar uma nova viagem")
    #print("2. Quero selecionar uma viagem ja existente na base de dados") #ou seja, escolhendo o id da viagem (vai visualizar a tabela completa)
    #opcao = int(input("\n"))

    #if opcao == 1:
        os.system('cls')
        print("╔════════════════════════════════════╗")
        print("║             Nova Viagem            ║")
        print("╚════════════════════════════════════╝")

        partida = ''
        destino = ''
        while partida != 'Coimbra' and destino != 'Coimbra' and partida != 'coimbra' and destino != 'coimbra':
            partida = input("Origem: ")
            destino = input("Destino: ")
            if partida != 'Coimbra' and destino != 'Coimbra' and partida != 'coimbra' and destino != 'coimbra':
                print("Partida ou Destino tem de incluir Coimbra")
                time.sleep(2)

        distancia = str(input("Distancia(em km): "))
        duracao_minutos = int(input("Duracao(em minutos): "))

        horas, minutos = divmod(duracao_minutos, 60)
        
        duracao= f"{horas:02d}.{minutos:02d}"

        
        #print("Insira agora a duração: ")

        #horas = int(input("Horas:"))
        #minutos= int(input("Minutos:"))
        #segundos = 0

        #duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)

        os.system('cls')

        cursor.execute("INSERT INTO tipo_viagem (distancia, partida, destino, duracao) VALUES (%s, %s, %s, %s) RETURNING id_tipo", (distancia, partida, destino, duracao))
        cursor.connection.commit()

        id_viagem = cursor.fetchone()[0]
        
        return id_viagem


def escolher_autocarro(ano_partida, mes_partida, dia_partida, horas_partida, minutos_partida):
    os.system('cls')

    data_selecionada = datetime.datetime(ano_partida, mes_partida, dia_partida, horas_partida, minutos_partida)

    cursor.execute("SELECT * FROM autocarros WHERE id_autocarro NOT IN (SELECT autocarros_id_autocarro FROM viagem WHERE data_partida = %s)", (data_selecionada,))
    result = cursor.fetchall()
    id_selecionado = [resultado[0] for resultado in result] #cria uma lista que contém todos os IDs presentes na tabela selecionada

    print("╔════════════════════════════════════╗")
    print("║       Autocarros disponíveis       ║")
    print("╚════════════════════════════════════╝")


    #visualizar a tabela completa
    while True:
        os.system('cls')
        for row in result:
            print(f"{row[0]}. Matricula: {row[1]:<10} Marca: {row[2]:<10} Numero de lugares: {row[3]:<10}")
        selecao = int(input("\nEscolha um dos ids: "))
        if selecao in id_selecionado: #se a seleçao for igual a um dos numeros de linhas existentes
            break


    
    cursor.execute("SELECT * FROM autocarros WHERE id_autocarro = %s", (id_selecionado[selecao-1],))
    resultado = cursor.fetchone()
    id_viagem = resultado[0]

        
    cursor.execute("SELECT lugares FROM autocarros WHERE id_autocarro = %d" % id_viagem)
    lugares = cursor.fetchone()[0]


    lotacao_autocarros = lugares


    os.system('cls')
    return id_viagem, lotacao_autocarros  


def selecionar_cliente():
    while True:
        os.system('cls')

        cursor.execute("SELECT * FROM cliente ORDER BY id_cliente") #ordenar por ordem do id
        result = cursor.fetchall()
        id_selecionado = [resultado[0] for resultado in result] #cria uma lista que contém todos os IDs presentes na tabela selecionada

        print("╔════════════════════════════════════╗")
        print("║              Clientes              ║")
        print("╚════════════════════════════════════╝")


        #visualizar a tabela completa
    
        while True:
            for row in result:
                print("{:<3} Nome: {:<20} NIF: {:<13} Telefone: {:<10} Email: {:<20} Password: {:<10} Estatuto Gold: {:<7} Numero de viagens: {:<3}".format(row[0], row[1], row[2], row[3], row[4], row[5], "True" if row[6] else "False", row[7]))
            selecao = int(input("\nSelecione o id do cliente que deseja mudar o estatuto gold: "))
            if selecao in id_selecionado: #se a seleçao for igual a um dos numeros de linhas existentes
                break

        os.system('cls')
        
        cursor.execute("SELECT gold FROM cliente WHERE id_cliente = %s", (id_selecionado[selecao-1],))
        resultado = cursor.fetchone()
        gold_atual = resultado[0]


        opcao = ''
        while opcao != 's' and opcao != 'n':
            os.system('cls')
            for row in result:
                if row[0] == id_selecionado[selecao-1]:
                    print("{:<3} Nome: {:<20} NIF: {:<13} Telefone: {:<10} Email: {:<20} Password: {:<10} Estatuto Gold: {:<7} Numero de viagens: {:<3}".format(row[0], row[1], row[2], row[3], row[4], row[5], "True" if row[6] else "False", row[7]))
            opcao = input("\nDeseja mudar o estatuto deste cliente? (s/n)\n")
            


        # atualizar o campo "gold" do cliente selecionado
        if opcao == 's':
            if gold_atual:
                os.system('cls')
                cursor.execute("UPDATE cliente SET gold = FALSE WHERE id_cliente = %s", (id_selecionado[selecao-1],))
                print("Estatuto atualizado com sucesso!")
                time.sleep(2)
                conn.commit()  # Adiciona a linha que confirma as mudanças no banco de dados
                os.system('cls')
                sair = input("Deseja voltar ao menu? (s/n)\n") 
                if sair == 's':
                    conn.close()
                    break
                elif sair == 'n':
                    os.system('cls')
                    continue
            else:
                os.system('cls')
                cursor.execute("UPDATE cliente SET gold = TRUE WHERE id_cliente = %s", (id_selecionado[selecao-1],))
                print("Estatuto atualizado com sucesso!")
                time.sleep(2)
                conn.commit()  # Adiciona a linha que confirma as mudanças no banco de dados
                os.system('cls')
                sair = input("Deseja voltar ao menu? (s/n)\n") 
                if sair == 's':
                    conn.close()
                    break
                elif sair == 'n':
                    os.system('cls')
                    continue

        elif opcao == 'n':
            sair = 0
            while sair != 's' and sair != 'n':
                os.system('cls')
                sair = input("Deseja voltar ao menu? (s/n)\n") 
                if sair == 's':
                    conn.close()
                    menu_administrador()
                elif sair == 'n':
                    os.system('cls')
                    continue
                

    menu_administrador()


def menu_viagens():
    os.system('cls')
    selecao = 0
    while selecao != 1 and selecao != 2:
        print("╔════════════════════════════════════╗")
        print("║               Viagens              ║")
        print("╚════════════════════════════════════╝")
        print("1. Visualizar/Alterar viagens")
        print("2. Voltar atras")
        selecao = int(input("\n"))
        os.system('cls')

    if selecao == 1:
        os.system('cls')

        cursor.execute("""
        SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, a.matricula, tv.partida, tv.destino, tv.distancia, tv.duracao
        FROM viagem v
        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
        ORDER BY v.id_viagem;
    """)
        
        result = cursor.fetchall()
        


        for row in result:
            # Formata a data no formato "DD/MM/AAAA"
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))

        while True:
            sair = input("\nDeseja alterar alguma viagem? (s/n)\n")
            if sair == 'n':
                menu_administrador()
            if sair == 's':
                os.system('cls')
                break



            #cursor.execute("SELECT gold FROM viagem WHERE id_viagem = %s", (id_selecionado[selecao-1],))
            #resultado = cursor.fetchone()
            #viagem_atual = resultado[0]

    
        while True:
            os.system('cls')
            for row in result:
                data = row[2].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))

            f = False

            while f == False:
                id_viagem = int(input("Selecione a viagem que deseja alterar: "))
                os.system('cls')

                for row in result:
                    id_viagem_1 = row[0]
                    if id_viagem_1 == id_viagem:
                        f = True
                if f == False:
                    print("Viagem não encontrada!")
                    time.sleep(2)
                    os.system('cls')
                    for row in result:
                        data = row[2].strftime('%d/%m/%Y %H:%M')
                        print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))



            cursor.execute("""
            SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, a.matricula, tv.partida, tv.destino, tv.distancia, tv.duracao
            FROM viagem v
            JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
            JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
            WHERE V.ID_VIAGEM = %s
            ORDER BY v.id_viagem;
        """ % id_viagem)
            
            viagem = cursor.fetchone()
            
            tipo_viagem_id = viagem[4]
            #print(tipo_viagem_id)
            #time.sleep(5)


            os.system('cls')

            if viagem is not None:
                row = viagem
                data = row[2].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))
                print("\nO que deseja mudar?")
                print("1. Data da Viagem (Partida)")
                print("2. Autocarro")
                print("3. Partida/Destino e Duração")   
                print("4. Regressar ao menu")
                print("\n")
                opcao = int(input(""))

            else:
                os.system('cls')
                print("Viagem nao encontrada.")
                time.sleep(2)
                opcao = 0


            if opcao == 1:
                meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                os.system('cls')

                while True:
                    ano_partida = int(input("Ano da viagem: "))
                    if ano_partida < 2023 or ano_partida > 2025:
                        print("Ainda so é possivel criar viagens entre 2023 e 2025")
                        time.sleep(2)
                        os.system('cls')
                    else:
                        break
                        
                while True:
                    mes_partida = int(input("Mês da viagem: "))
                    if mes_partida < 1 or mes_partida > 12:
                        print("Selecione um mês entre 1 e 12")
                        time.sleep(2)
                        os.system('cls')
                    else:
                        break
                                
                if (ano_partida % 4 == 0 and ano_partida % 100 != 0) or ano_partida % 400 == 0:
                    meses[2] = 29  # ano bissexto
                else:
                    meses[2] = 28  # ano não bissexto

                while True:
                    dia_partida = int(input("Dia da viagem: "))
                    if dia_partida < 1 or dia_partida > meses[mes_partida]:
                        print("Selecione um dia válido para o mês selecionado")
                        time.sleep(2)
                        os.system('cls')
                    else:
                        break

                while True:      
                    horas_partida = int(input("Horas da viagem: "))
                    if horas_partida < 0 or horas_partida > 23:
                        print("O horario escolhido tem de ser entre as 00 horas e as 23 horas")
                        time.sleep(2)
                        os.system('cls')
                    else:
                        break
                while True:
                    minutos_partida =int(input("Minutos da viagem: "))
                    if minutos_partida < 0 or minutos_partida > 59:
                        print("O horario escolhido tem de ser entre as 00 minutos e os 59 minutos")
                        time.sleep(2)
                        os.system('cls')
                    else:
                        break

                data_partida = datetime.datetime(ano_partida, mes_partida, dia_partida, horas_partida, minutos_partida)

                cursor.execute("UPDATE viagem SET data_partida = %s WHERE id_viagem = %s", (data_partida, id_viagem))
                conn.commit()

                os.system('cls')
                print("Data atualizada com sucesso!")
                time.sleep(2)

                break

            if opcao == 2:
                novo_id_autocarro = atualizar_autocarro()
                cursor.execute("UPDATE viagem SET autocarros_id_autocarro = %s WHERE id_viagem = %s", (novo_id_autocarro, id_viagem))
                conn.commit()

                os.system('cls')
                print("Autocarro atualiazado com sucesso!")
                time.sleep(2)

                break

            if opcao == 3:
                os.system('cls')
                cursor.execute("SELECT id_viagem FROM viagem WHERE tipo_viagem_id_tipo = %s"  % tipo_viagem_id)

                data = row[2].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))


                #opcao = ''
                #while opcao != 1 and opcao != 2:
                    #print("O que quer alterar?")
                    #print("1. Partida")
                    #print("2. Destino")
                    #opcao = int(input("\n"))
                
                #if opcao == 1:

                partida = ''
                destino = ''
                while partida != 'Coimbra' and destino != 'Coimbra' and partida != 'coimbra' and destino != 'coimbra':
                    partida = input("Novo local de partida: ")
                    destino = input("Novo local de destino: ")
                    distancia = int(input("Nova distancia(em km): "))
                    duracao_minutos = int(input("Duracao(em minutos): "))

                    horas, minutos = divmod(duracao_minutos, 60)
        
                    duracao= f"{horas:02d}.{minutos:02d}"

                    #duracao_horas = int(duracao_minutos) // 60
                    #duracao_minutos = int(duracao_minutos) % 60

                    #duracao = "{:02d}:{:02d}".format(duracao_horas, duracao_minutos)


                    if partida != 'Coimbra' and destino != 'Coimbra' and partida != 'coimbra' and destino != 'coimbra':
                        print("Partida ou Destino tem de incluir Coimbra")
                        time.sleep(2)
                        os.system('cls')
                        data = row[2].strftime('%d/%m/%Y %H:%M')
                        print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))
                    

                cursor.execute("UPDATE tipo_viagem SET partida = %s, destino = %s, distancia = %s, duracao = %s WHERE id_tipo = %s", (partida, destino, distancia, duracao, tipo_viagem_id))
                conn.commit()

                break

            if opcao == 4:
                menu_administrador()



                #distancia = str(input("Distancia(em km): "))
                #partida = input("Origem: ")
                #destino = input("Destino: ")

    
    
    
    elif selecao == 2:
        menu_administrador()
    
    menu_administrador()
        

def atualizar_autocarro():
    os.system('cls')

    cursor.execute("SELECT * FROM autocarros")
    result = cursor.fetchall()
    id_selecionado = [resultado[0] for resultado in result] #cria uma lista que contém todos os IDs presentes na tabela selecionada

    print("╔════════════════════════════════════╗")
    print("║       Autocarros Dísponiveis       ║")
    print("╚════════════════════════════════════╝")


    #visualizar a tabela completa
    while True:
        for row in result:
            print(f"{row[0]}. Matricula: {row[1]:<10} Marca: {row[2]:<10} Numero de lugares: {row[3]:<10}")
        
        selecao = int(input("\nSelecione o novo autocarro que deseja atribuir à viagem: \n"))

    
        cursor.execute("SELECT * FROM autocarros WHERE id_autocarro = %s", (id_selecionado[selecao-1],))
        id_autocarro = selecao

        os.system('cls')
        return id_autocarro


def alterar_preco():
    os.system('cls')
    while True:
        print("╔════════════════════════════════════╗")
        print("║        Alteração de Preços         ║")
        print("╚════════════════════════════════════╝")

        cursor.execute("""
            SELECT v.id_viagem, v.preco, v.data_partida, tv.partida, tv.destino
            FROM viagem v
            JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
            ORDER BY v.id_viagem;
        """)
        result = cursor.fetchall()

        f = False

        print("1. Ver o Histórico de preços de todas as viagens")
        print("2. Alterar o preço")
        print("3. Regressar ao menu")
        opcao1 = int(input())

        if opcao1 == 3:
            menu_administrador()

        if opcao1 == 2:
            while f == False:
                for row in result:
                    # Formata a data no formato "DD/MM/AAAA"
                    data = row[2].strftime('%d/%m/%Y %H:%M')
                    print("{0}. Data: {1:<20} Preço: {2:.2f}€    Partida: {3:<10} Destino: {4:<10}".format(row[0], data, row[1], row[3], row[4]))
                
                id_viagem = int(input("Selecione a viagem que deseja alterar: "))
                os.system('cls')

                for row in result:
                    id_viagem_1 = row[0]
                    if id_viagem_1 == id_viagem:
                        f = True
                if f == False:
                    print("Viagem não encontrada!")
                    time.sleep(2)
                    os.system('cls')        




            cursor.execute("SELECT * FROM viagem WHERE id_viagem = %s" % id_viagem)
            viagem = cursor.fetchone()


            viagem_id_viagem = viagem[4]

            os.system('cls')
            cursor.execute("SELECT * FROM viagem WHERE id_viagem = %s" % id_viagem)
            result = cursor.fetchall()
            

            for row in result:
                preco = row[1]
            
            data_atualizacao = datetime.date.today()

            preco_antigo = preco


            cursor.execute("INSERT INTO historico (data_atualizacao, preco_antigo, viagem_id_viagem) VALUES (%s, %s, %s)", (data_atualizacao, preco_antigo, viagem_id_viagem))
            conn.commit()
            #cursor.execute("SELECT * FROM historico WHERE id_viagem = %s" % id_viagem)

            preco_atualizado = float(input("Digite o novo valor para o preço: "))

            
            cursor.execute("UPDATE viagem SET preco = %s WHERE id_viagem = %s", (preco_atualizado, id_viagem))
            conn.commit()

            cursor.execute("""
                SELECT v.id_viagem, v.preco, v.data_partida, tv.partida, tv.destino
                FROM viagem v
                JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                ORDER BY v.id_viagem;
            """)

            result = cursor.fetchall()
            os.system('cls')

            for row in result:
                # Formata a data no formato "DD/MM/AAAA"
                data = row[2].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<20} Preço: {2:.2f}€   Partida: {3:<10} Destino: {4:<10}".format(row[0], data, row[1], row[3], row[4]))

            while True:
                sair = input("Digite 's' para sair: ")
                if sair == 's':
                    break
            

            menu_administrador()
        
        if opcao1 == 1:
            cursor.execute("""SELECT h.data_atualizacao, h.preco_antigo, v.preco, tv.destino, tv.partida, v.id_viagem
                FROM historico h
                JOIN viagem v ON h.viagem_id_viagem = v.id_viagem
                JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                WHERE h.preco_antigo != v.preco""")
            result = cursor.fetchall()
            os.system('cls')
            print("Tabela Histórico de Preços:")
            for row in result:
                data = row[0].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<20} Preço Antigo: {2:.2f}€    Preço Novo: {3:.2f}€   Partida: {4:<10} Destino: {5:<10}".format(row[5], data, row[1], row[2], row[4], row[3]))

            while True:
                print("\n\n")
                sair = input("\n\nPrime 's' para regressar ao menu\n\n")
                if sair == 's' or sair == 'S':
                    break
                else:
                    os.system('cls')
        
            menu_administrador()


def remover_viagem():
    os.system('cls')

    cursor.execute("""
        SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, a.matricula, tv.partida, tv.destino, tv.distancia, tv.duracao
        FROM viagem v
        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
        ORDER BY v.id_viagem;
    """)
        
    result = cursor.fetchall()

    print("╔════════════════════════════════════╗")
    print("║           Remover Viagem           ║")
    print("╚════════════════════════════════════╝")
        
    
    #while True:
    os.system('cls')
    for row in result:
        data = row[2].strftime('%d/%m/%Y %H:%M')
        print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))

    id_viagem = int(input("\nSelecione a viagem que deseja apagar: "))
    
    
    cursor.execute("SELECT viagem.lotacao, Autocarros.lugares FROM viagem JOIN Autocarros ON autocarros_id_autocarro= id_autocarro WHERE id_viagem=(%s)"% id_viagem)
    for i in cursor:
        lugares= i[0]
        lotacao=i[1]


    if lugares == lotacao:
        cursor.execute("""
                        SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, a.matricula, tv.partida, tv.destino, tv.distancia, tv.duracao, b.cancelada
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        JOIN bilhete b ON v.id_viagem = b.viagem_id_viagem
                        WHERE v.id_viagem = %s
                        ORDER BY v.id_viagem;
                        """ % id_viagem)
        
        #FEZ-SE ALTER TABLE bilhete ALTER COLUMN viagem_id_viagem DROP NOT NULL PARA O VALOR PODER SER NULO NA TABELA BILHETE
        #CASO ESTA SEJA ELIMINADA
        
        cursor.execute("UPDATE bilhete SET cancelada = TRUE WHERE viagem_id_viagem = %s" % id_viagem)
        cursor.execute("DELETE FROM bilhete WHERE viagem_id_viagem = %s" % id_viagem)
        cursor.execute("DELETE FROM historico WHERE viagem_id_viagem = %s" % id_viagem)

        cursor.execute("select tipo_viagem_id_tipo from viagem where id_viagem = %s" %id_viagem)
        id_tipo = cursor.fetchone()
        cursor.execute("DELETE FROM tipo_viagem WHERE id_tipo = %s" % id_tipo)

        cursor.execute("DELETE FROM viagem WHERE id_viagem = %s" % id_viagem)
        conn.commit()
        os.system('cls')

        cursor.execute("""
            SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, a.matricula, tv.partida, tv.destino, tv.distancia, tv.duracao
            FROM viagem v
            JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
            JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
            ORDER BY v.id_viagem;
        """)
            
        result = cursor.fetchall()
            


        for row in result:
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<20} Autocarro (Matricula): {2:<10} Partida: {3:<10} Destino: {4:<10} Duração: {5:<10} Distância: {6:<10}".format(row[0], data, row[4], row[6], row[5], row[8], row[7]))


        while True:
            sair = input("Prime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')


    else:
        while True:
            print("Impossivel apagar viagens ja com reservas")
            time.sleep(2)
            os.system('cls')
            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')
        
    menu_administrador()


def enviar_mensagem():
    os.system('cls')

    cursor.execute("SELECT * FROM cliente ORDER BY id_cliente")
    result = cursor.fetchall()


    print("╔════════════════════════════════════╗")
    print("║          Enviar Mensagens          ║")
    print("╚════════════════════════════════════╝")
    print("1. Apenas para um cliente")
    print("2. Para todos os clientes")
    print("3. Voltar ao menu")

    opcao = ''
    while opcao != 1 and opcao != 2 and opcao != 3:
        opcao = int(input("\nSelecione uma das opções: "))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print("Opcão inválida!")
            time.sleep(2)
            os.system('cls')
            print("╔════════════════════════════════════╗")
            print("║          Enviar Mensagens          ║")
            print("╚════════════════════════════════════╝")
            print("1. Apenas para um cliente")
            print("2. Para todos os clientes")
            print("3. Voltar ao menu")
    

    if opcao == 1:
        os.system('cls')
        for row in result:
            print("ID Cliente: {0:<5} Nome: {1:<20} NIF: {2:<13} Telefone: {3:<13} email: {4:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

        id_cliente = int(input("\nSelecione o cliente a que deseja enviar mensagem: "))

        cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s" % id_cliente)
        result = cursor.fetchall()
        os.system('cls')

        for row in result:
            print("Cliente Selecionado:")
            print("ID Cliente: {0:<5} Nome: {1:<20} NIF: {2:<13} Telefone: {3:<13} email: {4:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
        

        mensagem = str(input("Digite a mensagem que deseja enviar ao cliente: "))

        cursor.execute("INSERT INTO mensagem_cliente (texto, visualizacao, administrador_id_administrador) VALUES (%s, %s, %s)", (mensagem, False, id_administrador_login))
        conn.commit()
        cursor.execute("INSERT INTO cliente_mensagem_cliente (cliente_id_cliente, mensagem_cliente_id_mensagem) VALUES (%s, currval(pg_get_serial_sequence('mensagem_cliente', 'id_mensagem')))", (id_cliente,))
        conn.commit()
        
        menu_administrador()
    
    elif opcao == 2:

        mensagem = str(input("Digite a mensagem que deseja enviar a todos os clientes: "))

        cursor.execute("SELECT id_cliente FROM cliente")
        result = [row[0] for row in cursor.fetchall()]

        for id_cliente in result:
            cursor.execute("INSERT INTO mensagem_cliente (texto, visualizacao, administrador_id_administrador) VALUES (%s, %s, %s)", (mensagem, False, id_administrador_login))
            conn.commit()
            cursor.execute("INSERT INTO cliente_mensagem_cliente (cliente_id_cliente, mensagem_cliente_id_mensagem) VALUES (%s, currval(pg_get_serial_sequence('mensagem_cliente', 'id_mensagem')))", (id_cliente,))
            conn.commit()


        menu_administrador()

    
    elif opcao == 3:
        menu_administrador()
        

def estatisticas():
    os.system('cls')
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║                         Estatisticas                          ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║ 1. Viagem mais vendida num determinado mês                    ║")
    print("║ 2. Cliente com mais viagens compradas num determinado mês     ║")
    print("║ 3. Todas as viagens sem reservas num determinado mês          ║")
    print("║ 4. Lista de Cientes com reservas                              ║")
    print("║ 5. Lista de Cientes com reservas canceladas                   ║")
    print("║ 6. Reservas/Clientes em espera                                ║")
    print("║ 7. Percurso com mais clientes num determinado mês             ║")
    print("║ 8. Relatório de vendas (Dia/Mês)                              ║")
    print("║ 9. Regressar ao menu                                          ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    opcao = int(input())

    os.system('cls')
    
    if opcao == 9:
        menu_administrador()

    if opcao == 1:
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


        cursor.execute("""SELECT viagem.data_partida, tipo_viagem.partida, tipo_viagem.destino, viagem.lotacao, AVG(viagem.preco)
                    FROM viagem 
                    JOIN tipo_viagem ON viagem.tipo_viagem_id_tipo = tipo_viagem.id_tipo 
                    WHERE viagem.data_partida BETWEEN %s AND %s
                    GROUP BY tipo_viagem.destino, tipo_viagem.partida, viagem.lotacao, viagem.data_partida
                    order by lotacao ASC
                    LIMIT 3""", (primeiro_dia, ultimo_dia))
        
        result = cursor.fetchall()
        os.system('cls')

        while True:
            print("Viagem mais vendida de {} até {} (Top 3):\n".format(data_inicio, data_fim))
            for row in result:
                data = row[0].strftime('%d/%m/%Y %H:%M:%S')
                print("Data: {0:<27} Partida: {1:<13} Destino: {2:<13} Preço: {3:.2f}€    Lotação: {4:<5}".format(data, row[1], row[2], row[4], row[3]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')

        menu_administrador()

    elif opcao == 9:
        menu_administrador()
        
    elif opcao == 2:
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

        cursor.execute("""select cliente.id_cliente, count(distinct id_bilhete) as numero_viagens, cliente.nome, cliente.nif, cliente.telefone, cliente.email from bilhete, cliente, viagem
                        where cliente.id_cliente = bilhete.cliente_id_cliente
                        and viagem.data_partida BETWEEN %s AND %s
                        GROUP BY cliente.id_cliente
                        order by numero_viagens DESC
                        LIMIT 10
                        """, (primeiro_dia, ultimo_dia))

        
        result = cursor.fetchall()
        os.system('cls')

        
        while True:
            print("Lista de clientes com mais viagens compradas de {} até {} (Top 3):".format(data_inicio, data_fim))
            for row in result:
                print("{0}. Nome: {1:<12} NIF: {2:<11} Telefone: {3:<11} email: {4:<20} Numero de viagens compradas: {5:<3}".format(row[0], row[2], row[3], row[4],row[5], row[1]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')

        menu_administrador()
    
    elif opcao == 3:
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

        cursor.execute("""SELECT viagem.*, autocarros.lugares, tipo_viagem.partida, tipo_viagem.destino
                        FROM viagem
                        JOIN autocarros ON viagem.autocarros_id_autocarro = autocarros.id_autocarro
                        JOIN tipo_viagem ON viagem.tipo_viagem_id_tipo = tipo_viagem.id_tipo
                        WHERE viagem.lotacao = autocarros.lugares
                        AND viagem.data_partida BETWEEN %s AND %s
                        """, (primeiro_dia, ultimo_dia))

        
        result = cursor.fetchall()
        os.system('cls')

        while True:
            print("Lista de viagens sem reservas de {} até {}:\n".format(data_inicio, data_fim))
            for row in result:
                data = row[2].strftime('%d/%m/%Y %H:%M')
                print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[7], row[8],row[1], row[6]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')

        menu_administrador()

    elif opcao == 4:
        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        ORDER BY v.id_viagem;
                        """)
        
        result = cursor.fetchall()


        for row in result:
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))


        id_viagem = int(input("\nSelecione a viagem que deseja visualizar: "))
    

        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        WHERE v.id_viagem = %s
                        ORDER BY v.id_viagem;
                        """ % id_viagem)
        
        result = cursor.fetchall()
        os.system('cls')

        for row in result:
            print("Viagem Selecionada: ")
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))

        cursor.execute("""SELECT * FROM viagem AS v,tipo_viagem
                        AS tv, bilhete AS b, cliente as c 
                        WHERE b.viagem_id_viagem = v.id_viagem 
                        AND v.tipo_viagem_id_tipo = tv.id_tipo
                        and c.id_cliente = b.cliente_id_cliente
                        AND v.id_viagem = %s
                        """ % id_viagem)
        
        result = cursor.fetchall()

        while True:
            print("\nClientes: ")
            for row in result:
                print("ID Cliente: {0:<5} Nome: {1:<20} NIF: {2:<13} Telefone: {3:<13} email: {4:<20}".format(row[15], row[18], row[19], row[20], row[21]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')
        
        menu_administrador()

    elif opcao == 5:
        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        ORDER BY v.id_viagem;
                        """)
        
        result = cursor.fetchall()


        for row in result:
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))


        id_viagem = int(input("\nSelecione a viagem que deseja visualizar: "))
    

        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        WHERE v.id_viagem = %s
                        ORDER BY v.id_viagem;
                        """ % id_viagem)
        
        result = cursor.fetchall()
        os.system('cls')

        for row in result:
            print("Viagem Selecionada: ")
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))

        cursor.execute("""SELECT * FROM viagem AS v,tipo_viagem
                        AS tv, bilhete AS b, cliente as c 
                        WHERE b.viagem_id_viagem = v.id_viagem 
                        AND v.tipo_viagem_id_tipo = tv.id_tipo
                        and c.id_cliente = b.cliente_id_cliente
                        AND v.id_viagem = %s
                        AND b.cancelada = True
                        """ % id_viagem)
        
        result = cursor.fetchall()

        while True:
            print("\nClientes: ")
            for row in result:
                print("ID Cliente: {0:<5} Nome: {1:<20} NIF: {2:<13} Telefone: {3:<13} email: {4:<20}".format(row[15], row[18], row[19], row[20], row[21]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')
        
        menu_administrador()

    elif opcao == 6:
        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        ORDER BY v.id_viagem""")

        result = cursor.fetchall()


        for row in result:
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))


        id_viagem = int(input("\nSelecione a viagem que deseja visualizar: "))
    

        cursor.execute("""SELECT v.id_viagem, v.preco, v.data_partida, v.lotacao, tv.partida, tv.destino
                        FROM viagem v
                        JOIN tipo_viagem tv ON v.tipo_viagem_id_tipo = tv.id_tipo
                        JOIN autocarros a ON v.autocarros_id_autocarro = a.id_autocarro
                        WHERE v.id_viagem = %s
                        ORDER BY v.id_viagem;
                        """ % id_viagem)
        
        result = cursor.fetchall()
        os.system('cls')

        for row in result:
            print("Viagem Selecionada: ")
            data = row[2].strftime('%d/%m/%Y %H:%M')
            print("{0}. Data: {1:<25} Partida: {2:<11} Destino: {3:<11} Preço: {4:.2f}€    Lugares disponiveis: {5:<3}".format(row[0], data, row[4], row[5],row[1], row[3]))

        cursor.execute("""SELECT * FROM cliente c
                        JOIN bilhete b ON c.id_cliente = b.cliente_id_cliente
                        WHERE b.fila_espera = true AND b.viagem_id_viagem = %s""" % id_viagem)
        
        result = cursor.fetchall()

        while True:
            print("\n\nClientes em fila de espera:")
            for row in result:
                print("ID Cliente: {0:<5} Nome: {1:<20} NIF: {2:<13} Telefone: {3:<13} email: {4:<20} gold: {5:<7}".format(row[0], row[1], row[2], row[3], row[4], 'Ativo' if row[6] == 1 else 'Inativo'))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')
            
        menu_administrador()

    elif opcao == 7:
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

        cursor.execute("""SELECT tipo_viagem.partida || ' - ' || tipo_viagem.destino AS percurso, SUM(subquery.num_compras) AS total_clientes
                            FROM tipo_viagem
                            JOIN (
                            SELECT viagem.tipo_viagem_id_tipo, COUNT(*) AS num_compras
                            FROM viagem
                            JOIN bilhete ON viagem.id_viagem = bilhete.viagem_id_viagem
                            WHERE viagem.data_partida BETWEEN %s AND %s
                            GROUP BY viagem.tipo_viagem_id_tipo
                            ) subquery ON tipo_viagem.id_tipo = subquery.tipo_viagem_id_tipo
                            GROUP BY percurso
                            ORDER BY total_clientes DESC
                            LIMIT 3""", (primeiro_dia, ultimo_dia))
        
        colunas = [coluna[0] for coluna in cursor.description]
        result = cursor.fetchall()
        os.system('cls')

        while True:
            print("Percursos com mais clientes de {} até {} (Top 3):\n".format(data_inicio, data_fim))
            for row in result:
                print("Partida: {}\nDestino: {}\nNumero total de clientes: {}\n".format(row[colunas.index('percurso')].split(' - ')[0], row[colunas.index('percurso')].split(' - ')[1], row[colunas.index('total_clientes')]))

            sair = input("\n\nPrime 's' para regressar ao menu\n\n")
            if sair == 's' or sair == 'S':
                break
            else:
                os.system('cls')
        
        menu_administrador()

    elif opcao == 8:
        print("Que dados pretende ver?")    
        print("1. Dia do ano com mais vendas")
        print("2. Mês do ano com mais vendas")

        selecao = int(input("\n"))

        if selecao == 1:
            os.system('cls')
            while True: 
                ano = int(input("Ano: "))
                if ano < 2023 or ano > 2025:
                    print("So é possível visualizar viagens entre 2023 e 2025")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break

            cursor.execute("""SELECT to_char(viagem.data_partida, 'YYYY-MM-DD') AS dia, COUNT(bilhete.id_bilhete) AS total_vendas
                            FROM viagem
                            JOIN bilhete ON viagem.id_viagem = bilhete.viagem_id_viagem
                            WHERE EXTRACT(YEAR FROM viagem.data_partida) = %s
                            GROUP BY dia
                            ORDER BY total_vendas DESC
                            LIMIT 3;""" % ano)

            result = cursor.fetchall()
            os.system('cls')

            print("Dia com mais vendas no ano de {} (Top 3):\n".format(ano))

            while True:
                for row in result:
                    print("Dia: {}\nNumero de vendas: {}\n".format(row[0], row[1]))

                sair = input("\n\nPrime 's' para regressar ao menu\n\n")
                if sair == 's' or sair == 'S':
                    break
                else:
                    os.system('cls')
            
            menu_administrador()
        
        elif selecao == 2:
            meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
            os.system('cls')
            while True:
                ano = int(input("Ano: "))
                if ano < 2023 or ano > 2025:
                    print("So é possível visualizar viagens entre 2023 e 2025")
                    time.sleep(2)
                    os.system('cls')
                else:
                    break

            cursor.execute("""SELECT EXTRACT(MONTH FROM viagem.data_partida) AS mes, COUNT(bilhete.id_bilhete) AS total_vendas
                                FROM viagem
                                JOIN bilhete ON viagem.id_viagem = bilhete.viagem_id_viagem
                                WHERE EXTRACT(YEAR FROM viagem.data_partida) = %s
                                GROUP BY mes
                                ORDER BY total_vendas DESC
                                LIMIT 3;""" % ano)

            result = cursor.fetchall()
            os.system('cls')

            print("Mês com mais vendas no ano de {} (Top 3):\n".format(ano))

            while True:
                for row in result:
                    print("Mês: {}\nNumero de vendas: {}\n".format(meses[row[0]], row[1]))

                sair = input("\n\nPrime 's' para regressar ao menu\n\n")
                if sair == 's' or sair == 'S':
                    break
                else:
                    os.system('cls')
            
            menu_administrador()



#------------------------------------------------------

while True:
    os.system('cls')
    conn = psycopg2.connect(
    host="localhost",
    database="Projeto - Entrega II",
    user="postgres",
    password="postgres"
)
    cursor = conn.cursor()
    
    os.system('cls')
    print("╔══════════════════════╗")
    print("║         Menu         ║")
    print("╠══════════════════════╣")
    print("║ 1. Cliente           ║")
    print("║ 2. Administrador     ║")
    print("║ 3. Exit              ║")
    print("╚══════════════════════╝")
    a = int(input("\n"))

    if a == 1:
        os.system('cls')
        Cliente.escreve_cliente()
    
    elif a == 2:
        os.system('cls')
        escreve_administrador()

    elif a == 3:
        os.system('cls')
        break