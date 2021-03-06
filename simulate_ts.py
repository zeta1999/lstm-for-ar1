from random import seed, gauss
from typing import List, Callable, Any, Generator

seed(42)


def get_ar_ts(
    alpha: float, beta: float, sigma: float, init_x: float, num_ts: int
) -> Generator[float, None, None]:
    x = init_x
    i = 0
    while i < num_ts:
        yield x
        x = alpha + beta * x + gauss(0, sigma)
        i = i + 1


def simulate_many(f: Callable[[], Any], num_sim: int) -> List[Any]:
    return [f() for _ in range(num_sim)]

