def asciiToSentence(string, length) : 
	
	num = 0; 
	for i in range(length) : 

		# Append the current digit 
		num = num * 10 + (ord(string[i]) -
						ord('0')); 

		# If num is within the required range 
		if (num >= 32 and num <= 127) : 

			# Convert num to char 
			ch = chr(num); 
			print(ch, end = ""); 

			# Reset num to 0 
			num = 0; 

# Driver code 
if __name__ == "__main__" : 
	string = "7010897103324532123686411611595109894511551991145084953395871241081089511011111695116511081089585125"; 
	length = len(string); 
	
	asciiToSentence(string, length); 
