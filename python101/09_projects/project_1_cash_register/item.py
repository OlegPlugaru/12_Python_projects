class Item:
    """Simple Item for cash register"""
    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit # E.g -> Kg or ml

    def __repr__(self) -> str:
        return "<class 'Item'>"
    
    def __str__(self) -> str:
        return f"{self.name}: ${self.price}/{self.measurement_unit}"