import openai

client = openai.Client(api_key='YOUR_API_KEY')

def get_openai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Generate HTML content for the following article. Only include content between <body> and </body> tags, without using <html>, <head>, <body> tags or any CSS/JavaScript."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1024
    )
    return response.choices[0].message.content.strip()

input_file_path = 'D:/OXIDO/Oxido - Project/Zadanie dla JJunior AI Developera - tresc artykulu.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    article_text = file.read()

prompt = f"Przeformatuj ten tekst jako HTML, uwzględniając miejsca na grafikę: {article_text}"

html_content = get_openai_response(prompt)

output_file_path = 'D:/OXIDO/Oxido - Project/artykul.html'

with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML generated and saved in the file 'artykul.html'.")
