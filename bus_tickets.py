from typing import List


def get_lucky_bus_tickets(N: int) -> List[int]:
    start = 100000
    end = 1000000
    lucky_tickets = []

    for i in range(start, end):
        first_sum = sum(int(j) for j in f"{i}"[:3])
        last_sum = sum(int(j) for j in f"{i}"[3::])
        if first_sum == last_sum:
            lucky_tickets.append(i)
            if len(lucky_tickets) == N:
                break

    return lucky_tickets


def main():
    print(get_lucky_bus_tickets(10000))


main()