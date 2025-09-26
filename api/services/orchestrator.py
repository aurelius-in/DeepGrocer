import asyncio, json, os, signal as pysignal
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from agents import task_router, queueflow


async def tick_queueflow():
    # mock signal sampling
    payload = {"traffic": 90}
    queueflow.run(payload)


async def tick_task_router():
    # mock task batch
    payload = {"tasks":[{"id":"restock-001"},{"id":"restock-002"}]}
    await task_router.run_once(payload)


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick_queueflow, "interval", seconds=30, id="queueflow")
    scheduler.add_job(tick_task_router, "interval", seconds=45, id="task_router")
    scheduler.start()
    stop = asyncio.Event()
    for sig in (pysignal.SIGINT, pysignal.SIGTERM):
        asyncio.get_event_loop().add_signal_handler(sig, stop.set)
    await stop.wait()


if __name__ == "__main__":
    asyncio.run(main())

