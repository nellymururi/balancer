import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt
import pandas as pd


async def make_request(session, url):
    start_time = time.time()
    async with session.get(url) as response:
        await response.text()
    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken


async def main():
    url = 'http://localhost:5001/home'
    num_requests = 10000

    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, url) for _ in range(num_requests)]
        times = await asyncio.gather(*tasks)

    # Process the responses
    total_time_taken = sum(times)

    # Print the total requests and total time taken
    print(f'Total Requests: {num_requests}')
    print(f'Total Time Taken: {total_time_taken} seconds')

    # Create a DataFrame from the counts and times
    df = pd.DataFrame({
        'Metrics': ['Total Requests', 'Total Time Taken'],
        'Values': [num_requests, total_time_taken]
    })

    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot a bar chart of the counts and times with different colors
    bars = ax.bar(df['Metrics'], df['Values'], color=['blue', 'green'])

    # Set the labels for the x-axis
    ax.set_xlabel('Metrics')
    ax.set_ylabel('Values')

    # Set the legend labels
    ax.legend(bars, df['Metrics'])

    # Set the title for the graph
    ax.set_title('Performance for 10000 async requests')

    # Space out the subplots
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    asyncio.run(main())
