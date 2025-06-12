from collections import Counter

def prescricao_valida(prescricao, estoque):
    cont_prescricao = Counter(prescricao)
    cont_estoque = Counter(estoque)

    for medicamento, qtd in cont_prescricao.items():
        if cont_estoque[medicamento] < qtd:
            return False
    return True

# Exemplos:
print(prescricao_valida('a', 'b'))          # False
print(prescricao_valida('aa', 'b'))         # False
print(prescricao_valida('aa', 'aab'))       # True
print(prescricao_valida('aba', 'cbaa'))     # True
