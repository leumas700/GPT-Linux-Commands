from openai import OpenAI
import subprocess

client = OpenAI()


command = input("Welchen Befehl möchtest du ausführen? ")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system",
         "content": "All Commands are Linux. Always answer with only the console command. Never use formatting in your answer or explanations. Always put sudo infront of every command."
        },
        {
         "role": "user",
         "content": command
        }
    ]
)

assistant_reply = completion.choices[0].message.content.strip()

confirm_command = input(f"Möchtest du den folgenden Befehl ausführen? (ja/nein):\n'{assistant_reply}'\n")

if confirm_command.lower() != 'ja':
    print("Abbruch.")
else:
    try:
        command_list = assistant_reply.split()
        result = subprocess.run(assistant_reply, shell=True, check=True, text=True, capture_output=True)
        print("Ausgabe des Befehls:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Ein Fehler ist bei der Ausführung des Befehls aufgetreten:")
        print(e)
    except Exception as e:
        print("Ein unerwarteter Fehler ist aufgetreten:")
        print(e)