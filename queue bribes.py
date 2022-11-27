def minimumBribes(q):
    # does not pass all test cases
    # print(q)
    bribes = 0
    chaosFlag = False
    for index in range(len(q)):        
        diff = (index - q[index])
        # print("index: ", index, " value: ", q[index], " diff: ", diff)
        
        if diff < 0:
            if abs(diff) > 3:
                print("Too chaotic")
                chaosFlag = True
                break  
            elif abs(diff) == 2:
                bribes += 1
            elif abs(diff) == 3:
                bribes += 2
      
            
    if chaosFlag == False:
        print(bribes)
