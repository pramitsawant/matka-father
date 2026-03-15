from utils.helpers import get_daily_sorted_digits
import os
# print(get_daily_sorted_digits())

from utils.chart_generator import ChartGenerator

template_path = os.getcwd()+'/templates/daily.png'
font_path_archivo = os.getcwd()+'/fonts/ArchivoBlack-Regular.ttf'
font_path_cinzel = os.getcwd()+'/fonts/Cinzel-Regular.ttf'


c = ChartGenerator(font_path_archivo=font_path_archivo,font_path_cinzel=font_path_cinzel)
c.get_single_template(template_path=template_path)
c.save(file="new.png")


