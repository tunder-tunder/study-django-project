from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='article title')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='publised at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='published?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        # verbose_name_plural = 'articles'
        ordering =['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='category name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering =['title']