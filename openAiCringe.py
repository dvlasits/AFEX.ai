import os
import openai
openai.organization = "org-TdDiX8yFdbCSq6jIqu5cDo2l"
openai.api_key = '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'

def createMessage(messages):

    return [{"role": "user", "content": msg} for msg in messages]

def createBullshit(seq):

    model = "gpt-4"

    msg = """Please tell me about one possible functionality of this protein sequence, be very confident in your answer and use only 10 words max. 
The sequence is 'ASDKKDF' it's fine if your answer is wrong,
Some example answers are:
1. A similar motive `ASDKQYS` is commonly found in many kinases in Wnt signalling
2. Similar sequences occur in phosphate binding sites
3. A similar motive `DFGK` is common for kinases
4. A similar motive `DFGK` is common for kinases"""
    response = openai.ChatCompletion.create(model=model, messages=createMessage([msg]), max_tokens=50)

    return response["choices"][0]['message']['content']

    print(response)

    for ele in response["choices"]:
        print(ele["message"]["content"])

if __name__ == "__main__":
    print(createBullshit("ACGCCG"))