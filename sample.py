from aligncommerce import api

username 	= 'pinky@aligncommerce.com'
password	= 'password123'
client_id  	= '0d3067df52169d5f071c810e843eeebd'
secret_key 	= '8649d5f86727401bfd321a05e1d19e45'

api = api.Api( username, password, client_id, secret_key )

""" BUYER """
# print api.buyerList()
# print api.buyerInfo('564')

""" INVOICE """
create_invoice_data = {
	'currency' : 'sgd',
	'checkout_type' : 'btc',
	'products' : [{
		'product_name' 		: 'Test Product 1',
		'product_price' 	: '1',
		'quantity' 			: '1',
		'product_shipping' 	: '1'
	}],
	'buyer_info'	: {
		'first_name' : 'Testbuyer1',
		'last_name'  : 'Testbuyer1',
		'email'		 : 'mail@mail.com',
		'address_1'  : 'Testbuyer1',
		'address_2'  : 'Testbuyer1'
	}
}
# print api.invoiceList()
# print api.invoiceInfo('pFNvrjccQDj2ZCIsTGb2')
# print api.invoiceCreate(create_invoice_data)

""" PRODUCTS """
create_product_data = {
	'product_name' 			: 'Test Product Name1',
	'product_description'	: 'Test Product Name1',
	'product_price' 		: 20,
	'product_shipping' 		: 10
}
# print api.productList()
# print api.productInfo('VtLwEftNWW94heKZGkbL')
# print api.productCreate(create_product_data)

