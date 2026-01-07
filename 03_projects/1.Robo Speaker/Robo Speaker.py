import os
if __name__  == '__main__':
    print ('welcome to RoboSpeaker 1.1 created by Pramod')
    while True:
        x=input('what you want to speak = ') 
        if x =='q':
            os.system("say 'Bye Bye friends'")
            break
        command = f"say {x}"
        os.system(command)