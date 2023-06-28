# Import DuckDuckGoSearch from langchain tools as well as gpt4all.
from langchain.tools import DuckDuckGoSearchRun
import gpt4all
from datetime import datetime
import time

today = datetime.today()
formatted_date = today.strftime('%d %B')

# Instantiate the class
search = DuckDuckGoSearchRun()

# Run the search.
start_time = time.time()
result = search.run(f"Cape Town weather {formatted_date}")

query = f"Based on this text, '{result}' give a bullet point summary of the expected " \
        f"weather for {formatted_date} in Cape Town. The points must only " \
        f"include temperature information, precipitation and wind information. Exclude any other information." \
        f"The response format should be:" \
        f"Max Temperature: \n" \
        f"Min Temperature: \n" \
        f"Precipitation: \n" \
        f"Wind Speed: \n."

gptj = gpt4all.GPT4All("GPT4All-13B-snoozy.ggmlv3.q4_0")
messages = [{"role": "user", "content": query}]
gptj.chat_completion(messages)
end_time = time.time()
execution_time = end_time - start_time

minutes = int(execution_time // 60)
seconds = int(execution_time % 60)

print(f"\nThe script took {minutes} minutes and {seconds} seconds to run.")
