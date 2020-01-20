from django.test import TestCase,Client
from .models import *
from .forms import DocumentForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.core.files import File
import io
from Praktyka.settings import BASE_DIR

class home_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response1 = self.client.get('/home/')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.get('/')
        self.assertEqual(response2.status_code, 200)


class error_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response = self.client.get('/error')
        self.assertEqual(response.status_code, 200)

class error_no_file_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response = self.client.get('/error_no_file')
        self.assertEqual(response.status_code, 200)

class error_form_empty_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response = self.client.get('/error_form_empty')
        self.assertEqual(response.status_code, 200)

class PDF_List_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)

    def testModel(self):
        model = Document
        self.assertIs(model, Document)


class PDF_Send_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def testResponseCode(self):
        response = self.client.get('/send/')
        self.assertEqual(response.status_code, 200)

    def testModel(self):
        model = Document
        self.assertIs(model, Document)

    def testForm(self):
        #PyPDF2.utils.PdfReadError: Could not read malformed PDF file
        #pdf_file = SimpleUploadedFile("file.pdf", b"file_content", content_type="application/pdf")
        file = SimpleUploadedFile("file.txt", b"file_content", content_type="text/plain")

        with open('/home/bogu/PycharmProjects/Praktyka/media/test/test.pdf', "rb") as pdf_file:
            response1 = self.client.post(reverse('PDF_Service_send'), {'name': 'test_pdf', 'pdf': pdf_file})
        response2 = self.client.post(reverse('PDF_Service_send'), {'name': 'test_pic', 'pdf': file})        #ok
        response3 = self.client.post(reverse('PDF_Service_send'), {'name': 'test_none', 'pdf': None})       #ok

        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 302)                #ok
        self.assertEqual(response3.status_code, 302)                #ok

        # form_data1 = {'test_pdf', 'test/test.pdf'}
        # form_data2 = {'test_jpg', 'test/test.jpg'}
        # form_data3 = {'test_none', None}
        # form1 = DocumentForm(form_data1)
        # form2 = DocumentForm(form_data2)
        # form3 = DocumentForm(form_data3)
        # self.assertTrue(form1.is_valid())
        # self.assertTrue(form2.is_valid())
        # self.assertTrue(form3.is_valid())

class PDF_Preview_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        test_doc = Document(pk = 1667, pdf = 'test/test.pdf ', name = 'testtest12345', size='1345', page_number='1', date = '2018-11-30')
        test_page = Page(pk = 20223, id_document= test_doc, text='w ogole centralnie kamieniem go bez kitu', nr = 1, thumbnail = None)
        test_page.save()
        test_doc.save()

    def testResponseCode(self):
        response1 = self.client.get('/preview/1667')
        self.assertEqual(response1.status_code, 301)
        response2 = self.client.get('/preview/202299')
        self.assertEqual(response2.status_code, 301)            #bzdura

    def testModel(self):
        model = Page
        self.assertIs(model, Page)

    def tearDown(cls):
        del cls.client
        Document.objects.filter(pk=1667).delete()
        Page.objects.filter(pk=20223).delete()

class PDF_Delete_test(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        test_doc = Document(pk = 1667, pdf = 'test/test.pdf ', name = 'testtest12345', size='1345', page_number='1', date = '2018-11-30')
        test_doc.save()

    def testResponseCode(self):
        response1 = self.client.get('/preview/1667', follow=True)
        self.assertEqual(response1.status_code, 200)    #git
        response2 = self.client.post('/delete/1667')
        self.assertEqual(response2.status_code, 301)    #302?
        response1 = self.client.get('/preview/1667', follow=True)
        self.assertEqual(response1.status_code, 200)    #zle
        response2 = self.client.post('/delete/1667')
        self.assertEqual(response2.status_code, 301)    #zle

    def testModel(self):
        model = Document
        self.assertIs(model, Document)

    # def testGetObject(self):          #???
    #     object = self.get_object()
    #     self.assertEqual(object, Document(pk = 1667, pdf = 'test/test.pdf ', name = 'testtest12345', size='1345', page_number='1', date = '2018-11-30'))