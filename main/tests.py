from django.test import TestCase

# Create your tests here.
# Import modul unittest dan modul HttpResponse dari Django
# Import modul unittest dan modul HttpResponse dari Django
# import unittest
# from django.http import HttpResponse
# from django.test import Client
# from .views import show_main

# class MainViewTest(unittest.TestCase):

#     def setUp(self):
#         # Inisialisasi klien untuk mengirim permintaan ke view
#         self.client = Client()

#     def test_show_main(self):
#         # Kirim permintaan GET ke view show_main
#         response = self.client.get('/main/')  # Gantilah '/main/' dengan URL yang sesuai

#         # Periksa bahwa tanggapan adalah HttpResponse dengan status kode 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Periksa bahwa teks dalam tanggapan mengandung informasi yang sesuai
#         self.assertContains(response, "Selamat datang di DJSHOP")
#         self.assertContains(response, "<h5>Name: </h5>")
#         self.assertContains(response, "<p>Anindya Maulida Widyatmoko</p>")
#         self.assertContains(response, "<h5>Class: </h5>")
#         self.assertContains(response, "<p>PBP A</p>")
#         self.assertContains(response, "<h5> Umur:</h5>")
#         self.assertContains(response, "<p>17</p>")

# if __name__ == '__main__':
#     unittest.main()


from django.test import TestCase
from django.urls import reverse
from .models import models  # Gantilah YourModel dengan model yang sesuai
from .views import show_main  # Gantilah dengan nama view yang sesuai

class YourAppTestCase(TestCase):
    
    def test_show_main_view(self):
        
        response = self.client.get(reverse('show_main'))  # Sesuaikan dengan URL view Anda
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Anindya Maulida Widyatmoko')
        self.assertContains(response, 'PBP A')
        self.assertContains(response, '17')
