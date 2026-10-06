from pprint import pprint

products = {}
products['id'] = [101,102,103]
products['names'] = ['pA', 'pB', 'pC']
products['cost'] = [1550, 2500, 1250]
products['qty'] = [10, 50, 100]

pprint(products)

print("\n")

products = []
products.append({
    'id': 101,
    'name': 'pA',
    'cost': 1550,
    'qty': 10
})
products.append({
    'id': 102,
    'name': 'pB',
    'cost': 2500,
    'qty': 50
})
products.append({
    'id': 103,
    'name': 'pC',
    'cost': 1250,
    'qty': 100
})
pprint(products)

print("\n") 
products = {} # dict of dict
products['id'] = {'id1':101,'id2':102,'id3':103}
products['names'] = {'name1':'pA','name2':'pB','name3':'pC'}
products['cost'] = {'cost1':1000,'cost2':2000,'cost3':3000}
products['Qty'] = {'Qty1':10,'Qty2':20,'Qty3':30}
pprint(products)
