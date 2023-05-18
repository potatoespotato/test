import pytest
import random
from bus_tickets import get_lucky_bus_tickets


def test_bus_tickets():
    N = random.randint(0, 45)

    lucky_bus_tickets = get_lucky_bus_tickets(N)
    assert len(lucky_bus_tickets) == N

    random_ticket = random.choice(lucky_bus_tickets)

    first_sum = sum(int(j) for j in f"{random_ticket}"[:3])
    last_sum = sum(int(j) for j in f"{random_ticket}"[3::])

    assert first_sum == last_sum
