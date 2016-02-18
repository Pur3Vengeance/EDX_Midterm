#Accept list of integers, return integer from list that has most divisors.
#If tie: return first item with most divisors.
#Example: [8,12,18,6]. 12 and 18 have most divisors(6) - return 12 as is first.

def find_integer_with_most_divisors(input_list):

    while len(input_list)>0:
        
        calc_number = input_list.pop(0)
       
        divisors = []
        for x in range(1, calc_number+1):
            if calc_number%x==0:
                divisors.append(x)
        new_list = []
        new_list.append(divisors)
                   
        print(new_list)
        
        
        

find_integer_with_most_divisors([8, 12, 18, 6])
 
