from django.db import models

# Create your models here.
# model yaratish


class Product(models.Model):
    # string
    name = models.CharField(max_length=250)
    # integer
    proce = models.IntegerField()
    

class PortfolioProject(models.Model):
    nomi = models.CharField(max_length=200, verbose_name="O'yin nomi")
    category = models.CharField(max_length=100, verbose_name="Kategoriya")
    description = models.TextField(verbose_name="Tavsif")
    rasmmi = models.ImageField(upload_to='portfolio/', verbose_name="Rasm")
    texnoligiya = models.CharField(max_length=300, verbose_name="Texnologiyalar (vergul bilan)")
    


    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = "Portfolio Loyihasi"
        verbose_name_plural = "Portfolio Loyihalari"
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def umumiy_narx(self):
        return self.product.narxi * self.quantity
# class News(models.Model):
#     name = models.CharField("Nomi")
#     image = models.ImageField(upload_to='media')
#     text = models.TextField()
#     price= models.IntegerField("narxi ($)")


#     def __str__(self):
#         return self.name
    


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name="Sarlavha")
    game_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="O'yin nomi")
    
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Rasm")
    
    description = models.TextField(verbose_name="Tavsif")
    
    release_date = models.DateField(blank=True, null=True, verbose_name="Chiqish sanasi")

    
    is_published = models.BooleanField(default=True, verbose_name="Nashr qilingan")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

class Trending(models.Model):
    nomi = models.CharField("oyin nomi")
    rasmi=models.ImageField("rasmi")
    categoriya=models.CharField("kategoriya")

    class Meta:
        verbose_name = "Trending O'yin"
        verbose_name_plural = "Trending O'yinlar"
        ordering = ['-id']
    def __str__(self):
        return self.nomi        
