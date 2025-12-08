import sys

if __name__ == "__main__":
    frgui = open("fromGUI","r")
    togui = open("toGUI","w")
    count = 0

    # states
    TMenuOpen = False
    RMenuOpen = False
    NoMenu = False
    HoldingVertex = False
    OGCoords = None
    
    #error msg
    errormsg = "ERROR! Unexpected event message {eventMessage} while in state {i}"
    
    while True:
        # Read event message
        try:
            msg,data = frgui.readline().split(maxsplit=1);
        except:
            break
        count += 1
        print(f'Read({count}): {msg} {data}',file=sys.stderr) #4DEBUG!

        response = "noop 0"
        match msg:
            case 'documentReady':
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
                if HoldingVertex:
                    HoldingVertex = False
                if TMenuOpen:
                    response = "hideTP " + data
                    TMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    response = "moveC " + data + '\n' + "hideCP " + data
                    RMenuOpen = False
                    NoMenu = True
            case 'clickTriChooseButton':              
                if NoMenu:
                    response = "showTP " + data
                    TMenuOpen = True
                    NoMenu = False    
                elif TMenuOpen:
                    response = "hideTP " + data
                    TMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    response = "showTP " + data + '\n' + "hideCP " + data
                    NoMenu = False
                    RMenuOpen = False
                    TMenuOpen = True
            case 'clickRecenterButton':
                if NoMenu:
                    response = "showCP " + data
                    RMenuOpen = True
                    NoMenu = False
                elif TMenuOpen:
                    response = "hideTP " + data + "\n" + "showCP " + data
                    TMenuOpen = False
                    RMenuOpen = True
                    NoMenu = False
                elif RMenuOpen:
                    response = "hideCP " + data
                    RMenuOpen = False
                    NoMenu = True
            case 'clickRecenterPane':
                if NoMenu:
                    print(errormsg.format("ClickRecenterPane", "NoMenu"), file=sys.stderr)
                    # error
                    pass    
                elif TMenuOpen:
                    print(errormsg.format("ClickRecenterPane", "TMenuOpen"), file=sys.stderr)
                elif RMenuOpen:
                    # nothing
                    pass
            case 'clickRecenterTextBox':
                if NoMenu:
                    print(errormsg.format("ClickRecenterTextBox", "NoMenu"), file=sys.stderr)
                    pass    
                elif TMenuOpen:
                    print(errormsg.format("ClickRecenterTextBox", "TMenuOpen"), file=sys.stderr)
                elif RMenuOpen:
                    pass
            case 'clickTriTypeChoice':
                if NoMenu:
                    print(errormsg.format("ClickTriTypeChoice", "NoMenu"), file=sys.stderr)
                elif TMenuOpen:
                    response = "resetT " + data + "\n" + "hideTP " + data
                    TMenuOpen = False
                    RMenuOpen = False
                    NoMenu = True
                elif RMenuOpen:
                    print(errormsg.format("ClickTriTypeChoice", "RMenuOpen"), file=sys.stderr)
            case 'mouseDownVertex':
                response = "selectV " + data
                HoldingVertex = True
                OGCoords = data.split(':', 1)[1]
            case 'mouseLeaveCanvas':
                if HoldingVertex:
                    response = "moveV " + OGCoords
                    HoldingVertex = False
            case 'mouseMove':
                if HoldingVertex:
                    response = "moveV " + data            
            case 'mouseUpCanvas':
                HoldingVertex = False 
            case 'recenterTextChange':
                if NoMenu:
                    print(errormsg.format("recenterTextChange", "NoMenu"), file=sys.stderr)
                elif TMenuOpen:
                    print(errormsg.format("recenterTextChange", "TMenuOpen"), file=sys.stderr)
                elif RMenuOpen:
                    response = "checkCT " + data
            case 'recenterTextFail':
                if NoMenu:
                    print(errormsg.format("recenterTextFail", "NoMenu"), file=sys.stderr)
                elif TMenuOpen:
                    print(errormsg.format("recenterTextFail", "TMenuOpen"), file=sys.stderr)
                elif RMenuOpen:
                    response = "errorCT " + data
            case 'recenterTextSucc':
                if NoMenu:
                    print(errormsg.format("recenterTextSucc", "NoMenu"), file=sys.stderr)
                elif TMenuOpen:
                    print(errormsg.format("recenterTextSucc", "TMenuOpen"), file=sys.stderr)
                elif RMenuOpen:
                    response = "moveC " + data + "\n" + "hideCP " + data
                    RMenuOpen = False
                    NoMenu = True
            # default
            case _:
                print(f'No handler for: {msg}',file=sys.stderr)

        # Respond to GUI - flush to send line immediately!
        print(response + "\n",file=togui,flush=True)
        print(f'Sent({count}): {response}',file=sys.stderr) #4DEBUG!

        