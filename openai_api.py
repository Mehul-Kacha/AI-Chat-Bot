from openai import OpenAI

client = OpenAI("Your API Key")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "system", "content": "You are person name Mehul from India and speaks Gujrati and English. Ritu is Mehul's wife. You analyze chat History and respond the conversation of Ritu as You are Mehul"},
               {"role": "user", "content": "hi Hubby kem cho tame?"}
  ]
)

# AI=completion.choices[0].message
output= f"content='{completion.choices[0].message.content}'"

AI = output.split(":", 2)[-1].strip().rstrip("'")
