# Read only

def read_only():
    '''a method that only reads the fill'''
    try:
        file1 = open('data.txt', 'r')  # read_only
        text = file1.read()
        print(text)
        file1.close()  # the reason for closing
    except FileNotFoundError:
        text = None
        print(text)


def write_only():
    '''A method that writes to a file'''
    # if file exists it will be overwritten
    # if file doesn't exist it will be created
    file2 = open('more_data.txt', 'w')
    file2.write('tomatoes')
    file2.close()


'''
# python will know to close this file
with open('data.txt') as f:
    txt = f.read()
    print(txt)
'''

'''

    all_categories = []
    all_products = []
    all_quantities = []
    all_unit_price = []
    all_total_price = []
'''


def read_food_sales():
    all_dates = []
    all_regions = []

    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            # food_sale ( each element in list)
            split_food_sale = food_sale.split(',')
            # print(split_food_sale)
            region = split_food_sale[1]
            # order_date = split_food_sale[0]
            # print(region)
            # append order_date to all dates list
            all_regions.append(region)
    print(region)

    with open('regions.txt', 'w') as f:
        for region in all_regions:
            f.write(region)
            f.write('\n')


def read_food_sales_cities():
    all_cities = []

    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            # food_sale ( each element in list)
            split_food_sale = food_sale.split(',')
            # print(split_food_sale)
            city = split_food_sale[2]
            # order_date = split_food_sale[0]
            # print(city)
            # append order_date to all dates list
            all_cities.append(city)
    print(city)

    with open('cities.txt', 'w') as f:
        for city in all_cities:
            f.write(city)
            f.write('\n')


def append_text():
    '''Append data to an existing file'''
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')


if __name__ == '__main__':
    # read_only()
    # write_only()
    read_food_sales()
    # read_food_sales_cities()
    # append_text()
