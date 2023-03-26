import openai

openai.api_key = "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"

def get(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Firefox assistant in UBUNTU and your role is to write a pyautogui script to execute any command given by the user."},
        {"role": "system", "content": "You can only use pyautogui to perform actions. And you are not allowed to give any comments or suggestions."},
        {"role": "user", "content": "Open new tab"},
        {"role": "assistant", "content": "pyautogui.hotkey('ctrl','t')\n"},
        {"role": "user", "content": "focus on search bar"},
        {"role": "assistant", "content": "pyautogui.press('/')\n"},
        {"role": "user", "content": "open twitter"},
        {"role": "assistant", "content": "pyautogui.hotkey('ctrl','t')\npyautogui.typewrite('twitter.com')\npyautogui.press('enter)\ntime.sleep(5)"},
        {"role": "user", "content": prompt},
    ]
    )
    
    return response.choices[0].message.content