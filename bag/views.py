from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


""" We submit the form to this view including
the product id and the quantity """


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    """ Once in the view we grab the bag variable if it exists in the session
    or create it if it  does not """
    bag = request.session.get('bag', {})

    """ Then, we add the item to the bag or update the
    quantity if it already exists """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
