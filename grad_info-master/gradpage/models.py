from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

class Display_info(models.Model):
    title=models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    date = models.DateField()
    link=models.URLField()
    image = models.ImageField(upload_to='gradpage/images/%Y/%m/%d/')

class Archive(models.Model):
    title=models.TextField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='gradpage/images/%Y/%m/%d/')

class Major(models.Model):
    name = models.CharField(max_length=30, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    require_for_grad = models.TextField()
    display_info = models.ForeignKey(Display_info, null=True, blank=True, on_delete=models.SET_NULL)
    archive = models.ForeignKey(Archive, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/{self.department}/{self.name}/'



