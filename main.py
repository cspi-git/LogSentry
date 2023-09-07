import watchers.windowsdefender as WindowsDefender
import os, sys, time
import asyncio

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

watching_config = {
    "WindowsDefender": False
}

class colors:
    darkred = "\033[31m"
    red = "\033[91m"
    lightred = "\033[38;5;196m"
    darkgreen = "\033[32m"
    green = "\033[92m"
    lightgreen = "\033[38;5;46m"
    darkyellow = "\033[33m"
    yellow = "\033[93m"
    lightyellow = "\033[38;5;226m"
    darkblue = "\033[34m"
    blue = "\033[94m"
    lightblue = "\033[38;5;21m"
    reset = "\033[0m"

banner = f"""{colors.blue}
                                         ...:^^~~~~~~~^::..                                         
                                .:!JPB#&@@@@@@@@@@@@@@@@@@@@&&BPJ!^.                                
                          .^7P#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P?^.                          
                      .!P&@@@@@@@@@&##@@@@@@@@@@@@@@@@@@@@@@@@@#&@@@@@@@@@&G7.                      
                  .~P&@@@@@@@&BY!..!G&@@@@@@@@@@@@@@@@@@@@@@@@@&5~:~YB&@@@@@@@&P!.                  
               .7B@@@@@@@#Y~.    ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B^   .^JB@@@@@@@#?.               
             !B@@@@@@&5~.      ?@@@@@@@@@@@@@@&BGPPPG#&@@@@@@@@@@@@@#^      ^Y#@@@@@@#7.            
          :P@@@@@@#?.        .#@@@@@@@@@@@G7:          .^J#@@@@@@@@@@@Y        .7B@@@@@@P:          
        ~B@@@@@&J.          :@@@@@@@@@@&!                  .5@@@@@@@@@@G          .?&@@@@@#!        
      ~#@@@@@B~            .&@@@@@@@@@7   ^JGGY~             .P@@@@@@@@@G            :P@@@@@&!      
    ^#@@@@@P:              B@@@@@@@@&.  .#@@@@@@@~             ?@@@@@@@@@7             .Y@@@@@&~    
  .G@@@@@P.               ^@@@@@@@@@:   P@@@@@@@@@              P@@@@@@@@&               .5@@@@@B.  
 7@@@@@B.                 Y@@@@@@@@B    ~@@@@@@@@5              .@@@@@@@@@:                .G@@@@@J 
Y@@@@@P                   P@@@@@@@@5     .JB&&#P^                &@@@@@@@@~                  J@@@@@G
 Y@@@@@5.                 Y@@@@@@@@B                            .@@@@@@@@@:                 Y@@@@@P.
  :#@@@@@J                ^@@@@@@@@@.                           Y@@@@@@@@&                ?@@@@@&^  
    7&@@@@@J.              B@@@@@@@@&.                         !@@@@@@@@@J              ?&@@@@@7    
      ?&@@@@@5.            .@@@@@@@@@&~                       Y@@@@@@@@@B            .Y@@@@@@J      
        7&@@@@@#!           ^@@@@@@@@@@B~                   ?&@@@@@@@@@#           ~B@@@@@&?        
          ~B@@@@@@G~.        .#@@@@@@@@@@&5^.           .!G@@@@@@@@@@@P         ~P@@@@@@#!          
            .Y&@@@@@@B?:       J@@@@@@@@@@@@@&BG5JJJ5G#&@@@@@@@@@@@@&~      .7G@@@@@@&Y.            
               :Y&@@@@@@&G7:     J&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#~    :7P&@@@@@@&5:               
                  .?B@@@@@@@@#P?^..!G@@@@@@@@@@@@@@@@@@@@@@@@@@&P~.:7P#@@@@@@@@#J:                  
                      ^JB&@@@@@@@@&#GB&@@@@@@@@@@@@@@@@@@@@@@@&B#&@@@@@@@@@BJ^                      
                          .!YB&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B5!.                          
                               .:!JPB&&@@@@@@@@@@@@@@@@@@@@@@&&BPJ!:.                               
                                        ..:^~~7??????7~~^^...                                       
{colors.reset}"""

def main():
    divider = "-" * 20
    while True:
        clear()

        for char in banner:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0000001)

        print(colors.blue + "\n\n" + divider + " | LogSentry Watching | " + divider + colors.reset)
        print(f"{colors.darkblue}1. Windows Defender: " + str(watching_config["WindowsDefender"]) + f"{colors.reset}")
        print(f"{colors.darkblue}2. Start LogSentry{colors.reset}")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            watching_config["WindowsDefender"] = not watching_config["WindowsDefender"]
        elif choice == "2":
            print(f"\n{colors.green}Windows Defender watcher was started!{colors.reset}")
            while True:
                try:
                    asyncio.run(WindowsDefender.Watch())
                except KeyboardInterrupt:
                    print(f"{colors.red}Windows Defender watcher was stopped!{colors.reset}")
                    break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()