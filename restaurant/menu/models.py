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
	photo = models.ImageField("菜品图片",upload_to='dish_photo',null=True,blank=True)
	description = models.TextField("菜品介绍",null=True,blank=True)
	category = models.DecimalField("分类",max_digits=2,decimal_places=0,choices=CATEGORY_CHOICE)
	be_chice = models.DecimalField("被点数",max_digits=10,decimal_places=0)
#	desk = models.ForeignKey()
	def __unicode__(self):
		return unicode(self.name)
#	desk_id = models.DecimalField(max_digits=2,decimal_places=0)
class Desk(models.Model):             #餐桌
	be_useing = 1
	wait = 2
	cleaning = 3
	BEHAVIOUR_CHOICE = (
			(be_useing,'正在使用'),
			(wait,'等待中'),
			(cleaning,'清理中'),
			)
	behaviour = models.DecimalField("状态",max_digits=1,decimal_places=0,choices=BEHAVIOUR_CHOICE)
	max_person = models.DecimalField("承受最大人数",max_digits=2,decimal_places=0)
	chair = models.DecimalField("椅子数",max_digits=2,decimal_places=0)
	description = models.TextField("备注",null=True,blank=True)
	dish = models.ManyToManyField(Dish,through='Dishship')
#	dish = models.ForeignKey(Desk_Dish)
#	room_id = models.DecimalField(max_digits=2,decimal_places=0)
	def __unicode__(self):
		return unicode(self.id)
#class Room(models.Model):             #房间
#	desk_num = models.DecimalField("桌子编号",max_digits=2,decimal_places=0)
#	desk = models.ForeignKey(Desk)
#	description = models.TextField("备注",null=True)
#	customer_id = models.DecimalField(max_digits=2,decimal_places=0)
#	def __unicode__(self):
#		return unicode(self.id) 
class Customer(models.Model):
	customer_num = models.DecimalField(max_digits=3,decimal_places=0)
	time = models.DateTimeField("就餐时间",)
	def __unicode__(self):
		return unicode(self.id) 
class bill(models.Model):
	date = models.DateTimeField("时间",)
	consumption= models.DecimalField("总消费",max_digits=5,decimal_places=0)
	chair = models.DecimalField("椅子数",max_digits=2,decimal_places=0)
	tableware = models.DecimalField("餐具数",max_digits=2,decimal_places=0)
	description = models.TextField("备注",null=True,blank=True)
	customer = models.ForeignKey(Customer)
	def __unicode__(self):
		return unicode(self.id)
#class Relationships(models.Model):
#	desk = models.ForeignKey(Desk)
#	dish = models.ForeignKey(Dish)
#	customer = models.ForeignKey(Customer)
#	class Meta:
#		unique_together = ('desk','dish','customer')
#	dish_num = models.DecimalField("菜品数量",max_digits=2,decimal_places=0)
#	def __unicode__(self):
#		return unicode(self.customer)
class Dishship(models.Model):
	dish = models.ForeignKey(Dish)
	desk = models.ForeignKey(Desk)
	customer = models.ForeignKey(Customer)
	time = models.DateTimeField()
	dish_num = models.DecimalField("菜品数",max_digits=2,decimal_places=0)
	def __unicode__(self):
		return unicode(self.desk)
