import re
import csv
import os
import CustomTransformation

            #csv_input = pd.read_csv(FILENAME)
entries = os.listdir('Nulogy_Data/')
if not os.path.exists('Nulogy_Data/Transformed'):
    os.makedirs('Nulogy_Data/Transformed')
for entry in entries:
    plocation=entry.split('_')
    
    with open('Nulogy_Data/'+entry,'r',encoding="utf8") as csvinput:
        with open('Nulogy_Data/Transformed/'+'TRANS_'+entry, 'w',encoding="utf8") as csvoutput:
            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            #reader2 = csv.reader(csvinput)
            
            all = []
            row = next(reader)
            #result[]
            row.append('Plant Location')
            all.append(row)
            #print(reader[1])
            for row in reader:
                #print(row)
                if plocation[0]=='PTG':
                    row.append('MSI Portage')
                if plocation[0]=='NCT':
                    row.append('Newcomerstown')
                if plocation[0]=='WCG':
                    row.append('West Chicago')
                #all.append(row)
                row = [CustomTransformation.PercentageConversion(item) for item in row]
                all.append(row)
            writer.writerows(all)
        


    
            
           
            
            