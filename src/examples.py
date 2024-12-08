def get_values():
    example_text = """INVOICE
    # 31061
    SuperStore
    Bill To:
    Yoseph Carroll
    Ship To:
    Manukau City,
    Auckland, New
    Zealand
    Nov 30 2012
    Standard Class
    $2,921.43
    Date:
    Ship Mode:
    Balance Due:
    Item
    Quantity
    Rate
    Amount
    Bevis Computer Table, Adjustable Height
    4
    $1,181.02
    $4,724.06
    Tables, Furniture, FUR-TA-3417
    $4,724.06
    $1,889.62
    $86.99
    $2,921.43
    Subtotal:
    Discount (40%):
    Shipping:
    Total:
    Notes:
    Thanks for your business!
    Terms:
    Order ID : ID-2012-YC2189592-41243
    """

    keys_to_extract = """{
        "Bill To":"",
        "Ship To": {
            "postal_code":"",
            "city":"",
            "state":"",
            "country":""
        },
        "Date":"",
        "Ship Mode":"",
        "Balance Due":"",
        "Item":{
            "product_name":"",
            "sub_category":"",
            "category":"",
            "product_id":""
        },
        "Quantity":"",
        "Rate": "",
        "Amount": "",
        "Subtotal": "",
        "Discount": {
            "discount_%":"",
            "discount_amount":""
        },
        "Shipping":"",
        "Total": "",
        "Order ID":""
    }"""

    example_json = """{
        "Bill To": "Yoseph Carroll",
        "Ship To": {
            "postal_code": "",
            "city": "Manukau City",
            "state": "Auckland",
            "country": "New Zealand"
        },
        "Date": "Nov 30 2012",
        "Ship Mode": "Standard Class",
        "Balance Due": "$2,921.43",
        "Item": {
            "product_name": "Bevis Computer Table, Adjustable Height",
            "sub_category": "Tables",
            "category": "Furniture",
            "product_id": "FUR-TA-3417"
        },
        "Quantity": "4",
        "Rate": "$1,181.02",
        "Amount": "$4,724.06",
        "Subtotal": "$4,724.06",
        "Discount": {
            "discount_%": "40%",
            "discount_amount": "$1,889.62"
        },
        "Shipping": "$86.99",
        "Total": "$2,921.43",
        "Order ID": "ID-2012-YC2189592-41243"
    }"""

    return keys_to_extract, example_text, example_json