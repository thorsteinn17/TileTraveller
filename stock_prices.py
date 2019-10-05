import statistics  
def get_data_list(file_name):
    data_list = [ ] # start with an empty list
    for line_str in file_name:
    # strip end-of-line, split on commas, and append items to
        data_list.append(line_str.strip().split(','))
    return data_list

def get_monthly_averages(data):
    averages = []
    top = []
    bottom = []
    for month in range(10,13):
        for line in data: 
            if '-'+str(month)+'-' in line[0]:
                adj = line[-2]
                vol = line[-1]
                top.append(float(adj)*float(vol))
                bottom.append(float(vol)) 
            else:
                continue
        averages.append(round(sum(top)/sum(bottom),2))
        top = []
        bottom = []    
    for month in range(1,10):
        for line in data: 
            if '-0'+str(month)+'-' in line[0]:
                adj = line[-2]
                vol = line[-1]
                top.append(float(adj)*float(vol))
                bottom.append(float(vol)) 
            else:
                continue
        averages.append(round(sum(top)/sum(bottom),2))
        top = []
        bottom = []    
    print(averages)
    return averages


def get_highest_price(data):
    adj = []
    highest = []
    for line in data[1:]: 
        adj = line[-2]
        highest.append(float(adj))
    max_value = max(highest)
    date_index = highest.index(max_value)
    date = data[date_index+1][0]
    adj_value = round(max_value,2)

    return date, adj_value



    
        
       
        
        

#def print_info():
"""
def main():
    try: 
        filename = input('Enter filename:')
        file_name = open(filename, 'r')
        data = get_data_list(file_name)
        get_monthly_averages(data)
        #print(data)
        #print(data[1][-2])
    except IOError:
        print('Filename',filename,'not found!')
"""
    

#main()

filename = open('GOOG.csv','r')
data = get_data_list(filename)
average_list = get_monthly_averages(data)
(highest_date,highest_adjvalue) = get_highest_price(data)

print(highest_date)
print(highest_adjvalue)