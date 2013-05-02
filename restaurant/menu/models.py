#coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class Dish(models.Model):              #菜类
    soup = 1
    hot_dish = 2
    cold_dish = 3
    signature_dishes = 4
    dessert = 5
    seafood = 6
    chafing_dish = 7
    CATEGORY_CHOICE = (
            (soup,'汤类'),
            (hot_dish,'热菜'),
            (cold_dish,'凉菜'),
            (signature_dishes,'招牌菜'),
            (dessert,'甜点'),
            (seafood,'海鲜'),
            (chafing_dish,'火锅'),
            )
    name = models.CharField("菜名",max_length=30)
    price = models.DecimalField("价格",max_digits=5,decimal_places=2)
    photo = models.ImageField("菜品图片",upload_to='dish_photo',null=True,blank=True)
    description = models.TextField("菜品介绍",null=True,blank=True)
    category = models.DecimalField("分类",max_digits=2,decimal_places=0,choices=CATEGORY_CHOICE)
    be_chice = models.DecimalField("被点数",max_digits=10,decimal_places=0,default=0)
    def __unicode__(self):
        return unicode(self.name)
#class Desk(models.Model):             #餐桌
#	be_useing = 1
#	wait = 2
#	cleaning = 3
#	BEHAVIOUR_CHOICE = (
#			(be_useing,'正在使用'),
#			(wait,'等待中'),
#			(cleaning,'清理中'),
#			)
#	behaviour = models.DecimalField("状态",max_digits=1,decimal_places=0,choices=BEHAVIOUR_CHOICE)
#	max_person = models.DecimalField("承受最大人数",max_digits=2,decimal_places=0)
#	chair = models.DecimalField("椅子数",max_digits=2,decimal_places=0)
#	description = models.TextField("备注",null=True,blank=True)
#	dish = models.ManyToManyField(Dish,through='Dishship')
#	def __unicode__(self):
#		return unicode(self.id)
class MyUser(AbstractBaseUser):
    consumption= models.DecimalField("菜品总消费",max_digits=5,decimal_places=0)
    times = models.DecimalField("消费次数",max_digits=4,decimal_places=0)
    def __unicode__(self):
        return unicode(self.id)
class MyUser_data(models.Model):
    time = models.DateTimeField("就餐时间",)
    cost = models.DecimalField("本次消费",max_digits=6,decimal_places=2)
    user = models.OneToOneField(MyUser)
    def __unicode__(self):
        return unicode(self.user)
class Dishship(models.Model):
    dish = models.ForeignKey(Dish)
#	desk = models.ForeignKey(Desk)
#	time = models.DateTimeField()
    dish_num = models.DecimalField("菜品数",max_digits=2,decimal_places=0)
    money = models.DecimalField("小计",max_digits=3,decimal_places=1)
    def __unicode__(self):
        return unicode(self.desk)
class menu(object):
    def __inti__(self, *args, **kwargs):
        slif.items = []
        self.total_price = 0
    def add_dish(self,Dish):
        self.total_price += Dish.price
        for itme in self.items:
            if item.Dish.id == Dish.id:
                item.quantity += 1
        return self.item.append(Dishship(dish=dish,money=Dish.price,quantity=1))
