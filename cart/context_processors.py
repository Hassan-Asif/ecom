from .cart import Cart

# Create Context processor so our cart can work on all pages
def cart(request):
    # Return the defual data from our Cart
    return{'cart': Cart(request)}