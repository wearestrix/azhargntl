## STRIX.py - STRIX v1.0
# -*- coding: utf-8 -*-
import os
import sys
import time

strix_banner = """
     [4] Kembali 
	 [05] keluar dari STRIX
"""	 
	 
	 def restart_program():
          	python = sys.executable
			os.execl(python, python, * sys.argv)
			curdir = os.getcwd
			
	def backtomenu_option()
        print backtomenu_banner
		backtomenu = raw_input("strix >")
		if backtomenu == "00":
		        restart_program()
		elif backtomenu == "05":
                sys.exit()
		else:
		       print "\nERROR: Wrong Input"
		        time.sleep(2)
		        restart_program()
				
	def Fbbruteforce():
                    print '\n####### Install Fbbruteforce'
					os.system('apt update && apt upgrade')
					os.system('git clone https://github.com/tikuskecil/multi-bruteforce-facebook')
					os.system('apt insatll pip2')
					os.system('pip2 install mechanize')
					os.system('mv Fbbruteforce ~')
					print '@@@@@ Done'
					backtomenu_option()
					
	def	spammer_email():
	            print '\n####### Installing spammer-Email'
				os.system("apt update && apt upgrade")
				os.system("apt install git python2 && pip2 install argparse requests")
				os.system("git clone https://github.com/p4kl0nc4t/Spammer-Email")
				os.system("mv spammer-Email~")
				print '@@@@@ Done'
				backtomenu_option()
	
	def 