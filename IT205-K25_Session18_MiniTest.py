products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]


def find_by_id(products_list, id):
    for product in products_list:
        if product["id"] == id:
            return product
    return None


def show_products(products_list):
    if len(products_list) == 0:
        print('Cửa hàng hiện chưa có sản phẩm nào!')
    else:
        print('\n--- DANH SÁCH SẢN PHẨM ---')
        print(f'ID{"":<6} | Tên sản phẩm{"":<3} | Giá bán {"":<10}')
        print('-' * 40)
        for product in products_list:
            print(f'{product['id']:<8} | {product['name']:<15} | {product['price']:<10}')
        print('-' * 40)
    
    
def add_product(products_list):
    print('\n--- THÊM SẢN PHẨM MỚI ---')
    while True:
        id = input('Nhập mã sản phẩm (ID): ').strip().upper()
                
        if id == "":
            print('Mã sản phẩm không được để trống')
        elif find_by_id(products_list, id):
            print(f"Mã sản phẩm {id} đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break
        
    while True:
        name = input('Nhập tên sản phẩm: ').strip().capitalize()
                
        if name == "":
            print('Tên sản phẩm không được để trống')
        else:
            break
        
    while True:
        price = input('Nhập giá bán: ').strip()
                
        if price == "":
            print('Giá bán không được để trống')
        elif not price.isdigit():
            print('Giá bán phải là số nguyên lớn hơn 0')
        else:
            break
        
    new_product = {'id': id, 'name': name, 'price': price}
    
    products_list.append(new_product)
    
    print('\nThêm sản phẩm thành công!')
    

def update_price(products_list):
    if len(products_list) == 0:
        print('Cửa hàng hiện chưa có sản phẩm nào!')
    else:
        print('\n--- CẬP NHẬP GIÁ SẢN PHẨM ---')
        while True:
            id = input('Nhập mã sản phẩm cần sửa giá: ').strip().upper()
                    
            if id == "":
                print('Mã sản phẩm không được để trống')
            else:
                break
            
        product = find_by_id(products_list, id)
        if not product:
            print(f"Không tìm thấy sản phẩm mang mã {id}!")
            return
        

        print(f'Tìm thấy sản phẩm {product["name"]} (Giá hiện tại: {product["price"]})')
        while True:
            price = input('Nhập giá mới: ').strip()
                            
            if price == "":
                print('Giá bán không được để trống')
            elif not price.isdigit():
                print('Giá bán phải là số nguyên lớn hơn 0')
            else:
                break
                    
        product["price"] = price
                
        print('\nCập nhập giá thành công')
                    

def main():
    while True:
        print('=' * 40)
        print('     QUẢN LÝ CỬA HÀNG - MINI STORE     ')
        print('=' * 40)
        print('1. Xem danh sách sản phẩm hiện có')
        print('2. Thêm mới một sản phẩm')
        print('3. Cập nhật giá sản phẩm theo ID')
        print('4. Thoát chương trình')
        print('=' * 40)
        
        choice = input('Nhập lựa chọn: ').strip()
        
        if choice == '1':
            show_products(products)
        
        elif choice == '2':
            add_product(products)
            
        elif choice == '3':
            update_price(products)
            
        elif choice == '4':
            print('Cảm ơn bạn đã sử dụng chương trình!')
            break
        
        else:
            print('Lựa chọn không hợp lệ. Vui lòng thử lại.')
            
if __name__ == '__main__':
    main()