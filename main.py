#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Essas duas linhas são comentários especiais usados para configurar o ambiente de execução do código.

import random
import statistics

# Essas linhas importam dois módulos Python: random e statistics.
# O módulo random é usado para gerar números aleatórios.
# O módulo statistics é usado para realizar cálculos estatísticos, como média, mediana e moda.


def valores():  # Essa função chamada valores() coleta valores numéricos do usuário.
    n = int(
        input("Informe o tamanho do conjunto númerico: ")
    )  # Ela solicita ao usuário o tamanho do conjunto numérico e, em seguida, pede que o usuário insira os números.
    i = 0
    lista = []

    for i in range(n):
        lista.append(
            float(input("Número: "))
        )  # Os números são convertidos para ponto flutuante (float) e adicionados a uma lista chamada lista.

    lista = sorted(
        lista
    )  # Após a coleta dos números, a lista é ordenada em ordem crescente usando a função sorted().
    return lista  # A função retorna a lista ordenada.


def media_aritmetrica():  # A função media_aritmetrica() calcula a média aritmética de um conjunto de números. Chama a função valores() para obter a lista de números.
    n = valores()
    x = sum(n) / len(
        n
    )  # Calcula a média somando todos os números da lista com sum(n) e dividindo pelo número de elementos na lista com len(n)
    x = round(x, 2)  # Arredonda o resultado para duas casas decimais com round(x, 2).
    print("A media aritmetrica desse cunjunto eh: ", x)  # Imprime a média na tela.


def media_ponderada():  # A função media_ponderada() calcula a média ponderada de um conjunto de números.
    n = int(
        input("Informe o tamanho do conjunto númerico: ")
    )  # Solicita ao usuário o tamanho do conjunto numérico.
    i = 0
    y = 0
    z = 0
    a = 0

    for i in range(
        n
    ):  # Em seguida, entra em um loop onde o usuário insere pares de números e pesos.
        dados = float(input("Número: "))
        pesos = float(input("Peso: "))
        a += dados  # Os valores são acumulados em a, a soma dos produtos dos números e pesos é acumulada em y, e os pesos são acumulados em z.
        y += dados * pesos
        z += pesos
        i += 1

    try:
        x = float(
            y / z
        )  # Tenta calcular a média ponderada como y / z, arredondando para duas casas decimais.
        x = round(x, 2)
        print("A media ponderada desse conjunto eh: ", x)
    except ZeroDivisionError:
        x = (
            a / n
        )  # Se houver uma divisão por zero (caso em que a soma dos pesos é zero), calcula a média simples (não ponderada) como a / n.
        print("A media desse conjunto eh: ", x)


def moda():  # A função moda() calcula a moda de um conjunto de números.
    n = valores()

    try:
        x = statistics.mode(n)
        print("A moda desse conjunto eh: ", x)
    except (
        statistics.StatisticsError
    ):  # Se a lista for amodal (sem moda), uma exceção StatisticsError é capturada e uma mensagem de erro é impressa na tela.
        print("\n <|||> ERRO: conjunto Amodal (sem moda) <|||> ")


def mediana():  # A função mediana() calcula a mediana de um conjunto de números.
    n = valores()
    x = statistics.median(n)
    print("A mediana desse conjunto eh: ", x)


def main():  # A função main() é a função principal que organiza a execução do programa.
    i = True

    print(
        """
		=======================================================
		||           <<<===>>> Medidas <<<===>>>             ||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||            <<<===>>> de <<<===>>>                 ||
		||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||
		||      <<<===>>> Tendencia Central <<<===>>>        ||
		=======================================================
        """
    )

    while i == True:
        print("\n	Informe o número correspondente para a opção desejada: ")
        print("	(1) Calcular media aritmetrica;")
        print("	(2) Calcular media ponderada;")
        print("	(3) Calcular moda;")
        print("	(4) Calcular mediana;")
        print("	(0) Para Encerrar;")
        op = int(input(">>> "))

        if (op < 0) or (op > 5):  # Caso a opção informada seja invalida
            print(
                "\n <|||> ERRO: opção invalida... <|||> \n  **Por favor, reinicie o programa e imforme uma opção valida..."
            )
            exit()

        elif op == 1:
            media_aritmetrica()

        elif op == 2:
            media_ponderada()

        elif op == 3:
            moda()

        elif op == 4:
            mediana()

        elif (op == 0) or (i == False):  # Encerra o programa
            print("	Obg por usar nossa Calculadora! ")
            print("				< by Alunos do 3º'I' 2019 > ")
            break


main()
