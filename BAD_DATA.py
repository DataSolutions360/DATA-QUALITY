import pandas as pd
import re
import pandas_profiling
# Function to remove non-alphanumeric characters from a string
def remove_special_characters(text):
    return re.sub(r'\W', '', str(text)) #Convert to string before applying regex

#Function to remove all digits(numbers) from the text
#def remove_digits(text):
#    return re.sub(r'\d', '', str(text)) 

#Function to remove whitespace characters(spaces, tabs, newlines) from the text
#def remove_whitespace(text):
#    return re.sub(r'\s', '', str(text))

#Function removes a specific phrase
#def remove_specific_phrase(text):
#    return re.sub(r'specific_phrase', '', str(text))

#LAMBDA FUNCTIONS!!!!   Remove Specific Words or Phrases, such as "apple"
#######     df['column_name'] = df['column_name'].apply(lambda x: re.sub(r'apple', '', x))  ###########

# LAMBDA FUNCTION!!!!   Remove all EMAIL ADDRESS with "REDACTED"
####### df['column_name'] = df['column_name'].apply(lambda x: re.sub(r'\S+@\S+', 'REDACTED', x)) ######

df = pd.read_excel('BAD_DATA.xlsx')  #If the first column is NOT part of the columns to be factored in, add ", index_col=0"!!! 
print(df.head(6))

print(df.dtypes)

# run the profile report
profile = df.profile_report(title='Pandas Profiling Report')

# save the report as html file
profile.to_file(output_file="pandas_profiling1.html")

# save the report as json file
profile.to_file(output_file="pandas_profiling2.json")

#Specify which columns to clean
columns_to_clean = ['SYMBOL','AMOUNT','PRICE']
for column in columns_to_clean:
    if df[column].dtype == 'object':    # Check if the column contains string data
        df[column]=df[column].apply(remove_special_characters)

#If you want to apply for ALL COLUMNS:
#for column in df.columns:
 #   if df[column].dtype == 'object':  # Check if the column contains string data
 #       df[column] = df[column].apply(remove_special_characters)  

#Covert specific columns back to numeric:
columns_to_convert_to_numeric = ['PRICE'] 
for column in columns_to_convert_to_numeric:
    df[column] = pd.to_numeric(df[column], errors='coerce') # 'coerce' converts non-numeric values to NaN
    #POSSIBLE OPTIONS FOR ERROR TREATMENT:   1) IGNORE - IGNORES UNCONVERTIBLE VALUE AND LEAVES THEN AS THE ARE IN RESULTING SERIES
    #2) COERCE - CONVERTS UNCONVERTIBLE VALUES to NaN(Not a Number)...3) RAISE - WILL RAISE AN ERRO IF IT ENCOUNTERS ANY UNCONVERTIBLE VALUES

print(df.dtypes)

print(df.head(6))

df2=df.to_excel('GOOD_DATA.xlsx')

print(df2.dtypes)

print(df2)

