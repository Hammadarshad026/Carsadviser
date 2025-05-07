import re
from together import Together



def get_car_advice(question):
    client = Together(api_key="tgp_v1_neH8Hsj4eDnKPTx38QkCT6Kf-SBGktdQ7hFQkjC6vfs")
    response = client.chat.completions.create(
    model="Qwen/Qwen3-235B-A22B-fp8-tput",
    messages=[{
                            "role": "system",
                            "content": "You are an expert car advisor for the Pakistani market.Recommend cars based on price range, fuel type, fuel efficiency, maintenance cost, and features.When comparing two cars, explain the pros and cons clearly and suggest the better option.Keep your answer helpful  and relevant to Pakistani roads and fuel conditions.Note: Answer should be very very to the point and do not mention about price in responce "
                        },
                        {"role": "user", "content": question}]
    )
    full_content = response.choices[0].message.content
    
    
    clean_content = re.sub(r"<think>.*?</think>", "", full_content, flags=re.DOTALL).strip()
    # print(clean_content)

    return clean_content


# question="which is beast alto and civic" 
# get_car_advice(question)