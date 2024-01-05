from openai import OpenAI

MY_KEY = "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"

class myChatGPT:
    def __init__(self, company_name, stock_sym):
        self.name = company_name
        self.symbol = stock_sym
        self.client = OpenAI(api_key=MY_KEY)
        
    def send(self, message):
        if message != "":  
            stream = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                stream=True,)
  
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content, end="")          
        else:
            print("ERR: stringa vuota")