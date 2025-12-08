import sys

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    count = 0

    # states
    Start = True
    TMenuOpen = False
    NoMenu = False
    RMenuOpen = False
    TextBoxSelected = False
    CheckTextBox = False
    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!

        # Choose action message to respond with
        # IMPORTANT! My example code does something silly ...
        # - if you click on a vertex, the "Recentering Pane" will appear,
        #   and when you leave the "canvas", it disappears.  See why?
        response = "noop 0"
        match msg:
            case 'documentReady':
                Start = False
                NoMenu = True
            case 'click':
                if TMenuOpen:
                    response = "hideTP " + data
                    TMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    response = "hideCP " + data
                    RMenuOpen = False
                    NoMenu = True
            case 'clickOnCanvas':
                if TMenuOpen:
                    response = "hideTP " + data
                    TMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    response = "moveC " + data + '\n' + "hideCP " + data  #this one is weird
                    RMenuOpen = False
                    NoMenu = True
            case 'clickTriChooseButton':
                response = "showTP " + data
                TMenuOpen = True
                NoMenu = False
            case 'clickRecenterButton':
                if NoMenu:
                    RMenuOpen = True
                    NoMenu = False
                    response = "showCP " + data
    
                elif TMenuOpen:
                    response = "hideTP " + data + "\n" + "showCP " + data
                    TMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    response = "hideCP " + data
                    RMenuOpen = False
                    NoMenu = True
            # not implemented
            case 'clickRecenterPane':
                if NoMenu:
                    pass    
                elif TMenuOpen:
                    pass
                elif RMenuOpen:
                    pass


            
            # default
            case _:
                print(f'No handler for: {msg}',file=sys.stderr)
        #NOT IMPLEMENTED
        """
        case 'clickRecenterTextBox':
            pass
        case 'clickTriTypeChoice':
            pass
        case 'mouseDownVertex':
            pass
        case 'mouseLeaveCanvas':
            pass
        case 'mouseMove':
            pass
        case 'mouseUpCanvas':
            pass 
        case 'recenterTextChange':
            pass
        case 'recenterTextFail':
            pass
        case 'recenterTextSucc':
            pass
        """
        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!

        