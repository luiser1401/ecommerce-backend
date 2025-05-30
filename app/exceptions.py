"""Custom exceptions for the ecommerce backend."""

class EcommerceBackendException(Exception):
    """Base exception for all ecommerce backend errors."""
    
    def __init__(self, message: str = "An error occurred in the ecommerce backend"):
        self.message = message
        super().__init__(self.message)
