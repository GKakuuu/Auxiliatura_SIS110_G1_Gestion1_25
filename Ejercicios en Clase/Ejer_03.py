# Lexicográficamente Agradable

S = input().strip()
K = int(input())

# Construimos K grupos, cada grupo contiene los caracteres que pueden intercambiarse entre sí
groups = [[] for _ in range(K)]

for i, c in enumerate(S):
    print(f"Index: {i}, Character: {c}, Group: {i % K}")
    groups[i % K].append(c)

print(groups)

# Ordenamos cada grupo para obtener el menor orden lexiceográfico posible
for group in groups:
    group.sort()

# Reconstruimos la cadena mínima posible
result = []
indices = [0] * K

for i in range(len(S)):
    group_idx = i % K
    result.append(groups [group_idx] [indices[group_idx]])
    indices[group_idx] += 1


print(''.join(result))