def buy(shopping_bag):
    print('[구입]')
    while True:
        item = input('상품명? ')
        if item == '':
            break
        qty = int(input('수량은? '))
        shopping_bag[item] = qty
        print(f'장바구니에 {item} {qty}개가 담겼습니다.')

def show(shopping_bag):
    print(f'\n>>> 장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    print('[검색]')
    while True:
        search_item = input('장바구니에서 확인하고자 하는 상품은? ')
        if search_item == '':
            break
        qty = shopping_bag.get(search_item)
        if qty is not None:
            print(f'{search_item}(는) {qty}개 담겨 있습니다.')
        else:
            print(f'장바구니에 {search_item}은(는) 없습니다.')

# 주 프로그램
shopping_bag = {}
buy(shopping_bag)
show(shopping_bag)
find(shopping_bag)