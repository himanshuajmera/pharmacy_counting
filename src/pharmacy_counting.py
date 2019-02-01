#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    #get required packages
    from operator import itemgetter,attrgetter
    
    #read file
    infile = open("./input/itconr.txt", encoding = 'utf8').read()
    data = infile.split('\n')[1:]
    
    #create output file in .txt
    outfile = open("./output/top_cost_drug.txt","w")
    
    
    #create lists of input data 
    drug_names=[]
    temp_data=[]
    for i in data:
        row=i.split(',')[1:]
        temp_data.append(row)       #list of temporary data
        drug_name=i.split(',')[3]
        drug_names.append(drug_name)
    drug_names=set(drug_names)      #list of unique drug_names
    
    #compare data with unique drug list and store in a list
    temp=[]
    for d in drug_names:
        drug_temp=[]
        for n in row:
            if d in n:
                drug_temp.append(n)
        drug=[]
        cost=[]
        for z in drug_temp:
            drug.append(str(z))
            ind_cost = z[-1].replace('""','')
            cost.append(float(ind_cost))
        f_row=str(d),len(list(set(drug))),sum(cost)
        temp.append(f_row)
    
    #create output list with header
    output=sorted(temp, key=itemgetter(2), reverse=True)
    output.insert(0,"drug_name,num_prescriber,total_cost")
    
    #writing the output file as txt
    for listitem in output:
        f_row=str(listitem).replace("(",'').replace(")",'')
        outfile.write('%s\n' % f_row)
    
    #close the output file
    outfile.close()
    
    


# In[ ]:


#creating main function
if __name__ == '__main__':
    main()

