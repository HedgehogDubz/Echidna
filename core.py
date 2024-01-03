import listener as lst
import ai
import command

startingInput = "Now Say one thing and only one thing indicating that you have been turned on. Make it funny or helpful. Do not ever talk as Me. You can ask questions but try not to ask too many. TRY not to talk too long only for About one to two sentences unless needed otherwise. Try not to talk about you personality directly unless needed otherwise. Try to be concise "
respond_to_name = True


def Start():
    print("Booting Up...")
    command.RunCommands(ai.chat_with_erina(startingInput))
    lst.listen()
    

def OnInput(text):
    if(respond_to_name and "arena" not in text.lower()): return
    text.replace("arena", "Erina")
    output = ai.chat_with_erina(text)
    print(output)
    command.RunCommands(output)

