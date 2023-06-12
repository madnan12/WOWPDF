from django.contrib import admin
from django.urls import path
from fileapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('merge_pdf/', pdf_to_word),
    path('split_pdf/', split_pdf),
    path('compress_pdf/', pdf_to_word),
    path('pdf_to_word/', pdf_to_word),
    path('pdf_to_excel_converter/', pdf_to_word),
    path('word_to_pdf_converter/', pdf_to_word),
    path('excel_to_pdf/', pdf_to_word),
    path('pdf/edit/', pdf_to_word),
    path('pdf_to_jpg/', pdf_to_word),
    path('pdf_to_png/', pdf_to_word),
    path('jpg_to_pdf/', pdf_to_word),
    path('pdf_rotation/', pdf_to_word),
    path('html_to_pdf/', pdf_to_word),
    path('arrange_pdf/', pdf_to_word),
    path('add_watermark_to_pdf/', pdf_to_word),
    path('scan_pdf/', pdf_to_word),
    path('remove_pages/', pdf_to_word),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)