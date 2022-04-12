"""
Create a class ShoppingItem with the fields item code, description, price and discount. Note that item code and description are String where as price and discount are int. Create an object of the class ShoppingItem and print it.
"""

class shoppingItem:
  def __init__(self,item_code,description,price,discount):
    self.item_code = item_code
    self.description = description
    self.price = price
    self.discount = discount

  def __str__(self):
    return "Shopping Item: Code= {}, Description= {}, Price= {}, and Discount= {}".format(self.item_code,self.description,self.price,self.discount)

si = shoppingItem("R5DW34","Soap",100,5)
print(si)
