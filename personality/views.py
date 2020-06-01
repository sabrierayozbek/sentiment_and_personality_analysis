from django.shortcuts import get_object_or_404, redirect, render
from .forms import Query
from django.http import HttpResponseRedirect
from .minor import Var

def home(request):
        form=Query(request.POST or None)
        context = {
                'form': form,
        }
        if form.is_valid():
                request.session['form']=request.POST
                return HttpResponseRedirect('personAssess')
        return render(request,'home1.html',context)

def personAssess(request):
        form=Query(request.session.get('form'))
        obj=Var()
        agree=0
        opti=0
        pessi=0
        crit=0
        neu=0
        social=0
        view=0
        gram=0
        aciklik = 0
        sorumluluk = 0
        disa_donukluk = 0
        uyumluluk = 0
        duygusal_denge = 0
        public=""
        user=''
        img=''
        yes="yes"
        name=""
        followers=0
        following=0
        tweets=0
        t=[]
        context={
                'agree' : agree,
                'opti' : opti,
                'pessi' : pessi,
                'crit'  : crit,
                'neu' : neu,
                'social' : social,
                'view' : view,
                'gram' : gram,
                'aciklik' : aciklik,
                'sorumluluk' : sorumluluk,
                'disa_donukluk' : disa_donukluk,
                'uyumluluk' : uyumluluk,
                'duygusal_denge' : duygusal_denge,
                'public' : public,
                'user' : user,
                'img' :img,
                'name' :name,
                'followers' :followers,
                'following' :following,
                'tweets' :tweets,
                'parsed' :t,
        }
        if form.is_valid():
                obj=Var()
                obj.subj=request.session.get('form')['Twitter_Handle']
                obj.get_all_tweets()
                agree=obj.agree
                pessi=obj.pessi
                crit=obj.crit
                neu=obj.neu
                social=obj.social
                view=obj.view
                gram=obj.gram
                aciklik=obj.aciklik
                sorumluluk=obj.sorumluluk
                disa_donukluk=obj.disa_donukluk
                uyumluluk=obj.uyumluluk
                duygusal_denge=obj.duygusal_denge
                opti=obj.opti
                public=obj.public
                user=obj.subj
                img=obj.img
                yes=obj.yes
                name=obj.name
                followers=obj.follower
                following=obj.following
                tweets=obj.tweets
                t=obj.t
                #subj=request.session.get('form')['Query']
                if not obj.subj:
                        return render(request,'PerView',context)
                if yes=="no":
                        return render(request,'alt.html',context)
                
        context={
                'agree' : agree,
                'opti' : opti,
                'pessi' : pessi,
                'crit'  : crit,
                'neu' : neu,
                'social' : social,
                'view' : view,
                'gram' : gram,
                'aciklik': aciklik,
                'sorumluluk': sorumluluk,
                'disa_donukluk': disa_donukluk,
                'uyumluluk': uyumluluk,
                'duygusal_denge': duygusal_denge,
                'public' : public,
                'user' : user,
                'img' : img,
                'name' :name,
                'followers' :followers,
                'following' :following,
                'tweets':tweets,
                'parsed':t,
        }
        return render(request,'PerView.html',context)