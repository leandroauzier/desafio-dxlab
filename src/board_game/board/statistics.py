from collections import Counter


def show_statistics(results):
    total_timeout = sum([1 for result in results if result["time_out"]])
    total_played = sum([result["played"] for result in results])
    count_winner = Counter()
    for result in results:
        behaviour = str(result['behaviour'])
        count_winner[behaviour] += 1
    print(
        '#' * 80
    )
    print(
        f"Numero de partidas terminadas por timeout: "
        f"{total_timeout}"
    )
    print(
        '-' * 40
    )
    print(
        f"Numero de turnos em média que uma partida demora: "
        f"{total_played / len(results):.1f}"
    )
    print(
        '-' * 40
    )
    print("A porcentagem de vitórias por comportamento dos jogadores")
    for behaviour, winner in count_winner.most_common():
        print("  *  ", f"{behaviour}: {(winner * 100)// len(results)}%")
    print(
        '-' * 40
    )
    print(
        f"""O comportamento que mais venceu:
        -> {count_winner.most_common(1)[0][0]} <-
    	venceu: {count_winner.most_common(1)[0][1]} vezes"""
    )
    print(
        '#' * 80
    )
