import PIL
from PIL import Image, ImageDraw, ImageFont
import os
import io
from datetime import datetime

class ChartGenerator:
    def __init__(self, font_path_archivo,font_path_cinzel):
        self.primary_fill = (229,175,55)
        self.white_fill = (255,255,255)
        self.market_title_font = ImageFont.truetype(font_path_cinzel, 60)
        self.week_title_font = ImageFont.truetype(font_path_archivo, 46)
        self.date_title_font = ImageFont.truetype(font_path_archivo, 26)
        self.panna_font = ImageFont.truetype(font_path_archivo, 100)
        self.numbers_font = ImageFont.truetype(font_path_archivo, 45)

        self.template = None
        self.draw = None

    def __add_market_title(self, market_title):
        self.draw.text((512, 182), market_title, font=self.market_title_font, anchor="ms", fill=self.primary_fill)

    def __add_week_title(self, week_title):        
        self.draw.text((512, 370), week_title, font=self.week_title_font, anchor="ms", fill=self.primary_fill)

    def __add_date_title(self, date_title):
        self.draw.text((512, 410), date_title, font=self.date_title_font, anchor="ms", fill=self.primary_fill)

    def __add_panna(self, panna):
        self.draw.text((512, 560), panna, font=self.panna_font, anchor="ms", fill=self.primary_fill)

    def __add_numbers(self, numbers):
        self.draw.text((512, 715), numbers, font=self.numbers_font, anchor="ms", fill=self.primary_fill)

    def get_single_template(self, template_path:str):
        target_date = datetime.now()    
        date_str = target_date.strftime("%Y-%m-%d" )
        week_str = target_date.strftime("%A" )
        self.template = Image.open(template_path)
        self.draw = ImageDraw.Draw(self.template)                        
        self.__add_market_title("Main")
        self.__add_week_title(week_title=week_str)
        self.__add_date_title(date_title=date_str)
        self.__add_panna(panna="3-8-9")
        self.__add_numbers(numbers="38 - 39 - 89 - 83 - 93 - 98")

    def get_img(self):
        target_date = datetime.now()    
        date_str = target_date.strftime("%Y-%m-%d" )
        bio = io.BytesIO()
        bio.name = date_str+'.png'
        self.template.save(bio, 'PNG')
        bio.seek(0)
        return bio
        
    def save(self,file):
        self.template.save(file) 
        self.template = None
        self.draw = None

