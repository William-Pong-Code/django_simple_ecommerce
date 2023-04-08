from .basket import Basket


def basket(request):
    '''
    Can be used in all templates
    '''
    return {'basket': Basket(request)}