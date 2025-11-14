listaNotas = []
def calcular_media(listaNotas):
    quantidadeNotas = int(input("Quantas notas você quer calcular a média?: "))
    for i in listaNotas:
        nota = float(input(f"Digite sua nota {i + 1}: "))
        media = sum(listaNotas) / len(quantidadeNotas)

def  verificar_situacao(media):
    if media >= 7:
        return "Parabéns! Você está aprovado. "
    elif media > 5 <= 6.9:
        return "Você está de recuperação. "
    elif media < 5:
        return "Você está reprovado. "