def HanoiTowers(n, froms=1, to=3, additional=2):
    if n == 1:
        return [(froms, to)]
    result = HanoiTowers(n - 1, froms, additional, to)
    result.append((froms, to))
    result += HanoiTowers(n - 1, additional, to, froms)
    return result

a = int(input("Введите количество колец:\n"))
b = 1

moves = HanoiTowers(a)
for move in moves:
    print(f"{b}. Переместить диск с {move[0]} на {move[1]}\n")
    b += 1
    
print(f"Эту головоломку можно решить за {b-1} ходов\n")