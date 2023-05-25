from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        ref = defaultdict(set)
        
        #Using set for faster lookup
        words = set(wordList)
        
        #Insert characters based on their indexes
        for word in wordList:
            for idx, letter in enumerate(word):
                ref[idx].add(letter)
        
        #For BFS traversal starting from level 1
        queue = deque()
        queue.append((beginWord, 1))
        
        #Record all visiting words from beingWord
        seen = set()
        seen.add(beginWord)
        
        while queue:
            
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            #Making new string by replacing each indexes char 
            # with available char for that index from ref
            for i in range(len(word)):
                for char in ref[i]:
                    
                    #hit -> *it -> [cit, lit, dit] 
                    newWord = word[:i] + char + word[(i+1):]
                    
                    if newWord in words and newWord not in seen:
                        queue.append((newWord, (level+1)))
                        seen.add(newWord)
        return 0

test_cases = {
    'test_case_1': {
        'description': 'cycle test',
        'input': {
            'wordList': ["hot", "dot", "dog", "lot", "log", "cog"],
            'beginWord': 'hit',
            'endWord': 'cog'
        },
        'output': 5,
        'active': True
    },
    'test_case_2': {
        'description': 'cycle test',
        'input': {
            'wordList': ["hot", "dot", "dog", "lot", "log"],
            'beginWord': 'hit',
            'endWord': 'cog'
        },
        'output': 0,
        'active': True
    },
    'test_case_3': {
        'description': 'cycle test',
        'input': {
            'wordList': ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"],
            'beginWord': 'cet',
            'endWord': 'ism'
        },
        'output': 11,
        'active': True
    }
}

for test_name, data in test_cases.items():

    print('Running -> {} -> {}'.format(test_name, data['description']))

    if data['active'] == False:
        print('Skipped!')
        continue

    input = data['input']
    result = Solution().ladderLength(
        input['beginWord'], input['endWord'], input['wordList'])
    if result == data['output']:
        print('Test passed!')
    else:
        print('Test fail')
        print('Expected Output: ', end="")
        print(data['output'])
        print('Actual Output: ', end="")
        print(result)
    print()
