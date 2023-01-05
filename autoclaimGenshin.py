import asyncio
import genshin

async def main():
    cookies = {"ltuid": 25089082, "ltoken": "4P3cU29tyXw2pVSS01MukdJhvSPF16GoGi7gQJxF"}
    client = genshin.Client(cookies, game=genshin.Game.GENSHIN)

    # claim daily reward
    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        print("Daily reward already claimed")
    else:
        print(f"Claimed {reward.amount}x {reward.name}")


asyncio.run(main())
