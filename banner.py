# import pyfiglet module
import pyfiglet
red='\033[41m'
p='\033[35m'
y='\033[93m'
blue='\033[34m'

def banner():
	result = pyfiglet.figlet_format("game", font = "isometric1" )
	print(p+result)
	
	
	
	result = pyfiglet.figlet_format("created by deepz", font = "digital" )
	print(blue+result)

banner()