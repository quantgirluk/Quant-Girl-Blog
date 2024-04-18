from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import numpy as np
from wordcloud import ImageColorGenerator
from PIL import Image


from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt

def get_text_pdf(path):

    resource_manager = PDFResourceManager()
    string_io = StringIO()
    la_params = LAParams()
    device = TextConverter(resource_manager, string_io, laparams=la_params)

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, device)
    password = ""
    max_pages = 0
    caching = True
    pagenos = set()
    pages = PDFPage.get_pages(fp, pagenos,
                              maxpages=max_pages, password=password, caching=caching,
                              check_extractable=True)

    for page in pages:
        interpreter.process_page(page)

    text = string_io.getvalue()
    fp.close()
    device.close()
    string_io.close()

    return text


text = get_text_pdf('data/Jarrow_Protter.pdf')
font = 'fonts/Quicksand-Bold.ttf'
custom_mask = np.array(Image.open("data/heart.png"))
word_cloud = WordCloud(font_path=font, mask=custom_mask,
                       width=1600,
                       height=800,
                       colormap='PuRd',
                       margin=0,
                       max_words=500,
                       min_word_length=3,
                       max_font_size=300, min_font_size=30,
                       background_color="white").generate(text)

image_colors = ImageColorGenerator(custom_mask)
word_cloud.recolor(color_func=image_colors)

plt.figure(figsize=(20, 20))
plt.imshow(word_cloud, interpolation="gaussian")
plt.axis("off")

plt.savefig('../figures/word_cloud.png')
plt.show()