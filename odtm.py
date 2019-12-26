#!/usr/bin/pytyon2
#D@rk_Devil#666

import os 
import time 
import sys 

system = os.system
sleep = time.sleep
exit = sys.exit 

def loadinggan():
    loadingdulu = [ '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[/]', '[-]', '[\]', '[|]', '[\033[1;32m✓\033[1;37m]' ]
    for a in loadingdulu:
        print '\r\033[1;32m[\033[1;33m+\033[1;32m] \033[1;33mLoading' + a,
        sys.stdout.flush()
        sleep(0.1)
        
def intro():
    loadinggan()
    system("pkg install figlet")
    system("pkg install ruby")
    system("gem install lolcat")
    system("pkg install mpv")
    system("cd $HOME")
    system("cd odtm")
    system("mpv * ls")
    system("rm -rf intro.mp3")
    loadinggan()
    main()
    
def main():
    system("figlet ODTM | lolcat")
    print ""
    sleep(0.2)
    print "^_^ Selamat datang ^_^"
    sleep(0.2)
    print "^_^ Silahkan ketik angka 1 ^_^"
    sleep(0.2)
    ea = raw_input("\033[1;32m=> \033[1;37m")
    if ea == "1" or ea == "01":
        system("pkg install python")
        system("pkg install git")
        system("pip install requests")
        system("pip install mechanize")
        system("git clone https://github.com/Darkdevil730/Facetapp")
        system("cd Facetapp")
        system("python FacetappV1-3fixbug.py")
        main()
        
    elif ea == "exit":
        exit(1)
        
    elif ea == "admin":
        print "odtm merupakan salah satu gc yg paling saya senangi"
        print "karena tiap hari ada pembagian sembako, eh itu yg punya sapi tolong di pinggirin sapinya"
        sleep(2)
        print "nah, berhubung hari hujan, besok aja deh"
        sleep(3)
        print "aduh mata ngantuk nih besok aja deh"
        sleep(3)
        print "udh tidur, tapi lapar, makan dulu deh"
        sleep(3)
        print "udh makan, tapi lele tetangga kan belum makan, ternak lele dulu deh"
        sleep(3)
        print "gitu aja terus sampai ajal menjemput"
        sleep(3)
        print ""
        print "Ajal : hahahaha kau akan mati manusia"
        print "homan : besok aja deh"
        print "Ajal : ehhhhh ??"
        sleep(3)
        
    else:
        print "wah, sepertinya mata anda harus dicongkel bogeng"
        exit(1)
        
if __name__ == "__main__":
    intro()
    