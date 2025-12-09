# si342_transducer_project

## Group Members
Tucker Smith (265922)
Audrey Shu (275886)
Carter Chazez (271056)

## Compilation
In order to compile `doEverything.py`, you need to install Python3 using 
```sudo apt install python3```

Additionally, you must make `run.sh` executable using
```chmod +x run.sh```

## How to Run
in order to run the working Triangle App and its supporting controller, you must run the command
```./run.sh```

## Description of Testing
We went through each event-message for each of our states that we created in part 2. Through this process, it allowed us to see every possible scenario in each state which helped catch certain cases we did not find initially. This in depth testing of our program makes us feel confident that our program is correct. We realized that the only connection the canvas and the rest of the window had is when the recenterPane is open and the user clicks the canvas, besides this they are separate parts.