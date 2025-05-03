#9-4
# 딕셔너리를 사용하여 수량을 저장
# 장바구니 내 상품을 검색하여 해당 상품의 수량 출력

shopping_bag = {}

while True:
    item = input('상품명? : ')
    if item == '':
        break
    qty = int(input('수량은? : '))
    shopping_bag[item] = qty
    print(f'장바구니에 {item} {qty}개가 담겼습니다.')

print(f'\n>>> 장바구니 보기 : {shopping_bag}')

print('[검색]')
search_item = input('\n장바구니에서 확인하고자 하는 상품은? : ')
qty = shopping_bag.get(search_item)
if qty is not None:
    print(f'{search_item}는(은) {qty}개 담겨있습니다.')
else:
    print(f'{search_item}는(은) 장바구니에 없습니다.')