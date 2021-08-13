from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import data_preparation as data


def calculate_price_per_square_feet(resale_price, square_meter_area):
    convert_sm_to_sqft = 10.7639
    square_feet_area = np.round(square_meter_area * convert_sm_to_sqft)
    per_sqft = np.round(resale_price / square_feet_area, 2)
    return per_sqft


# Data Transformation
data.import_raw_data_to_mysql()


saved_data = np.genfromtxt("../data/clean_data.csv",
                           delimiter=",",
                           dtype=[('purchase_date', 'U10'),
                                  ('town', 'U30'),
                                  ('flat_type', 'U30'),
                                  ('floor_area_sqm', 'i4'),
                                  ('lease_commence_year', 'U10'),
                                  ('resale_price', 'i4'),
                                  ('region', 'U30')]
                           )
print("Data Count (Saved Data): {}".format(len(saved_data)))

saved_data['purchase_date'] = [datetime.strptime(date, '%Y-%m').year for date in saved_data['purchase_date']]
years = np.unique(saved_data['purchase_date'])
regions = np.unique(saved_data['region'])

data_price_by_region = []
for region in regions:
    data_by_region = []
    for year in years:
        filtered_data = saved_data[np.isin(saved_data['region'], [region]) &
                                   np.isin(saved_data['purchase_date'], [year])]

        has_elements = filtered_data.size > 0
        if has_elements:
            resale_price = filtered_data['resale_price']
            square_meter_area = filtered_data['floor_area_sqm']
            per_sqft = calculate_price_per_square_feet(resale_price, square_meter_area)
            data_by_region.append(int(per_sqft.mean()))
        else:
            data_by_region.append(0)

    data_price_by_region.append(data_by_region)

years = np.array([int(i) for i in years])
color = ['orange', 'green', 'red', 'purple', 'black']
plt.grid(axis='x', alpha=0.5)
plt.grid(axis='y', alpha=0.5)
plt.suptitle("HDB RESALE PRICE \n between Year {} to {}".format(years.min(), years.max()), fontsize=14, fontweight='bold')
plt.title("Average Resale Price per Square Feet (sqft) by Region")
plt.xlabel("Year")
plt.ylabel("Price per sqft (SGD)")
plt.xticks(np.arange(len(years)), years, rotation=45)
plt.yticks(np.arange(0, 700, 100))

count = 0
for i in data_price_by_region:
    plt.plot(i, label=regions[count], color=color[count])
    count += 1
legend = plt.legend(loc='upper left', shadow=True, title='Region')

plt.show()
