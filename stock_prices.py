

def get_data_list(file_name): # data list function sorts the data from the input file into a list 
    data_list = [ ] # start with an empty list
    for line_str in file_name:
    # strip end-of-line, split on commas, and append items to
        data_list.append(line_str.strip().split(','))
    return data_list


def get_monthly_averages(data): # function that calculates the average for each month in the data list
    starting_year = data[1][0][:4] 
    ending_year = data[-1][0][:4]
    years = int(ending_year) - int(starting_year)
    averages = []
    for i in range(1,years+1): # use starting year and end year to run a for loop that goes over every year in the list
        # The equation for average is ((adj_1*vol_1+...+adj_n*vol_n)/(vol_1+...+vol_n))
        top = [] # empty list that i will use to append all values from the numerator in the average equation
        bottom = [] # empty list that i will use to append all values from the denominator in the average equation
        if starting_year < ending_year:
            for month in range(10,13): # for loop that iterates over the months numbered 10-12
                for line in data: 
                    if starting_year+'-'+str(month)+'-' in line[0]: # use starting year and month to seperate the data into different months and years
                        adj = line[-2] # the value of adj in the data list
                        vol = line[-1] # the value of volume in the data list 
                        top.append(float(adj)*float(vol)) # add these values as floats into the top list
                        bottom.append(float(vol))  # add these values as floats to the bottom list
                    else:
                        continue    
                a = sum(top)/sum(bottom) # sum up the values from the top and bottom lists which gives us the average
                averages.append('%.2f' %a) # append those values to the list containing average values with only 2 decimal points
                top = [] # reset the top list so that the values will be correctly calculated in the next loop
                bottom = [] # do the samt thing for the bottom list
            starting_year = int(starting_year)+1 # increase the value of starting year by one so the loop calculating averages calculates the numbers for the next year
            starting_year = str(starting_year)
        if starting_year <= ending_year: 
            for month in range(1,10): # for loop that iterates over all the months numbered 1 to 9
                for line in data: 
                    if starting_year+'-0'+str(month)+'-' in line[0]: #use starting year and month to seperate the data into different months and years
                        adj = line[-2]
                        vol = line[-1]
                        top.append(float(adj)*float(vol)) # add these values as floats into the top list
                        bottom.append(float(vol)) # add these values as floats into the bottom list
                    else:                    
                        continue     
                a = sum(top)/sum(bottom) # sum the lists into one value
                averages.append('%.2f' %a) #append to averages list with only 2 decimal points
                top = [] #reset top list again
                bottom = [] #reset bottom list again   
    return averages


def get_highest_price(data): # function that calculates the highest price on any given date within the data list.
    adj = [] # empty list used for appending all values in the adj column
    highest = []
    for line in data[1:]: 
        adj = line[-2] #append all values into previously empty list, creating a list containing only adj values
        highest.append(float(adj)) # append as floats
    max_value = max(highest) # use local function to find the highest values
    date_index = highest.index(max_value) # return the index of the location
    date = data[date_index+1][0]  # find the date asosiated with location index
    adj_value = round(max_value,2)

    return date, adj_value # return both values, date and highest value


def get_list_of_months(data): #creates a list containing all months in the input file
    months = []
    for line in data[1:]:
        months.append(line[0][:7]) # take a slice of all the dates 
    months = list(dict.fromkeys(months)) # remove all duplicated values
    return months #returns a list with all the months
    

def print_info(average_list,months,highest_date,highest_adjvalue): # function that prints all the data into two formated columns, along with the highest price and its date  
    average_list.insert(0,'Price')
    months.insert(0,'Month')
    fmt = '{:<10}{:>7}' # format the line spacing and alignment of the two colums
    for item, (months, average_list) in enumerate(zip(months, average_list)): 
        print(fmt.format(months, average_list)) #print both formated columns
    print('Highest price',highest_adjvalue,'on day',highest_date)


def main(): #main function that calls all the other functions and checks if the input file exists
    try: 
        file_name = input('Enter filename: ')
        filename = open(file_name, 'r')
    except IOError:
        print('Filename',file_name,'not found!')
    data = get_data_list(filename)
    average_list = get_monthly_averages(data)
    (highest_date,highest_adjvalue) = get_highest_price(data)
    months = get_list_of_months(data)
    print_info(average_list,months,highest_date,highest_adjvalue)

    
main()

