start = 'hit'
end = 'cog'
chars =[]
for i in range(len(end)):
    chars.append(end[i])

print(chars)
a_dict =  ['hot', 'dot', 'dog', 'lot', 'log']

def find_path(start,end,paths):
    if start == end:
        return "start=end"
    else:
        visited=[]
        visited.append(start)
        for word in visited:
            print(word)
            for i in range(len(word)):
                a_word = word
                successed = False
                for j in range(ord('a'),ord('z')+1):
                    a_word = a_word[:i]+chr(j)+a_word[i+1:]
                    print(a_word)
                    if a_word == end:
                        print(end)
                        paths.append(a_word)
                        return
                    if a_word in paths and a_word not in visited:
                        successed = True
                        visited.append(a_word)
                        break
                if successed == True:
                    break
find_path(start,end,a_dict)
                        
                    
        
      
               
