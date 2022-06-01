
from googlesearch import search  #import module
print("Hello, Welcome to my search engine, have a good time") #welcome message
query=input("What do you wish to search? : ") #take query as an input from user
result=search(query, tld="co.in",lang='en',start=0, stop=5) #use deifferent inputs and arguments
                                                                    # for more functions

for i in result: #the availaible links can be accessed from results using i

    print(i)



