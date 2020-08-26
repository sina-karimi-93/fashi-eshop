from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product, ProductGallery, Comment
from eshop_products_categories.models import ProductCategory
from eshop_tag.models import Tag
from .forms import CommentForm
from django.contrib.auth.models import User
from cart.forms import CartAddProductForm

# Create your views here.

# ====================================== List ======================================


class ProductList(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


# ====================================== Detail ======================================
def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    product = Product.objects.get_product_by_id(selected_product_id)

    if product is None:
        raise Http404('Selected Product not found...')

    # get product categories
    product_category = product.categories.all()

    # get product galleries
    galleries = ProductGallery.objects.filter(product_id=selected_product_id)

    # get product tags
    tags = Tag.objects.filter(
        product__tag__product=selected_product_id).distinct()

    # get comments
    user = request.user
    comments = Comment.objects.filter(product=product).order_by('-id')
    new_comment = None
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.cleaned_data.get('body')
            new_comment = Comment.objects.create(
                product=product, user=user, body=comment)
            new_comment.save()

        else:
            comment_form = CommentForm()
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'product_category': product_category,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'galleries': galleries,
        'tags': tags,
        'cart_product_form': cart_product_form,
    }
    # Delete Comment
    delete_comment = request.GET.dict()
    if delete_comment is not None:
        for key in delete_comment.keys():
            if key is not None:
                print(f'key = {key}')
                delete_comment_id = key
                comments.get(id=delete_comment_id).delete()
                return redirect(f'/products/{selected_product_id}/{product}')

    return render(request, 'products/product_detail.html', context)


# ====================================== Search ======================================
class SearchProductsView(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()


# ====================================== Category ======================================
class ProductListByCategory(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(
            url__iexact=category_name).first()
        if category is None:
            raise Http404('Page Not Found...')
        return Product.objects.get_products_by_category(category_name)


# ====================================== Category Partial ======================================
def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)


# ====================================== Tag Partial ======================================
def products_tag_partial(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'products/products_tag_partial.html', context)
