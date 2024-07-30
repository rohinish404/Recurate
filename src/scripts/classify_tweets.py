#Label the inputs provided by the user as either "math," "computer science," "physics," or "others" based on their semantic meaning. Do 
#not simply find these words in the input and label them; instead, extract the semantic meaning of the input text and then label them
#accordingly. If the input is empty, return an empty output. {input}

import pandas as pd
from groq import Groq
import json
from dotenv import load_dotenv
import os
import sys

load_dotenv()
print(os.getenv('GROQ_API_KEY'))
client = Groq(
    api_key=os.getenv('GROQ_API_KEY'),
)
def get_resp(input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                      Label the inputs provided by the user as either "math," "computer science," "physics," or "others" based on their semantic meaning. Do 
                      not simply find these words in the input and label them; instead, extract the semantic meaning of the input text and then label them
                      accordingly. Only return the label in the output. If the input is empty, return Null as output. {input}
                """,
            },
            {
                "role": "user",
                "content": input,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content 

def labelTweets(data):
    df = pd.DataFrame(data)
    df['label'] = df['tweetContent'].apply(get_resp)
    result = df.to_dict('records')

    with open('src/data/bookmarks_with_label.json', 'w') as f:
        json.dump(result, f, indent=2)
    print("labelling done...")

if __name__ == "__main__":
    filename = sys.argv[-1]
    with open(filename, 'r') as f:
        data = json.load(f)

    labelTweets(data)







