from plingo import Plingo

if __name__ == "__main__":
    lingo = Plingo()

    result = ""
    for idx, cmd in enumerate(sorted(lingo._commands)):
        try:
            method = getattr(lingo, cmd)

            command = cmd[9:]

            doc = method.__doc__
            if not doc:
                doc = "_not yet documented_"

            result = f"{result}## {idx:03d} - {command} \n\n{doc} \n\n"
        except:
            result = f"{result}## {idx:03d} - {command} \n\nNot implemented yet \n\n"

    print(result)
