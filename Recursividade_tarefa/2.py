def soma_lista(lista):
    if len(lista) == 1:
        soma = lista[0]
        return soma
    else:
        for i in lista:
            soma = lista[0] + soma_lista(lista[1:])
            return soma
        
lista = [1,2,3,4,5]
print(soma_lista(lista))