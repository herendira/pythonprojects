#Python Remove hyphen from string

myStr = "123-456-789"

# printing original string
print("The original string is : " + myStr)

# Remove hyphen from string
result = myStr.replace('-','')

# printing result
print ("String hyphen remove after : " + str(result))