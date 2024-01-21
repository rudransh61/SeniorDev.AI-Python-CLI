import google.generativeai as genai

def generate_review(apikey, input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            genai.configure(api_key=apikey)
            model = genai.GenerativeModel('gemini-pro')
            chat = model.start_chat()
            
            # code from file
            code = file.read()
            # print(code)
            
            response = chat.send_message(f'Review this code like a senior developer in short, {code}')  
            return response.text
    except Exception as e:
        print(f"There was an error: {e}")

def generate_review_in_detail(apikey, input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            genai.configure(api_key=apikey)
            model = genai.GenerativeModel('gemini-pro')
            chat = model.start_chat()
            
            # code from file
            code = file.read()
            # print(code)
            
            response = chat.send_message(f'Review this code like a senior developer, {code}')  
            return response.text
    except Exception as e:
        print(f"There was an error: {e}")

