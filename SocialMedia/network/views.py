from django.shortcuts import render,redirect

from django.views import View

from network.models import Profile,Post,Like,Comment,Follower

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from network.forms import RegistrationForm,LoginForm,ProfileForm,PostForm,CommentForm

from django.db.models import Q


# Create your views here.


class SignUpView(View):

  def get(self,request,*args, **kwargs):

    form=RegistrationForm()

    return render(request,'register.html',{'form':form})

  def post(self,request,*args, **kwargs):

    form=RegistrationForm(request.POST)

    if form.is_valid():

      form.save()

      return redirect('signin')

    return render(request,'login.html',{'form':form})

class SignInView(View):

  def get(self,request,*args, **kwargs):

    form=LoginForm()

    return render(request,'login.html',{'form':form})

  def post(self,request,*args, **kwargs):

    form=LoginForm(request.POST)

    if form.is_valid():

      uname=form.cleaned_data.get('username')

      pwd=form.cleaned_data.get('password')

      user_object=authenticate(request,username=uname,password=pwd)

      if user_object:

        login(request,user_object)

        return redirect('home')

    return render(request,'login.html',{'form':form})

class SignOutView(View):

    def get(self,request,args,*kwargs):

        logout(request)
        
        return redirect("signin")


# home page
# ------------

class HomeView(View):

  def get(self,request,*args, **kwargs):

   qs=Post.objects.all().order_by("-created_date")

   qs1=Profile.objects.get(name=request.user)

   return render(request, 'home.html', {'data': qs,'data1':qs1})


# user profile
# ---------------

class ProfileView(View):

  def get(self,request,*args, **kwargs):

    qs=Profile.objects.get(name=request.user)

    qs_1=Post.objects.filter(user_object=request.user)

    return render(request,'profile.html',{'data':qs,'data_1':qs_1})  

# profile update
# ---------------

class UpdateUserProfileView(View):

  def get(self,request,*args, **kwargs):

    qs=Profile.objects.get(name=request.user)

    form=ProfileForm(instance=qs)

    return render(request,'profile_update.html',{'form':form})

  def post(self,request,*args, **kwargs):

    qs=Profile.objects.get(name=request.user)

    form=ProfileForm(request.POST,instance=qs,files=request.FILES)

    if form.is_valid():

      form.instance.name=request.user

      form.save()

      return redirect('profile')

    return render(request,'profile_update.html',{'form':form})

# post upload
# ----------

class PostUploadView(View):

  def get(self,request,*args,**kwargs):
    
        form=PostForm()

        return render(request,"post_upload.html",{"form":form})

  def post(self,request,*args,**kwargs):

        form=PostForm(request.POST,files=request.FILES)

        if form.is_valid():

            form.instance.user_object=request.user

            form.save()

            return redirect("home")

        return render(request,"post_upload.html",{"form":form})


# like count view
# ----------

class LikeCountUpdateView(View):

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Post.objects.get(id=id)

        action=request.POST.get("action")

        if action=="like":

            qs.like.add(request.user)

            Like.objects.create(user=request.user,post=qs)

            return redirect("home")
        

        
        # like=0
        # for i in Like.objects.all():
        #     like+=1
        # return render(request,"home.html",{"like":like})

        # return redirect("home")

# post-detail view
# ---------------

class PostDetailView(View):

  def get(self,request,*args, **kwargs):

    id=kwargs.get('pk')

    qs=Post.objects.get(id=id)

    p1=Profile.objects.get(name=request.user)

    return render(request,'post_detail.html',{'data':qs,'p1':p1})

# post-update view
# ---------------

class PostUpdateView(View):

  def get(self,request,*args, **kwargs):
   
   id=kwargs.get('pk')

   post_obj=Post.objects.get(id=id)

   form=PostForm(instance=post_obj)

   return render(request,"post_update.html",{"form":form})

  def post(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        post_obj=Post.objects.get(id=id)

        form=PostForm(request.POST,files=request.FILES,instance=post_obj)

        if form.is_valid():

            form.save()

            return redirect("profile")

        return render(request,"post_update.html",{"form":form})


# post-deleteview
# --------------------

class PostDeleteView(View):

  def get(self,request,*args, **kwargs):

    id=kwargs.get('pk')

    Post.objects.get(id=id).delete()

    return redirect('profile')


# commentview
# --------------


class CommentCreateView(View):

  def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        post_obj=Post.objects.get(id=id)
    
        form=CommentForm()

        return render(request,'comment_add.html',{"form":form})

  def post(self,request,*args,**kwargs):
        
        id=kwargs.get('pk')

        post_obj=Post.objects.get(id=id)

        form=CommentForm(request.POST)

        if form.is_valid():

            form.instance.post_object=post_obj

            form.instance.user_object=request.user

            form.save()

            return redirect("home")

        return render(request,'comment_add.html',{"form":form})




# commentlist view
# ------------------

class CommentListView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        post_object=Post.objects.get(id=id)

        qs=Comment.objects.filter(post_object=post_object)

        return render(request,"comment_list.html",{"data":qs})

