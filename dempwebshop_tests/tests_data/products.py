from dataclasses import dataclass


@dataclass
class Product:
    number: int
    payload: dict[str, int | str]
    price: int


product_31 = Product(
    number=31,
    payload={'addtocart_31.EnteredQuantity': 1},
    price=1590
)

product_72 = Product(
    number=72,
    payload={'product_attribute_72_5_18': 53,
             'product_attribute_72_6_19': 54,
             'product_attribute_72_3_20': 57,
             'addtocart_72.EnteredQuantity': 1},
    price=815
)

product_4 = Product(
    number=4,
    payload={'giftcard_4.RecipientName': 'HisName',
             'giftcard_4.SenderName': 'Myname Mysurname',
             'giftcard_4.Message': 'Happy Birthday!',
             'addtocart_4.EnteredQuantity': 1},
    price=100
)

product_28 = Product(
    number=28,
    payload={'product_attribute_28_7_10': 25,
             'product_attribute_28_1_11': 29,
             'addtocart_28.EnteredQuantity': 1},
    price=11
)