#define frame() function
def frame(*words):
  
   size = max(len(word) for word in words)
   print('*' * (size + 4))
   for word in words:
        print('* {:<{}} *'.format(word, size))
   print('*' * (size + 4))

   
frame("Write","good","code","every","day")
