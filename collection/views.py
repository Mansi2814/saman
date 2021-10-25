from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from collection.models import Men,Women,Accessory
# from collection.models import Orders

# Create your views here.

# def signin(request):
#     if request.method == "POST":
#         usernamein = request.POST.get('usernamein')
#         passin = request.POST.get('passin')
#         # request.session['username'] = usernamein
#         user = authenticate(username=usernamein, password=passin)
#         if user:
#             login(request, user)
#             messages.success(request,'Logged In Successfully!')
#         else:
#             messages.warning(request, 'Invalid Credentials!! Please Try Again')
#     return redirect('/')



def index(request):
    l1=Men.objects.filter(latest=True)
    l2=Women.objects.filter(latest=True)
    l3=Accessory.objects.filter(latest=True)
    latest=[]
    for i in l1:
        latest.append(i)
    for i in l2:
        latest.append(i)
    for i in l3:
        latest.append(i)
    f1=Men.objects.filter(featured=True)
    f2=Women.objects.filter(featured=True)
    f3=Accessory.objects.filter(featured=True)
    featured=[]
    for i in f1:
        featured.append(i)
    for i in f2:
        featured.append(i)
    for i in f3:
        featured.append(i)
    data={"latest":latest,
          "featured":featured}
    return render(request, 'index.html',data)

def men(request):
    # all=Men.objects.all()
    # for i in all:
    #     i.ordered=False
    #     i.save()
    shirts=Men.objects.filter(category="shirt")
    trousers = Men.objects.filter(category="trouser")
    winters = Men.objects.filter(category="winter")
    data={"shirts":shirts,
          "trousers":trousers,
          "winters":winters}
    return render(request,'men.html',data)

def women(request):
    # all=Women.objects.all()
    # for i in all:
    #     i.ordered=False
    #     i.save()
    shirts=Women.objects.filter(category="shirt")
    trousers = Women.objects.filter(category="trouser")
    winters = Women.objects.filter(category="winter")
    data={"shirts":shirts,
          "trousers":trousers,
          "winters":winters}
    return render(request,'women.html',data)

def accessory(request):
    # all=Accessory.objects.all()
    # for i in all:
    #     i.ordered=False
    #     i.save()
    shoes=Accessory.objects.filter(category="shoe")
    watches = Accessory.objects.filter(category="watch")
    perfumes = Accessory.objects.filter(category="perfume")
    glasses = Accessory.objects.filter(category="glass")
    offers=Accessory.objects.filter(category="offer")
    data={"shoes":shoes,
          "watches":watches,
          "perfumes":perfumes,
          "glasses":glasses,
          "offers":offers}
    return render(request,'accessory.html',data)

def account(request):
    orderedItems1=Men.objects.filter(ordered=True)
    orderedItems2 = Women.objects.filter(ordered=True)
    orderedItems3 = Accessory.objects.filter(ordered=True)
    orderedItems=[]
    for i in orderedItems1:
        orderedItems.append(i)
    for i in orderedItems2:
        orderedItems.append(i)
    for i in orderedItems3:
        orderedItems.append(i)
    data={"orderedItems": orderedItems}
    print(orderedItems)
    return render(request,'account.html',data)

def cart(request):
    cartItems1=Men.objects.filter(addedToCart=True)
    cartItems2 = Women.objects.filter(addedToCart=True)
    cartItems3 = Accessory.objects.filter(addedToCart=True)
    cartItems=[]
    for i in cartItems1:
        cartItems.append(i)
    for i in cartItems2:
        cartItems.append(i)
    for i in cartItems3:
        cartItems.append(i)
    print("hee",cartItems)
    subtotal=0
    for i in cartItems:
        subtotal+=(int(i.Price)*i.quantity)
    tax=0.18*subtotal
    total=subtotal+tax
    data={"cartItems":cartItems,
          "subtotal": subtotal,
          "tax": round(tax),
          "total": total}
    return render(request,'cart.html',data)

def addToCart(request,product_id):
    prod1=Men.objects.filter(product_id=product_id)
    if len(prod1)==0:
        prod1=Women.objects.filter(product_id=product_id)
    if len(prod1)==0:
        prod1=Accessory.objects.filter(product_id=product_id)
    # print("he",prod1[0])
    prod1[0].added()
    # prod1[0].addedToCart=True
    # prod1[0].save()
    # print("hi",Men.objects.filter(addedToCart=True))
    # return redirect('/cart')
    print("ho",request.META['HTTP_REFERER'])
    u=request.META['HTTP_REFERER']
    print("hii",product_id)
    print("hee",u)
    u=u+'#'+product_id
    return redirect(u)

def delete_cartItem(request,product_id):
    prod2=Men.objects.filter(product_id=product_id)
    if len(prod2)==0:
        prod2=Women.objects.filter(product_id=product_id)
    if len(prod2)==0:
        prod2=Accessory.objects.filter(product_id=product_id)
    prod2[0].deleted()
    return redirect('/cart')

def changeQuantity(request,product_id):
    if request.method=="POST":
        quan=request.POST.get("quantity")
        item=Men.objects.filter(product_id=product_id)
        if len(item) == 0:
            item = Women.objects.filter(product_id=product_id)
        if len(item) == 0:
            item = Accessory.objects.filter(product_id=product_id)

        item[0].changedQuantity(quan)
        print("he",quan)
        return redirect('/cart')

def order_placed(request):
    cartItems1= Men.objects.filter(addedToCart=True)
    cartItems2 = Women.objects.filter(addedToCart=True)
    cartItems3 = Accessory.objects.filter(addedToCart=True)
    for i in cartItems1:
        i.ordered1()
        i.deleted()
    for i in cartItems2:
        i.ordered1()
        i.deleted()
    for i in cartItems3:
        i.ordered1()
        i.deleted()
    # print("or",Orders.objects.all())
    return redirect('/account')

