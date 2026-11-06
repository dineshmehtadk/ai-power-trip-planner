
#openai/gpt-oss-120b

import asyncio
from mcp_client import weather_mcp_search,forecast_mcp_search

async def main():
    try:
        result = await forecast_mcp_search("New Delhi")
        print("Weather result:")
        print(result)
    except Exception as exc:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())