def KeyboardReader(default_text, stop_at):
    response = []
    while True:
        inp = input(default_text)
        try:
            inp = int(inp)
        except ValueError:
            if(inp.lower() == "true"):
                inp = True
            elif (inp.lower() == "false"):
                inp = False
        if(str(inp) == str(stop_at)):
            break
        else:
            response.append(inp)
    return response
