from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import BranchBoard,Branch,BranchBoard,BranchManager,BranchBoardBM,Themes
from _datetime import date
from django.db import transaction
from django.shortcuts import render,redirect
def hex_to_rgba(hex,alpha):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    rgb.append(alpha)
    return tuple(rgb)

def index(request):
    # return HttpResponse("Hellos")
    latest_bulletins=BranchBoard.objects.filter(datex__contains=date.today())
    theme=Themes.objects.filter(showit=True).first()
    right_content_fg=theme.right_content_fg
    right_content_bg=theme.right_content_bg
    right_content_fg_transparency=theme.right_content_fg_transparency
    right_content_bg_transparency=theme.right_content_bg_transparency
    center_content_bg=theme.center_content_bg
    center_content_bg_transparency=theme.center_content_bg_transparency
    right_content_fg_rgba="rgba"+str(hex_to_rgba(right_content_fg.lstrip('#'),right_content_fg_transparency))
    right_content_bg_rgba="rgba"+str(hex_to_rgba(right_content_bg.lstrip('#'),right_content_bg_transparency))
    center_content_bg="rgba"+str(hex_to_rgba(center_content_bg.lstrip('#'),center_content_bg_transparency))
    title_propery=theme.title_property
    title_text_color=theme.title_text_color
    category_propery = theme.category_property
    category_text_color = theme.category_text_color

    if(latest_bulletins):
        branch_board_bm=BranchBoardBM.objects.filter(board=latest_bulletins[0]).select_related()
    else:
        return HttpResponse("No data for today. Please Add records to display")
    context = {"bmx": latest_bulletins, "bbbm": branch_board_bm, "theme": theme, \
               'right_content_fg_rgba': right_content_fg_rgba, \
               'right_content_bg_rgba': right_content_bg_rgba, 'center_content_bg_rgba': center_content_bg,
               "title_property": title_propery, "title_text_color": title_text_color, \
               "category_property": category_propery, "category_text_color": category_text_color,
               "bm_box_shadowrgba":"rgba"+str(hex_to_rgba(theme.bm_box_shadow.lstrip("#"),theme.bm_box_shadow_transparency)),\
               "bm_name_color":theme.bm_name_color,"amount_bg_color":theme.amount_bg_color,"amount_fg_color":theme.amount_fg_color,\
               "branch_fg_color":theme.branch_fg_color,"branch_bg_color":theme.branch_bg_color,
               "body_bg_image":theme.body_bg_image,
               }
    return render(request=request,template_name="bannerboard/index.html",context=context)

