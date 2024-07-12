    # public static int maxCost(List<Integer> cost, List<String> labels, int dailyCount) {
    #     int count = 0;
    #     int Maxnum = 0;
    #     int maxcost=0;
    #     for(int i = 0; i < labels.size(); i++){
    #         Maxnum += cost.get(i); 
    #         if(labels.get(i).equals("legal") && count != dailyCount){
    #             count += 1;
    #         }
    #         if(count == dailyCount){
    #             if(maxcost < Maxnum){
    #                 maxcost = Maxnum ;
    #             }
    #             Maxnum = 0;
    #             count = 0;
    #         }
    #     }
    #     return maxcost;
        
        

    # }
    

def find_sub(a, b):
    count = 0;
    new_count = 0;
    s=""
    c=''
    res=0
    vowels=['a','e','i','o','u']
    for i in range(len(a)):
        new_count += 1
        if a[i] in vowels:
            count+=1
        if new_count == b:
            c = a[i-b+1]
            if res < count:
                res = count
                s = a[i-b+1: i+1]
            if c in vowels:
                count-=1
            new_count -= 1
    return (s, res)
    