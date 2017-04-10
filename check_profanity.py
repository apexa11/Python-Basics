import urllib

def read_file():
   quotes = open("/Users/apexa/Desktop/Python Basic/movie_quotes.txt")
   content_file = quotes.read()
   print(content_file)
   quotes.close()
   check_profanity(content_file)

def check_profanity(check_text):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+check_text)
    output = connection.read()
    print(output)
    connection.close()
    
read_file()
