from django.views.generic import ListView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import DocumentForm
from .models import *
import logging
from pdf2image import *

logg = logging.getLogger('view_logger')

def home(request):
    logg.info('home_view: view called')
    return render(request, 'PDF_Service/home.html')

def error(request):
    logg.info('error_view: view called')
    return render(request, 'PDF_Service/error.html')

def error_no_file(request):
    logg.info('error_view: view called')
    return render(request, 'PDF_Service/error_no_file.html')

def error_form_empty(request):
    logg.info('error_view_form_empty: view called')
    return render(request, 'PDF_Service/error_form_empty.html')

class PDF_List(ListView):
    model = Document
    context_object_name = 'PDF_Service_list'
    template_name = 'PDF_Service/list.html'
    logg.info('PDF_List: view called')

    def get_queryset(self):
        logg.info('PDF_List: get_queryset successful')
        return Document.objects.all()

class PDF_Send(CreateView):
    model = Document
    #fields = ['name', 'page_number', 'date']
    context_object_name = 'PDF_Service_send'
    logg.info('PDF_Send: view called')
    template_name = 'PDF_Service/send.html'
    form_class = DocumentForm
    success_url = reverse_lazy('PDF_Service_list')

    def form_valid(self, form):
        if form:
            logg.info('PDF_Send: form_valid is successful. Form is not empty')
            if form.instance.pdf:
                logg.info('PDF_Send: form_valid is successful. Form includes file')
                if os.path.splitext(str(form.instance.pdf))[-1].lower() == ".pdf":
                    logg.info('PDF_Send: form_valid is successful. File is a .pdf file')
                    path = os.path.abspath(str(form.instance.pdf)).replace("views.py", "")
                    path = os.path.abspath(str(form.instance.pdf)).replace("Praktyka/", "Praktyka/media/pdfs/files/")
                    pattern = re.compile(r'\s+')
                    path = re.sub(pattern, '_', path)

                    pdf = form.instance.pdf
                    pdf.seek(0, os.SEEK_END)
                    size = pdf.tell()
                    form.instance.size = size
                    logg.info('PDF_Send: File size calculated')
                    reader = pdf2.PdfFileReader(pdf)
                    pageno = reader.numPages
                    form.instance.page_number = pageno
                    logg.info('PDF_Send: Page count calculated')
                    form.save()
                    pages = pdf2image.convert_from_path(str(path), 500)
                    logg.info('PDF_Send: .pdf file converted to pages')
                    i = 0
                    for page in pages:
                        pagetemp = reader.getPage(i)
                        pagetemp = pagetemp.extractText()
                        #pagetemp = beautifulsoup4(pagetemp, 'lxml')
                        #filename = path.split('/')
                        #filename = filename[-1]
                        #image = page.save('/home/bogu/PycharmProjects/Praktyka/media/pdfs/thumbnails/out%.jpg' %i, 'JPEG')
                        Page(id_document=form.instance, text=pagetemp, nr=i+1, thumbnail = None).save()
                        i += 1
                        logg.info('PDF_Send: page converted')
                    logg.info('PDF_Send: .pdf file converted')
                    return super(PDF_Send, self).form_valid(form)
                else:
                    logg.error('PDF_Send: sent file is not a .pdf file')
                    return redirect('PDF_Service_error')
            else:
                logg.error('PDF_Send: file not sent')
                return redirect('PDF_Service_error_no_file')
        else:
            logg.error('PDF_Send: form invalid')
            return redirect('PDF_Service_error_form_empty')

class PDF_Preview(ListView):
    model = Page
    context_object_name = 'PDF_Service_preview'
    template_name = 'PDF_Service/preview.html'
    logg.info('PDF_Preview: view called')

    def get_queryset(self):
        doc = Document.objects.get(id=self.kwargs['pk'])
        page = doc.pages.all()
        logg.info('PDF_Preview: get_queryset successful.')
        return page

class PDF_Delete(DeleteView):
    model = Document
    context_object_name = 'PDF_Service_delete'
    template_name = 'PDF_Service/delete.html'
    logg.info('PDF_Delete: view called')
    success_url = reverse_lazy('PDF_Service_list')

    def get_object(self, queryset=None):
        obj = super(PDF_Delete, self).get_object()
        logg.info('PDF_Delete: get_object successful, document deleted')
        return obj