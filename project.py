import sys
import csv

def main():
    check_correct_args()
    try:
        data = []
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                    data.append(row)
    except FileNotFoundError:
        sys.exit('Unreadable CSV file')

    output = []
    for row in data:
        colour = select_colour(row['year'])
        expected_mileage = select_mileage_from_price(row['price'])
        output.append({
            'name': row['name'],
            'year': row['year'],
            'price': row['price'],
            'colour': colour,
            'expected_mileage': expected_mileage
        })
    print(output)

    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'colour', 'expected_mileage'])
        writer.writerow({'name': 'name', 'colour': 'colour', 'expected_mileage': 'expected_mileage'})
        for row in output:
            writer.writerow({'name': row['name'],'colour': row['colour'],'expected_mileage': row['expected_mileage']})



def check_correct_args():
    if len(sys.argv )< 3:
        sys.exit('Add more command-line arguments')
    if len(sys.argv )> 3:
        sys.exit('Remove some command-line arguments')
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('Should be a CSV file')




def select_colour(years):
    year = int(years)
    if year in [2016, 2017]:
        return ('White' )
    elif year in [2018, 2019]:
        return ('Pearl_white')
    else:
        return('None')


def select_mileage_from_price(price_str):
    try:
        price = float(price_str.replace('M', ''))
    except ValueError:
        return 'Unknown'

    if price > 2.0:
        return 'Below 50,000 km'
    else:
        return 'Above 50,000 km'


if __name__ == "__main__":
    main()
