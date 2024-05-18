from django.db import models
import uuid
from django.utils.text import slugify
# from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    slug=models.SlugField(blank=True,null=True)
    image = models.ImageField(upload_to = 'image/img-category',  blank = True, null=True, default='')
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Category,self).save(*args,**kwargs)
        
        
    def __str__(self):
        return self.title
    
    
class Products (models.Model):
    
    CHOICES = (
        (0, 'Zero Star'),
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars')
        # Add more choices as needed
    )
    
    name=models.CharField(max_length=100)
    discount = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'image/img-product',  blank = True, null=True, default='')
    old_price = models.FloatField(default=100.00)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    slug = models.SlugField(blank=True,null=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    Wishlist=models.BooleanField(default=False)
    evaluation=models.IntegerField(default=0,choices=CHOICES)

    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100)*self.old_price)
            return new_price
        else:
            return self.old_price
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super(Products,self).save(*args,**kwargs)
        
        
    def __str__(self):
        return self.name
    