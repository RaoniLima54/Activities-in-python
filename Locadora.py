def main():
    clientes = []
    total_km = 0
    contador_clientes = 0

    while True:
        
        nome_cliente = input('Digite o nome do cliente (ou "SAIR" para encerrar):')

        if nome_cliente.upper() =='SAIR':
            print('volte sempre!')
            break

        sexo_cliente = input('Digite o sexo do cliente (M - masculino   / F - Feminino) :')
        placa_carro = input('Digite a placa do carro:')
        km_contratado = float(input('Digite a quantidade de quilometros contratados:'))
        dias_contratados = int(input('Digite a quantidade de dias contratados:'))

        valor_total = (dias_contratados * 70) + (km_contratado * 0.10)

        clientes.append({
             'nome': nome_cliente,
             'sexo': sexo_cliente,
             'placa': placa_carro,
             'km':km_contratado,
             'dias':dias_contratados,
             'valor':valor_total,
        })

        total_km += km_contratado
        contador_clientes += 1

        print(f'Placa do carro: {placa_carro}')
        print(f'Valor total a pagar: R$ {valor_total:.2f} \n')

        if contador_clientes > 0:
            media_km = total_km / contador_clientes
            print(f'Média de quilometros contratados : {media_km:.2f} km')
        
        print('\n Clientes do sexo feminino que alugaram por mais de 7 dias:')
        for cliente in clientes :
            if cliente['sexo']== 'F' and cliente['dias'] > 7:
                print(cliente['nome'])
if __name__ == '__main__':
    main()



