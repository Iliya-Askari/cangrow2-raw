import requests
import json

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAr7cHMJjnBL7GxYXpaP1RYVaUSpuOCcsI"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": (
                        "سلام من یکسری کلمات کلیدی هست و احتمال مدل من کلمات غیر ضروری هم اورده  "
                        "که از کسی هست رزومه اش این موارد رو کم داره 'سلام من یکسری کلمات کلیدی هست که از کسی هست رزومه اش این موارد رو کم داره\n\n"
                        "['frontend', 'backend', 'interfaces', 'appealing', 'seamless', 'experiences', 'users', 'visually', 'collaborate', 'create', "
                        "'ensuring', 'work', 'solutions', 'infrastructure', 'providing', 'server', 'databases', 'creating', 'aspects', 'application']\n\n"
                        "و من ازت میخوام یه نقشه راه به کاربر بدی که باید جیا یاد بگیره و جه کار هایی باید انجام و اگر دید کلمه ای اضافه و بی مورد هست "
                        "در نظر نگیر و باید دقت بالایی نقشه راه بده اگر هر زبان یا کتاب خونه ایی از اون زبون رو باید یاد بگیره بگو در ضمن باید طبق استاندارد "
                        "نقشه راه بدی و من ازت میخوام یه نقشه راه به کاربر بدی که باید جیا یاد بگیره و جه کار هایی باید انجام و اگر دید کلمه ای اضافه و بی مورد هست "
                        "در نظر نگیر و باید دقت بالایی نقشه راه بدی اگر هر زبان یا کتاب خونه ایی از اون زبون رو باید یاد بگیره بگو در ضمن باید طبق استاندارد "
                        "نقشه راه بدی و حتما انگلیسی باشه و چون این پرامت من با api وصل میکنم توضیحات اول و اخر رو نیاز ندارم و بهم توضیح نده فقط نقشه راه "
                        "به زبان انگلیسی بفرست منظورم اینه که توضیحات ندی اینه که مثل این دستوراتی هستی که پاسخ به من میدی من یک نرم افزار دارم و با api به تو وصل "
                        "شدم و میخوام به محض اینکه پرامت فرستادم نقشه راه باشه و در اول و اخر هیچی نباشه و باید بدون فرمت خاصی باشه باید فرمت txt باشه"
                    )
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    text = result['candidates'][0]['content']['parts'][0]['text']

    # حذف کاراکترهای ` * -
    for char in ['`', '*', '-']:
        text = text.replace(char, '')

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
else:
    print(f"Error: {response.status_code}")
    print(response.text)

