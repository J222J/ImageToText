# Made by Saba Kharebava (J222J on Github)
#                                         ▓▓▓▓████████████████▒▒▒▒                                                                                    
#                             ████████████▓▓▓▓####        ####████████████                                                                            
#                     ░░░░████████                                        ████████                                                                    
#                 ████████                                                                                                                            
#             ████████                                                            ####                                                                
#             ████                                                                    ▓▓▓▓                                                            
#         ████            ████                                            ▒▒▒▒            ████                                                        
#     ▒▒▒▒▒▒▒▒            ████                    ▓▓▓▓                                    ████                                                        
#     ████                ▓▓▓▓░░░░                ████████            ▒▒▒▒####                ████                                                    
#     ████                    ########        ████    ████            ####▓▓▓▓                ████                                                    
# ▒▒▒▒░░░░                ####    ####                ▓▓▓▓████            ▒▒▒▒                ████░░░░                                                
# ████                    ▒▒▒▒    ####    ####            ████            ░░░░                ▒▒▒▒████                                                
# ████                    ▒▒▒▒    ####████                ▒▒▒▒            ░░░░                ####████                                                
# ████                    ####        ░░░░                    ████        ####                ####████                                                
# ▒▒▒▒####                ░░░░    ████▓▓▓▓░░░░                ####▒▒▒▒▓▓▓▓▓▓▓▓                ▒▒▒▒▒▒▒▒                                                
#     ████                ▒▒▒▒▓▓▓▓▒▒▒▒████████████████####████                                ████                                                    
#     ████                ▒▒▒▒▓▓▓▓        ████            ####        ▓▓▓▓                    ████                                                    
#     ▒▒▒▒░░░░                            ████████    ▒▒▒▒                                ████####                                                    
#         ████                                ████    ████                                ████                                                        
#             ████                            ████████                                ▒▒▒▒                                                            
#             ████░░░░                            ████                            ░░░░░░░░                                                            
#                 ████░░░░                                                    ####░░░░                                                                
#                     ▓▓▓▓░░░░                                            ░░░░
#                             ████░░░░                            ####
#
# To run the code you must use the following command
#
# python3 main.py -f (filename) -ow (width of the output) -oh (height of the output)
#
# You can change the ASCII characters that the code uses by simply modifying the "characters" array, I've made a few presets
# This is a WIP Project (Version A01)

import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help = "Input Image Name")
parser.add_argument("-oh", "--height", help = "Change The Output Height")
parser.add_argument("-ow", "--width", help = "Change The Output Width")
args = parser.parse_args()

characters = ['█', '▓', '▒', '░', '#', ' ']
#characters = [' ', '#', '░', '▒', '▓', '█']
#characters = [" ", ",", "'", "`", '"', "~", "_", "!", "j", "|", r"\\", r"]", "g", "p", "e", "d", "0", r"#", "%", "&", "4", "Y", "7", "N", "M", "Q", "▒", "▓"]

image = cv2.resize(cv2.imread(args.filename, 0), (int(args.width), int(args.height)))

rows, cols = image.shape[0], image.shape[1]

output = open('output.txt', 'w')

print(rows, cols)

for i in range(rows):
	for j in range(cols):
		index = image[i, j]*len(characters)//256
		ch = characters[index]

		print(ch, end = '')
		output.write(4*ch)
	output.write('\n')
	print()
