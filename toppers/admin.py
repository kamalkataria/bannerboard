from django.contrib import admin
from toppers.models import Branch,BranchManager,BranchBoard,Themes
# Register your models here.
from django.contrib.admin.options import StackedInline,TabularInline
from .forms import ThemesForm


class BranchBoardBMInline(StackedInline):
    model = BranchBoard.branch_manager.through
class BranchManagerInline(StackedInline):
    model = BranchManager
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("branch_name", "sol_id")
    inlines = [BranchManagerInline,]

@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    form = ThemesForm
# @admin.register(BranchBoard)
# class BranchBoardAdmin(admin.ModelAdmin):
#     inlines = [BranchManagerInline,]
@admin.register(BranchManager)
class BranchManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "branch")

# admin.site.register(BranchBoard)
class BranchBoardInline(StackedInline):
    model = BranchBoard

@admin.register(BranchBoard)
class BranchBoardAdmin(admin.ModelAdmin):
    inlines = [BranchBoardBMInline,]

#
# @admin.register(BulletinBoard)
# class BulletinBoardAdmin(admin.ModelAdmin):
#     list_display = ("bulletin_date",)
#     inlines = [BranchBoardInline,]
#
#
#

