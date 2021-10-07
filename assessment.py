# —————————————————Function to load in data from file————————————————————————————
def load_data(path):
    
    f = open(path, 'r')
    products_list = f.readlines()
    f.close()

    return products_list

# ——————————Function to get separated single lines from file————————————————————————————
# ———————————Will display as ['#', 'Name', 'Price', 'Count']————————————————————————————
def get_data(array, index):
    
    stripped_product_str = array[index].strip()
    split_product_str = stripped_product_str.split(',')
    
    return split_product_str

# —————————Function to search for string(input) in file lines————————————————————————————
# ——————————————Will iterate over all lines in file————————————————————————————
def search(string):
    
    index = 0
    products_list = load_data('products.txt')
    products_not_found = True
    while index < len(products_list):
        product = get_data(products_list, index)
        
        if string in product[1]:
            print("Name: ", product[1])
            print("Price: ", product[2])
            print("Count: ", product[3])
            print("Total: ", float(product[2]) * float(product[3]))
            products_not_found = False
        
        index += 1
    
    if products_not_found == True:
        print('Error: product not found')


# ———————————————Function that controls search again————————————————————————————
def shopping():
    is_shopping = True

    while is_shopping == True:
        string = input('What are you looking for today? > ')
        search(string.capitalize())
        search_again = input('Search again? (Yes/No) > ')

        if search_again.capitalize() == 'No':
            is_shopping = False

    return 'Thank you for shopping!'
            
            

    







# ———————————————————————Testing Code————————————————————————————
# test = load_data('products.txt')
# print(test)

# array = load_data('products.txt')
# test2 = get_data(array, 0)
# print(test2)

# print(len(array))

# string = input('What are you looking for today? > ')
# test3 = search(string.capitalize())
# print(test3)

# ———————————————————————Running Code————————————————————————————
test4 = shopping()
print(test4)

