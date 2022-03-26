from django.db import models

# Create your models here.

class Movie(models.Model): #ctrl+ left.mouse
    
    class TYPE:
        MOVIE = 'MOVIE'
        TRAILER = 'TRAILER' 
        SHOW = 'SHOW'
        SERIES = 'SERIES'
    
        CHOICES = (
            (MOVIE, MOVIE),
            (TRAILER, TRAILER),
            (SHOW, SHOW),
            (SERIES, SERIES)
            )   
    
    title = models.CharField(max_length=50) #VARCHAR(50)
    released_year = models.IntegerField(null=True) #released_year INT
    language = models.CharField(max_length=50, default='O\'zbek tili')
    duration = models.CharField(max_length=200)
    views_count = models.IntegerField(default=0)
    source_link = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50,
                            choices=TYPE.CHOICES, default=TYPE.MOVIE)
    banner = models.ImageField(upload_to='banners')
    slug = models.SlugField(max_length=300)
    objects = models.Manager()
    category_id = models.IntegerField(null = True)
    def __str__(self):
        return self.title

# models.PositiveIntegerField() # >=0
# models.PositiveSmallIntegerField() #>=0
# models.BooleanField() #Boolean
# models.DateField(auto_now=False) # YYYY/MM/DD sana
# models.DecimalField(max_digits=10, decimal_places=2) #DECIMAL(n,m)
# models.FileField() #Fayllarni saqlash uchun
# models.TextField() -katta textlarni saqlash uchun charfieldga o'xhash ammo bunda limit yo'q

# commads
"""# 1-step python manage.py makemigrations
# 2-step python manage.py migrate 
# databasega saqlash uchund
# 3-step python manage.py showmigrations"""
# databaseni tekshirish uchun
#  fsfsdfs
# movie_1 = Movie(title="Avengers")

# save to db object_name.save()
#agar models.py nomli faylga o'zgartirish kiritsak 
# shell exit() qilib yana yangidan ochishimiz kerak
# git 
# git -- version
# git init
# git status
#  git add folder
# git commit -m " tetx"
# git config user.name "username"
# git config user.email "email"
# git log