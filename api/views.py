from django.http import HttpRequest,JsonResponse
from .models import SmartPhone,Cart
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from base64 import b64decode
from django.contrib.auth import authenticate

def isAuth(auth):
    if auth is None:
        return False
    # Get token
    token = auth.split(' ')[1]
    auth=b64decode(token).decode() # Decode token
    username, password = auth.split(':') # Split token

    # Check if user is authenticated
    
    user = authenticate(username=username, password=password)

    if user is not None:
        return user
    return False

def get_all_phones(req:HttpRequest):
    if req.method=='GET':
        phones=SmartPhone.objects.all()
        ans=[]
        for phone in phones:
            ans.append({
                'id':phone.id,
                'price':phone.price,
                'img_url':phone.img_url,
                'color':phone.color,
                'ram':phone.ram,
               'memory':phone.memory,
                'name':phone.name,
               'model':phone.model,
                'add_date':phone.add_date,
                'update_date':phone.up_date
            })
        return JsonResponse(ans, safe=False)

def add_phone(req:HttpRequest):
    if req.method=='POST':
        phone=req.body
        phone=phone.decode()
        phone=json.loads(phone)
        price = phone.get('price', 0)
        img_url = phone.get('img_url', 0)
        color = phone.get('color', 0)
        ram = phone.get('ram', 0)
        memory = phone.get('memory', 0)
        name = phone.get('name', 0)
        model = phone.get('model', 0)
        ans=SmartPhone(
            price=price,
            img_url=img_url,
            color=color,
            ram=ram,
            memory=memory,
            name=name,
            model=model
        )
        ans.save()
    return JsonResponse({'result':'ok'})

def model_phones(req:HttpRequest):
    if req.method=='POST':
        ans=req.body.decode()
        ans=json.loads(ans)
        models={}
        phones=SmartPhone.objects.all().filter(model=ans['model'])
        for phone in phones:
            models[phone.id]={
            'id': phone.id,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
            'memory':phone.memory,
            'name':phone.name,
            'model':phone.model,
            'add_date':phone.add_date,
            'update_date':phone.up_date
            }
            
    return JsonResponse(models)
def search_name(req:HttpRequest):
    if req.method=='POST':
        ans=req.body.decode()
        ans=json.loads(ans)
        phones=SmartPhone.objects.filter(name__icontains=ans['name'])
        res={}
        for phone in phones:
            res[phone.id]={
            'id': phone.id,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
            'memory':phone.memory,
            'name':phone.name,
            'model':phone.model,
            'add_date':phone.add_date,
            'update_date':phone.up_date
            }        
        return JsonResponse(res)

def upd_phone(req:HttpRequest):
    if req.method=='POST':
        ans=req.body.decode()
        ans=json.loads(ans)
        sear=ans['name']
        ph=ans['phone']
        try:
            phone=SmartPhone.objects.get(id=sear)
        except ObjectDoesNotExist:
            return JsonResponse({'result':'bad request'})
        else:
            phone=SmartPhone.objects.filter(id=sear).update(
            price=ph['price'],
            img_url=ph['img_url'],
            color=ph['color'],
            ram=ph['ram'],
            memory=ph['memory'],
            name=ph['name'],
            model=ph['model']
            ) 
            phone.save()
            return JsonResponse({'result':'ok'})
    return JsonResponse({'result':'no method'})

def sign_in(req:HttpRequest):
    """
    input:
        password,
        username,
        email
    output-->dict:
        ans={
            result:ok
        }
    """
    if req.method=="POST":
        user=req.body
        user=json.loads(user.decode())
        auth=req.headers.get('Authorization')
        token = auth.split(' ')[1]
        auth=b64decode(token).decode() # Decode token
        username, password = auth.split(':')
        email=user['email']
        try:
            userbek=User.objects.get(username=username)
        except:
            user=User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'result':'ok'})
        else:
            return JsonResponse({'result':'bad request'})
    return JsonResponse({'result':'no method'})

def sign_up(req:HttpRequest):
    if req.method=="POST":
        user=req.headers.get('Authorization')
        if isAuth(user):
            products=[]
            cart=Cart.objects.filter(user=isAuth(user))
            for c in cart:
                ph_id=c.phone_id
                try:
                    phone=SmartPhone.objects.get(id=ph_id)
                except:
                    return JsonResponse({'result':'No such phone'})
                else:
                    products.append({
                        'price':phone.price,
                        'img_url':phone.img_url,
                        'color':phone.color,
                        'ram':phone.ram,
                        'name':phone.name,
                        'model':phone.model
                    })
            return JsonResponse({'result':products})
        else:
            return JsonResponse({'result':'No Authentication'})
    return JsonResponse({'result':'no method'})

def add_product_cart(req:HttpRequest,pk:int):
    if req.method == 'POST':
        pdct=req.body.decode()
        pdct=json.loads(pdct)
        ph_id=pdct['phone_id']
        us_id=pdct['user_id']
        try:
            phone=SmartPhone.objects.get(id=ph_id)
            us=User.objects.get(id=us_id)
            user=Cart.objects.get(user=us)
            cart=Cart(phone_id=ph_id, phone_name=phone.name, user=us)
        except:
            return JsonResponse({'result':'Bad Request'})
    return JsonResponse({'result':'no method'})



def sort_max(request:HttpRequest,max:float):
    if request.method=='GET':
        phones=SmartPhone.objects.filter(price__lte=max)
        ans=[]
        for phone in phones:
            ans.append({
            'id': phone.id,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
            'memory':phone.memory,
            'name':phone.name,
            'model':phone.model
            })
        return JsonResponse(ans,safe=False)

def sort_min(request:HttpRequest,min:float):
    if request.method=='GET':
        phones=SmartPhone.objects.filter(price__gte=min)
        ans=[]
        for phone in phones:
            ans.append({
            'id': phone.id,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
           'memory':phone.memory,
            'name':phone.name,
           'model':phone.model
            })
        return JsonResponse(ans,safe=False)
        


