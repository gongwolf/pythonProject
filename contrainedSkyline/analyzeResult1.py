import os


def analyzeByFileName(file_name):
    with open(file_name) as f:
            content = f.readlines()
    content = [x.strip() for x in content if not x.startswith("====")] 
    
    number=len(content)/2
    #print number
    counter=1
    
    
    op_base_time=0
    #op_base_visisted_bus_stops=0
    #op_base_final_bus_stops=0
    op_base_sk_counter=0
    
    base_5_time=0
    #base_5_visisted_bus_stops=0
    #base_5_final_bus_stops=0
    base_5_sk_counter=0
    
    
    for line in content:
        t_time=0
        t_visisted_bus_stops=0
        t_final_bus_stops=0
        t_sk_counter=0
    
        t_time=float(line.split("|")[1])
        #t_visisted_bus_stops=float(line.split(" ")[-4].split(",")[0])
        #t_final_bus_stops=float(line.split(" ")[-4].split(",")[1])
        #t_sk_counter=float(line.split(" ")[-1])
        
        if counter <= number:
            op_base_time+=t_time
            #op_base_visisted_bus_stops+=t_visisted_bus_stops
            #op_base_final_bus_stops+=t_final_bus_stops
            op_base_sk_counter += float(line.split(" ")[-1])
    
        else:
            base_5_time+=t_time
            #base_5_visisted_bus_stops+=t_visisted_bus_stops
            #base_5_final_bus_stops+=t_final_bus_stops
            base_5_sk_counter += float(line.split(" ")[-2])
    
        counter+=1
    
    
    
    op_base_time/=number
    #op_base_visisted_bus_stops/=number
    #op_base_final_bus_stops/=number
    op_base_sk_counter/=number
    
    base_5_time/=number
    #base_5_visisted_bus_stops/=number
    #base_5_final_bus_stops/=number
    base_5_sk_counter/=number
    
    #base_t_ratio = base_5_final_bus_stops/base_5_visisted_bus_stops
    time_speed_up = op_base_time/base_5_time
    sk_speed_up = base_5_sk_counter/op_base_sk_counter*100
    
    s="%.2f %.2f %.4f %d %d %.4f" % (base_5_time,op_base_time,time_speed_up,base_5_sk_counter,op_base_sk_counter,sk_speed_up)
    return s


path_base="/home/gqxwolf/shared_git/bConstrainSkyline/target/output/exp2/"
#path_base="/home/gqxwolf/shared_git/bConstrainSkyline/target/new_output/"


for file_name in os.listdir(path_base):
    fname = path_base+file_name
    graphsize = file_name.split("_")[0]
    degree = file_name.split("_")[1]
    hotels = file_name.split("_")[2]
    #if int(graphsize) in [1000,2000,4000,6000] :
    s=analyzeByFileName(fname)
    print "%s %s %s %s" % (graphsize,degree,hotels,s)
