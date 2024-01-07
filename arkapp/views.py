from math import ceil
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from arkapp import Keys

from arkapp.models import Product,Orders,OrderUpdate

# Create your views here.
def home(request):
    current_user=request.user
    print(current_user)
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n//4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}   
    print(params) 
    return render(request,'index.html',params)


def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Login & try again!')
        return redirect('/auth/login')
    if request.method=='POST':

        item_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amt')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zib_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        Order=Orders(items_json=item_json,name=name,amount=amount,email=email,address1=address1,address2=address2,city=city,state=state,zib_code=zib_code,phone=phone)
        print(amount)
        Order.save()
        update=OrderUpdate(order_id=Order.order_id,update_desc='the order has been placed')
        update.save()
        thanks=True
    #payment integration
        id=Order.order_id
        oid=str(id)+'infykart'
        # parm_dic={
        #     'MID':Keys.MID,      #MERCHANT KEY
        #     'ORDER_ID':oid,
        #     'TXN_AMOUNT':str(amount),
        #     'CUST_ID':email,
        #     'INDUSTRY_TYPE_ID':'Retail',
        #     'WEBSITE':'WEBSTAGING',       
        #     'CHANNEL_ID':'WEB',
        #     'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        # }
        filter2=Orders.objects.filter(order_id=str(id))
        for i in filter2:
            i.oid=oid
            i.amountpaid=amount
            i.paymentstatus='PAID'
            i.save()
        #parm_dic['CHECHSUMHASH']=checksum.generate_checksum(parm_dic,MERCHANT_KEY=Keys.MK)  #WILL DO THE TRANSACTION AND CHECK EVERYTHING
        return redirect('/finished')
    return render(request,'checkout.html')

def finished(request):
     return render(request,'finished.html')    