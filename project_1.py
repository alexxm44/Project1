"""
*Structured English*
Create a program that reads a list of the phone numbers below and formats
each number with parentheses and a hyphen.
Basic 10-digit phone number, add ().
If it is a 11-digit phone number, add +1 ().
Example:
Phone numbers input:
10-digit:
1198628896
5556786777
5597872056
..
...
11-digit:
11198628896
..
...
Phone number output goal:
10-digit:
(119)862-2886
(555)678-6777
(559)787-2055
11-digit:
+1(119)862-8896
..
...
"""

"""
# basic 10-digit phone number formatting    
def phone_format(num):
       num = remove white space from line    
   new_num = (xxx)xxx-xxxx
       return new_num
      
# if the supplied phone number is 11 digits add the country code +x    
def long_phone_format(num):
       num = remove white space from line    
   new_num = +x(xxx)xxx-xxxx
       return new_sum
     
# format data given in a .txt file    
def format_from_file():
      
    
   Open output file for writing:
           Iterate through lines:
               string = convert line (int) to string    
           if the number has 10 digits:
                   Use short format and print to file    
           If number has 11 digits:
                   Use long format and print to file
               else:
                   Tell the user the formatting is incorrect
     
# format data provided by the user    
def format_from_user():
     
   Iterate through numbers list:
               string = convert user input to string    
           if string has 10 digits:
                   Format and write short formatting    
           If string has 11 digits:
                   Format and write long format
               else:
                   Tell user the formatting is incorrect    
# Kickstart the program    
def main():
           Give instructions to user
       User chooses how to input the numbers
     
   if choice == read
           format_from_file()
     
    
   if choice == input:
           format_from_user()
     
Run main function 
"""