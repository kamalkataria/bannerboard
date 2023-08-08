from django.db import models
from django.utils import timezone
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
class Branch(models.Model):
    sol_id=models.IntegerField(default=0000)
    branch_name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch_name}"

#
# class BulletinBoard(models.Model):
#     bulletin_date=models.DateField(default=timezone.now,blank=True,null=True)
#     category=models.CharField(max_length=500)
#     def __str__(self):
#         return f"{self.bulletin_date}"






class BranchManager(models.Model):
    branch=models.OneToOneField(Branch,on_delete=models.DO_NOTHING)
    employee_code=models.IntegerField(default=0043,primary_key=True)
    # bboard=models.ForeignKey(BranchBoard,on_delete=models.CASCADE,blank=True,null=True,related_name="bboard")
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return f"{self.name}"

class Themes(models.Model):
    theme=models.CharField(max_length=200,primary_key=True)
    body_bg_image=models.ImageField(upload_to='images/', blank=True, null=True)
    left_image = models.ImageField(upload_to='images/', blank=True, null=True)
    center_image = models.ImageField(upload_to='images/', blank=True, null=True)
    bg_image = models.ImageField(upload_to='images/', blank=True, null=True)
    org_image = models.ImageField(upload_to='images/', blank=True, null=True)
    showit=models.BooleanField(default=False)
    content_right=models.CharField(max_length=200,default="Well done!\nKeep it Up")
    right_content_fg=models.CharField(max_length=20,default="#000000")
    right_content_fg_transparency=models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],)
    right_content_bg = models.CharField(max_length=20,default="#000000")
    right_content_bg_transparency = models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],)
    center_content_bg = models.CharField(max_length=20, default="#000000")
    center_content_bg_transparency = models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], )
    title_property=models.CharField(max_length=200,default="tag is-warning is-dark is-large is-rounded")
    title_text_color=models.CharField(max_length=7,default="#000000")
    category_property = models.CharField(max_length=200, default="tag is-medium is-warning text text-danger is-centered text-center")
    category_text_color = models.CharField(max_length=7, default="#000000")
    bm_box_shadow=models.CharField(max_length=7,default="#000000")
    bm_box_shadow_transparency=models.FloatField(default=0.0,validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],)
    bm_name_color=models.CharField(max_length=7,default="#000000")
    amount_bg_color=models.CharField(max_length=7,default="#FFFFF0")
    amount_fg_color=models.CharField(max_length=7,default="#353935")
    branch_fg_color=models.CharField(max_length=7,default="#FFFFFF")
    branch_bg_color=models.CharField(max_length=7,default="#3da4ab")

    def __str__(self):
        return f"{self.theme}"


class BranchBoard(models.Model):
    # bulletin=models.ForeignKey(BulletinBoard,on_delete=models.CASCADE,blank=True,null=True,related_name="bullet_boards")
    datex=models.DateField(default=timezone.now,blank=True, null=True)
    category = models.CharField(max_length=500)
    branch_manager=models.ManyToManyField(BranchManager,through='BranchBoardBM')


    def __str__(self):
        return f"{self.bulletin_date}"

    def __str__(self):
        return f"{self.datex},{self.category}"

class  BranchBoardBM(models.Model):
    bm = models.ForeignKey(BranchManager,on_delete=models.CASCADE)
    board = models.ForeignKey(BranchBoard,on_delete=models.CASCADE)
    amt=models.FloatField(default=0)

