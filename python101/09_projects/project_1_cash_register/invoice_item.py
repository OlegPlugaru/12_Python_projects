from item import Item

class InvoiceItem:
    """Line Item for cash register with purchase quantity & discount"""

    def __init__(self, item: Item,  quantity: int, discount: float = 0) -> None:
        self.item = item
        self.discount = discount
        self.quantity = quantity
        # Private Member
        self._sub_total = (item.price * quantity) - discount

    def __repr__(self) -> str:
        return "<class 'InvoiceItem'>"
    
    def __str__(self) -> str:
        return (
            f"Item: {self.item.name}, Quantity: {self.quantity}, Discount: {self.discount}, " 
            f"Sub Total: {self.get_sub_total():.2f}"
        )
    
    def get_sub_total(self) -> float:
        """Returns the sub-total"""
        return self._sub_total