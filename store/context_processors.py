from .models import Category


def categories(request):
    '''
    Can be used in all templates
    '''
    return {
        'categories': Category.objects.all()
    }