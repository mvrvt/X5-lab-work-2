
import asyncio

from concurrent.futures import ProcessPoolExecutor
from timer import log, print_time


CLIENTS = [
    ("alice", 0.5),
    ("bob", 5.0),
    ("carol", 0.5),
    ("dave", 0.5),
    ("eve", 0.5),
]


def heavy_compute() -> int:
    h = 0
    for i in range(30_000_000):
        h = (h * 31 + i) & 0xFFFFFFFF
    return h



async def handle_request(
    client: str,
    duration: float,
    pool: ProcessPoolExecutor
) -> None:
    log(f"{client}: запрос принят")

    if client in ("bob", "dave", "eve"):
        loop = asyncio.get_running_loop()

        await loop.run_in_executor(
            pool,
            heavy_compute
        )
    else:
        await asyncio.sleep(duration)

    log(f"{client}: ответ отправлен")


async def main() -> None:
    with ProcessPoolExecutor(max_workers=3) as pool:
        coroutines = [
            handle_request(client, duration, pool)
            for client, duration in CLIENTS
        ]

        await asyncio.gather(*coroutines)



if __name__ == "__main__":
    with print_time():
        asyncio.run(main())
