#coding=utf-8
from django.db import models
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
	photo = models.ImageField("菜品图片",upload_to='dish_photo')
	description = models.TextField("菜品介绍",)
	category = models.DecimalField("分类",max_digits=2,decimal_places=0,choices=CATEGORY_CHOICE)
	be_chice = models.DecimalField("被点数",max_digits=10,decimal_places=0)
#	desk = models.ForeignKey()
	def __unicode__(self):
		return unicode(self.name)
#	desk_id = models.DecimalField(max_digits=2,decimal_places=0)
class Desk(models.Model):             #餐桌
	max_person = models.DecimalField("承受最大人数",max_digits=2,decimal_places=0)
	chair = models.DecimalField("椅子数",max_digits=2,decimal_places=0)
#	dish = models.ForeignKey(Desk_Dish)
#	room_id = models.DecimalField(max_digits=2,decimal_places=0)
	def __unicode__(self):
		return unicode(self.id)
class Desk_Dish(models.Model):
	desk = models.ForeignKey(Desk,primary_key=True)
	dish = models.ForeignKey(Dish,primary_key=True)
	dish_num = models.DecimalField("菜品数量",max_digits=2,decimal_places=0)
class Room(models.Model):             #房间
	desk_num = models.DecimalField("桌子编号",max_digits=2,decimal_places=0)
	air_conditioning = models.BooleanField("空调",)
	desk = models.ForeignKey(Desk)
#	customer_id = models.DecimalField(max_digits=2,decimal_places=0)
	def __unicode__(self):
		return unicode(self.id) 
class Customer(models.Model):
	person_num = models.DecimalField("顾客人数",max_digits=2,decimal_places=0)
	date = models.DateField("就餐时间",)
	consumption= models.DecimalField("总消费",max_digits=2,decimal_places=0)
	room = models.ManyToManyField(Room)
	chair = models.DecimalField("椅子数",max_digits=2,decimal_places=0)
	tableware = models.DecimalField("餐具数",max_digits=2,decimal_places=0)
	def __unicode__(self):
		return unicode(self.id)
