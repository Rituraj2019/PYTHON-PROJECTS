import pyshorteners  #importing the necessary module

print("Welcome to URL Shortner, You will get URL in 2 steps :) ") #Welcome message
url=input("Please enter the original url: ")  #User input for orginal url

shorturl=pyshorteners.Shortener().tinyurl.short(url)  #using the imported module and Shortner().tinyurl.short()
                                                    #method, we will shorten the url
print() #changing the line for result
print("Your shortened url is: ", shorturl) #printing the shortened url