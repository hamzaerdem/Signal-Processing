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
import matplotlib.pyplot as plt

def drawGraph(x, y, title, legend):
	
	plt.title(title + " Axis Manipulation")
	plt.gcf().canvas.set_window_title('Signal Processing')
	plt.plot([1,0], [0,1], label = 'Signal', color = '#e60000', linewidth = 3)
	plt.plot(x, y, label = legend, color = '#009900', linewidth = 3	)
	plt.legend()
	
	plt.grid(True, color='#9C27B0', linewidth = 2)
	plt.show()

def horizontal(a):

	x = [1,0]
	y = [0,1]

	#t*constant
	#Time Compression #Time Reversal #Time Expansion

	if(a[0] > 1):	

		legend = 'Time Compression'
						
	elif(a[0] < 0):

		legend = 'Time Reversal'
		
	else:	
				
		legend = 'Time Expansion'	

	x[0] = x[0]/a[0]		
	
	#(t*constant) +- constant

	if len(a) > 1:
		
		if(a[1]=='+'):
			
			#Delay and #Scale
			
			x = [((x[0] - a[2]) / a[0]) , ((-a[2]) / a[0])]

			legend += ' and Advance(leftShifthing)'
		
		elif(a[1]=='-'):

			#Advance and #Scale

			x = [(x[0]+ a[2])/a[0], (a[2]/a[0])]

			legend += ' and Delay(rightShifthing)'

	drawGraph(x, y, "Horizontal", legend)

def vertical(a):
	
	x = [1,0]
	y = [0,1]

	if (a[0][0]>=1): 

		legend = 'Amplification'					
	
	elif (0<a[0][0]<1):

		legend = 'Attenuation'					

	else: 

		legend = 'Sign Change'

	y[1] = y[1]*(a[0][0])

	if len(a) > 1:

		if(a[1]=='+'):

			y = [(y[0]+a[2]), (y[1]+a[2])]
			legend += ' and upShifting'		

		elif(a[1]=='-'):
		
			y = [(y[0]-a[2]), (y[1]-a[2])]
			legend += ' and downShifting'
		
	drawGraph(x, y, "Vertical", legend)

def horizontal_vertical(a):

	x = [1,0]
	y = [0,1]

	if(a[1]=='+'):
			
		x = [((x[0] - a[2]) / a[0][1]) , ((-a[2]) / a[0][1])]
		legend = 'Left Shifting,'
			
	elif(a[1]=='-'):

		x = [(x[0]+ a[2])/a[0][1], (a[2]/a[0][1])]
		legend = 'Right Shifting,'

	if a[0][0]>=1: 

		legend += ' Amplification'					
	
	elif 0<a[0][0]<1:

		legend += ' Attenuation'					

	else: 
		legend += ' Sign Change'

	y[1] = y[1]*(a[0][0])

	if len(a) > 3:

		if(a[3]=='+'):

			y = [(y[0]+a[4]), (y[1]+a[4])]
			legend += ' and upShifting'		

		elif(a[3]=='-'):
		
			y = [(y[0]-a[4]), (y[1]-a[4])]
			legend += ' and downShifting'

	drawGraph(x, y, "Horizontal and Vertical", legend)

