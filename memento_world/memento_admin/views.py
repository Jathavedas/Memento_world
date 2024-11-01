from django.shortcuts import render,redirect,get_object_or_404
from .forms import ItemsForm
from .models import Items,Type
from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.



def loginview(request):
    if request.method == 'POST':
        usname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=usname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('memento_admin:add')  # Ensure this matches your URL pattern
        else:
            return render(request, "login.html", {"msg": "Invalid details"})
    else:  # Handle GET requests
        return redirect('memento_admin:logout')  # Render login form for GET requests

    
@login_required
def logout_(request):
    logout(request)
    return redirect('memento_user:home')


#add.html
@login_required
def add(request):
    return render(request,"adminadd.html")

@login_required
def upload_item(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('memento_admin:add')  # Redirect to the items list after successful upload
    else:
        form = ItemsForm()
    return render(request, 'adminadd.html', {'form': form})


@login_required
def memento_list(request):
    # Get the search query and sort option from the POST request
    search_query = request.POST.get('search', '')
    sort_by = request.POST.get('sort', 'price_asc')

    # Fetch all items initially
    memento_type = get_object_or_404(Type, type='memento')
    items = Items.objects.filter(type=memento_type)

    # Filter items based on the search query
    if search_query:
        items = items.filter(name__icontains=search_query)

    # Sort items based on the selected option
    if sort_by == 'price_asc':
        items = items.order_by('price')
    elif sort_by == 'price_desc':
        items = items.order_by('-price')
    elif sort_by == 'stock_asc':
        items = items.order_by('stock')
    elif sort_by == 'stock_desc':
        items = items.order_by('-stock')

    # # Render the response with the filtered and sorted items
    context = {
        'items': items,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'admin_memento.html', context)

 


#view memento
@login_required
def trophy_list(request):
   
    # Get the search query and sort option from the POST request
    search_query = request.POST.get('search', '')
    sort_by = request.POST.get('sort', 'price_asc')

    # Fetch all items initially
    trophy_type = get_object_or_404(Type, type='trophy')
    items = Items.objects.filter(type=trophy_type)

    # Filter items based on the search query
    if search_query:
        items = items.filter(name__icontains=search_query)

    # Sort items based on the selected option
    if sort_by == 'price_asc':
        items = items.order_by('price')
    elif sort_by == 'price_desc':
        items = items.order_by('-price')
    elif sort_by == 'stock_asc':
        items = items.order_by('stock')
    elif sort_by == 'stock_desc':
        items = items.order_by('-stock')

    # # Render the response with the filtered and sorted items
    context = {
        'items': items,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'admin_memento.html', context)



# update
@login_required
def update(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        data = Items.objects.filter(name=name)
        
        if data.exists():
            # Pass the item details to the template if found
            return render(request, "update.html", {"data": data, "name": name})
        else:
            # Display a message if no matching item is found
            return render(request, "update.html", {"msgu": "No data found"})
    else:
        return render(request, "update.html")

#update functionality
@login_required
def updatedata(request):
    if request.method == "POST":
        original_name = request.POST.get('original_name', '').strip()
        
        if original_name:
            data = Items.objects.filter(name=original_name)
            if data.exists():
                item = data.first()
                
                # Retrieve new values from the form
                new_name = request.POST.get('new_name')
                new_type = request.POST.get('new_type')
                new_price = request.POST.get('new_price')
                new_stock = request.POST.get('new_stock')
                new_image = request.FILES.get('new_image')  # For optional image upload
                
                # Update fields only if new values are provided
                if new_name:
                    item.name = new_name
                if new_type:
                    item.type = new_type  # Ensure this is set correctly for your model
                if new_price:
                    item.price = new_price
                if new_stock:
                    item.stock = new_stock
                if new_image:
                    item.image = new_image  # Update the image if a new one is uploaded
                
                # Save the updated item data
                item.save()
                
                return render(request, "update.html", {"msg": "Updated successfully", "data": [item]})
            else:
                return HttpResponse("Item not found.")
        else:
            return HttpResponse("No name provided.")

    return HttpResponse("Error: Invalid request.")


#Delete
@login_required
def delete(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        data = Items.objects.filter(name=name)
        
        if data.exists():
            data.delete()
            return render(request, "delete.html", {"msg": "Deleted successfully "})
        else:
            return render(request, "delete.html", {"msg": "No data found"})
    else:
        return render(request, "delete.html")