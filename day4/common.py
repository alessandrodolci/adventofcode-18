import time

def order_input(source_file_name, dest_file_name):
    input_file = open(source_file_name, "r")
    output_file = open(dest_file_name, "w")
    dates = []
    # Dictionary to store references between timestamps and lines (could be improved)
    date_lines = {}
    for line in input_file:
        tokens = line.split()
        date_string = (tokens[0] + ' ' + tokens[1])[1:len(tokens[0])+len(tokens[1])]
        dates.append(time.strptime(date_string, "%Y-%m-%d %H:%M"))
        date_lines[date_string] = line
    
    dates.sort()
    for date in dates:
        date = time.strftime("%Y-%m-%d %H:%M", date)
        output_file.write("%s" %date_lines[date])
    return
