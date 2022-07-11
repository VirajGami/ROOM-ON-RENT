from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import auth,User
import smtplib
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import *
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.core.mail import send_mail



Customer_session_nm=None
Customer_session_id=None


def index(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id

    cus_list=Customer.objects.all()
    room_list=putroom.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'rental/index.html',{'Customer_session_nm':Customer_session_nm ,'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list,'room_list':room_list})
    return render(request,'rental/index.html',{'cus_list':cus_list,'room_list':room_list})


def alllist(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id

    cus_list=Customer.objects.all()
    room_list=putroom.objects.all()
    return render(request,'rental/alllist.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list,'room_list':room_list})


# def showroom1(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    print(user)
    cus_list=Customer.objects.all()
    room_list=putroom.objects.filter(owner=user)
    print(room_list)
    return render(request,'rental/myroom.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list,'room_list':room_list})

def showroom(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cus_list=Customer.objects.all()
    user1 = Customer.objects.get(id=user)
    print(user1)
    k=user1.CustomerEmail
    print(k)
    room=putroom.objects.raw('SELECT * FROM rental_putroom WHERE  owneremail = %s',[k])
    
    
    return render(request,'rental/myroom.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list,'room':room})





def about(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cus_list=Customer.objects.all()
    room_list=putroom.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'rental/about.html',{'Customer_session_nm':Customer_session_nm ,'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request,'rental/about.html',{ })


def contact(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id  

    if request.method == 'POST':
        Name= request.POST.get('Name','')
        Email= request.POST.get('Email','')
        Subject = request.POST.get('Subject','')
        Message=request.POST.get('Message','')
        c=Contact(Name=Name, Email=Email, Subject=Subject,Message=Message)
        c.save()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
        return render(request,'rental/contact.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize()})
    return render(request,'rental/contact.html',{ })





    

def addroom(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    
    cus_list=Customer.objects.all()
    user1 = Customer.objects.get(id=user)
   
    oname=user1.CustomerName
    oemail=user1.CustomerEmail
    ophone=user1.phone
    
    initial_data={
            'ownername':oname,
            'owneremail':oemail,
            'ownerphone':ophone
    }
    
    d=""
    n=""
    form = data(initial=initial_data)
    if request.method == 'POST':
        form = data(request.POST, request.FILES)
        
        if form.is_valid():
            d = form.cleaned_data.get("roomid")
            n = form.cleaned_data.get("name")
            print(d)
            form.save()
            # subject = ' Added Room  '
            # message = f'Dear {user1.CustomerName},\n Your Room Id:  {d} , Room Name:  {n} \nIs Successfully Added On Our Site.\n \nDo Not Reply this is Computer Generated mail. '
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user1.CustomerEmail, ]
            # send_mail( subject, message, email_from, recipient_list )
            return redirect('rental:index') 
        
           
   
          
    return render(request, 'rental/addroom.html', {'d':d,'n':n,'form' : form,'Customer_session_nm':Customer_session_nm ,'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list})

   




# def addroom(request):
#     Customer_session_nm = None
#     Customer_session_id = None
#     if request.session.has_key('name'):
#         Customer_session_nm=request.session['name']
#     if request.session.has_key('id'):
#             Customer_session_id=request.session['id']
#             print(Customer_session_id)
#     user = Customer_session_id
#     cus_list=Customer.objects.all()

#     if request.method == 'POST' :
#         roomid= request.POST.get('roomid','')
#         name= request.POST.get('name','')
#         image = request.POST.get('image','')
#         location = request.POST.get('location','')
#         # owner = request.POST.get('owner','')
#         Type = request.POST.get('Type','')
#         area = request.POST.get('area','')
#         bed = request.POST.get('bed','')
#         bath = request.POST.get('bath','')
#         parking = request.POST.get('parking','')
#         amenities = request.POST.get('amenities','') 
#         rent = request.POST.get('rent','') 
#         subimage1 = request.POST.get('subimage1','') 
#         subimage2 = request.POST.get('subimage2','') 
#         subimage3 = request.POST.get('subimage3','') 
#         description = request.POST.get('description','') 
        
#         c=putroom(roomid=roomid,name=name,image=image,location=location,Type=Type,area=area,bed=bed,bath=bath,parking=parking,amenities=amenities,rent=rent,subimage1=subimage1,subimage2=subimage2,subimage3=subimage3,description=description)
#         c.save()
     

#     return render(request,'rental/addroom.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list})


def detail(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    
    room=putroom.objects.get(id=id)
    
    return render(request,'rental/detail.html',{'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'room':room})

def deleteroom(request,id):
    Customer_session_nm = None
    Customer_session_id = None
    d=""
    n=""
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cus_list=Customer.objects.all()
    user1 = Customer.objects.get(id=user)
    
    room=putroom.objects.get(id=id)
    d=room.roomid
    n=room.name
    room.delete()
    # subject = ' Removed  Room  '
    # message = f'Dear {user1.CustomerName},\n Your Room Id:  {d} , Room Name:  {n} \nIs Successfully Removed From Our Site.\n \nDo Not Reply this is Computer Generated mail. '
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [user1.CustomerEmail, ]
    # send_mail( subject, message, email_from, recipient_list )
    return redirect('rental:index')
    
    return render(request,'rental/index.html',{'room':room,'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize(),'cus_list':cus_list})







def login(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('id'):
        Customer_session_id=request.session['id']
        print(Customer_session_id)
    user = Customer_session_id

    if request.method=='POST':   
        username=request.POST['username']
        password=request.POST['password']

        Customer_name=Customer.objects.filter(CustomerName__contains=username,CustomerPassword__contains=password).values_list('CustomerName', 'id').first()
        if Customer_name is not None:
                request.session['name'] = Customer_name
                request.session['id'] = Customer_name[1]
                return redirect('rental:cust_login1')

        else:
            messages.error(request, 'Please Enter Valid UserName And Password.')
            return redirect('rental:login')  
                  
    return render(request,'rental/login.html')    



def cust_login1(request):
    Customer_session_nm = None
    Customer_session_id = None
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
    if request.session.has_key('id'):
            Customer_session_id=request.session['id']
            print(Customer_session_id)
    user = Customer_session_id
    cus_list=Customer.objects.all()
    room_list=putroom.objects.all()
    if request.session.has_key('name'):
        Customer_session_nm=request.session['name']
       
    else:
        
        return render(request,'rental/login.html',{})
       
    return render(request,'rental/index.html',{'room_list':room_list,'cus_list':cus_list,'Customer_session_nm':Customer_session_nm ,  'name':Customer.objects.get(id=user).CustomerName.capitalize()})   

def register(request):
    Customer_session_nm = None
    Customer_session_id = None
    c=Customer.objects.all()
    if request.method == 'POST':
        CustomerName= request.POST.get('username','')
        CustomerEmail= request.POST.get('email','')
        CustomerPassword = request.POST.get('password1','')
        phone=request.POST.get('phone','')

        for info in c:
            if info.CustomerEmail ==CustomerEmail:
                print("Email already in use")
                messages.warning(request, 'email already exists.')
                return redirect('rental:register',) 
                   
           
        c=Customer(CustomerName=CustomerName, CustomerPassword=CustomerPassword, CustomerEmail=CustomerEmail,phone=phone)
        
        c.save()
    
        # subject = 'welcome to Room on Rent '
        # message = f'Dear {c.CustomerName}, \n \n Thanks for you Registration in ROOM ON RENT.\n \n Your account has been successfully created  And You can put your Room on rent.\n Your Password is:{c.CustomerPassword} \n \n  Do Not Reply this is Computer Generated mail. '
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [c.CustomerEmail, ]
        # send_mail( subject, message, email_from, recipient_list )
            
        return redirect('rental:login',)
    return render(request, 'rental/register.html', {})            

def logout(request):

    
    try:
        del request.session['name']
        return redirect('rental:index',)
    except:
      pass
    return redirect('rental:index')





# def sendmail(CustomerEmail):
#     print("send mail call")
#     server =smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login('gamiviraj222002@gmail.com','gamiviraj222002@vb09')
#     server =smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login('gamiviraj222002@gmail.com','gamiviraj222002@vb09')
#     email = CustomerEmail
#     name = CustomerName

#     subject ='Registration'
#     body= 'Dear ' + str(name) +' ,'+ '\n Thanks for you Registration in E-Pustakshala. Your account has been successfully created. \n Visit : e-pustakshala.herokuapp.com/contact for any query -From Viraj Gami' 

#     msg=f"subject:{subject}\n\n{body}"

#     server.sendmail(
#         'gamiviraj222002@gmail.com',
#         email,
#         msg
#     )
#     print('msg has been send')
#     server.quit()
   
