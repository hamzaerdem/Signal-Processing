'''
Author's (on Github)

@hamzaerdem
@muratcanabay
@onuro315
@NADS666
@berkay-net95

'''

from __future__ import division  

import sys
import re 
import signal_manipulations as signal

def horizontal_input(arg):

	if(arg[0]=='t'):

		arg[0] = 1 
	
	elif(arg[0]=='-t'):

		arg[0] = -1

	else:	
		arg[0] = float(eval(arg[0][:-1])) 
		
	if len(arg) > 1:
		
		arg[2] = float(eval(arg[2]))

def vertical_input(arg):

	arg[0] = arg[0].rsplit('(')
	arg[0][1] = arg[0][1].rsplit('t')[0]


	if(arg[0][0]==''):
	
		arg[0][0] = 1

	elif(arg[0][0]=='-'):
				
		arg[0][0] = -1

	else:
		arg[0][0] = float(eval(arg[0][0]))

	if(arg[0][1]==''):
				
		arg[0][1] = 1
	
	elif(arg[0][1]=='-'):
				
		arg[0][1] = -1	
								
	else:
		arg[0][1] = float(eval(arg[0][1]))							
				
	if(len(arg)>2):
				
		arg[2] = arg[2].rsplit(')')[0]	
		arg[2] = float(eval(arg[2]))
			
	if(len(arg)>3):
		arg[4] = float(eval(arg[4]))		

def get_args():

	patternA = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)t"
			     "( )(\+|\-)"
			     "( )\d*(\.\d+)?|(\/\d+)?$") 

	patternB = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)t$")

	patternC = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)\(-?\d*((\.\d+)?|(\/\d+)?)t"
			     "( )(\+|\-)?"
			     "( )\d*((\.\d+)?|(\/\d+)?)\)?"
			     "( )(\+|\-)"
			     "( )\d*(\.\d+)?|(\/\d+)?$")

	patternD = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)\(-?\d*((\.\d+)?|(\/\d+)?)t"
			     "( )(\+|\-)"
			     "( )\d*((\.\d+)?|(\/\d+)?)\)?$")

	patternE = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)\(-?\d*((\.\d+)?|(\/\d+)?)t\)"
			      "( )(\+|\-)"
			      "( )\d*((\.\d+)?|(\/\d+)?)$") 
	
	patternF = re.compile("^-?\d*((\.\d+)?|(\/\d+)?)\(-?\d*((\.\d+)?|(\/\d+)?)t\)") 
	
	print "\n-- SIGNAL PROCESSING --"
	print "\nWhich process you want to make?"	
	print "1.Type 'H' for Horizontal Axis Manipulation"
	print "2.Type 'V' for Vertical Axis Manipulation"
	print "3.Type 'HV' for Horizontal&Vertical Axis Manipulation"

	while True:	
		
		choose = raw_input("\n--> ").upper()
		
		if(choose == 'H'):

			while True:
				arg = raw_input("\nx(t) >>> : ")

				if patternA.match(arg) or patternB.match(arg):
					arg = [item for item in arg.split(' ') if item.strip()]
					break
				else: 
					print ("Wrong input ! Please write in format -> '2t + 1', '2t - 1' or '3t' , '1/2t' ")
						
			horizontal_input(arg)			

			return choose, arg

		elif(choose == 'V'):

			while True:
				arg = raw_input("\na.x(t) + c >>> : ")

				if patternC.match(arg) or patternE.match(arg) or patternF.match(arg):
					arg = [item for item in arg.split(' ') if item.strip()]
					break
				else: 
					print ("Wrong input ! Please write in format -> '5(t) + 1', '1/2(t) + 1'")
			
			vertical_input(arg)			

			return choose, arg

		elif(choose == 'HV'):

			while True:
				arg = raw_input("\na.x(t + 1) + c >>> : ")

				if patternC.match(arg) or patternD.match(arg):
					arg = [item for item in arg.split(' ') if item.strip()]
					break
				else: 
					print ("Wrong input ! Please write in format -> '5(t + 1) + 1', '2(t + 1)' ")

			vertical_input(arg)
			
			return choose, arg

		else:
			print "\nTry Again!"


choose, arg = get_args()

if(choose=='H'):

	signal.horizontal(arg)

elif(choose=='V'):

	signal.vertical(arg)

elif(choose=='HV'):

	signal.horizontal_vertical(arg)
