from realestate_com_au import RealestateComAu
from realestate_com_au.objects.listing import get_listing
from csv import writer
from ast import literal_eval
import pandas as pd

api = RealestateComAu()

# Get property listings
#listings = api.search(locations=["Burwood, VIC 3125"], channel="buy", keywords=["tenant"], exclude_keywords=["pool"])
listings = api.search(locations=["Melbourne"], channel="buy")


#df = pd.DataFrame(columns=['id','badge:','url','suburb','state','postcode','short_address','full_address','property_type','price','price_text','bedrooms','bathrooms','parking_spaces','building_size','building_size_unit','land_size','land_size_unit','listing_company_id','listing_company_name','listing_company_phone','auction_date','available_date','sold_date','description','images','images_floorplans','listers:','inspections'])

#new_row = pd.DataFrame.from_dict(listings[0].__dict__)


df_list = []
for index in range(len(listings)):    
    new_row = listings[index].__dict__
    df_list.append(new_row)
    #df = pd.concat([df,new_row])
    #df.append(new_row, ignore_index=True)

# Open a file in write mode.
with open('test.csv', 'w') as f:
    # Write all the dictionary keys in a file with commas separated.
    f.write(';'.join(df_list[0].keys()))
    f.write('\n') # Add a new line
    for row in df_list:
        # Write the values in a row.
        f.write(';'.join(str(x) for x in row.values()))
        f.write('\n') # Add a new line

