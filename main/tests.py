# # from django.test import TestCase

# # # Create your tests here.
# # # Import modul unittest dan modul HttpResponse dari Django
# # # Import modul unittest dan modul HttpResponse dari Django
# # # import unittest
# # # from django.http import HttpResponse
# # # from django.test import Client
# # # from .views import show_main

# # # class MainViewTest(unittest.TestCase):

# # #     def setUp(self):
# # #         # Inisialisasi klien untuk mengirim permintaan ke view
# # #         self.client = Client()

# # #     def test_show_main(self):
# # #         # Kirim permintaan GET ke view show_main
# # #         response = self.client.get('/main/')  # Gantilah '/main/' dengan URL yang sesuai

# # #         # Periksa bahwa tanggapan adalah HttpResponse dengan status kode 200 (OK)
# # #         self.assertEqual(response.status_code, 200)

# # #         # Periksa bahwa teks dalam tanggapan mengandung informasi yang sesuai
# # #         self.assertContains(response, "Selamat datang di DJSHOP")
# # #         self.assertContains(response, "<h5>Name: </h5>")
# # #         self.assertContains(response, "<p>Anindya Maulida Widyatmoko</p>")
# # #         self.assertContains(response, "<h5>Class: </h5>")
# # #         self.assertContains(response, "<p>PBP A</p>")
# # #         self.assertContains(response, "<h5> Umur:</h5>")
# # #         self.assertContains(response, "<p>17</p>")

# # # if __name__ == '__main__':
# # #     unittest.main()



# from django.test import TestCase, Client

# # class MainTest(TestCase):
# #     def setUp(self):
# #         self.client = Client()

# #     def test_main_url_exists(self):
# #         response = self.client.get('/main/')
# #         self.assertEqual(response.status_code, 200)

# #     def test_main_uses_main_template(self):
# #         response = self.client.get('/main/')
# #         self.assertTemplateUsed(response, 'main.html')

# #     # def test_main_context_data(self):
# #     #     response = self.client.get('/main/')
# #     #     self.assertEqual(response.status_code, 200)
# #     #     self.assertTemplateUsed(response, 'main.html')
        
# #     #     # Memeriksa apakah data yang benar ditampilkan di template
# #     #     self.assertContains(response, 'Kemeja')
# #     #     self.assertContains(response, 'Kemeja berkualitas tinggi, adem, dan harga terjangkau.')
# #     #     self.assertContains(response, 'Kaos')
# #     #     self.assertContains(response, 'Kaos Berkualitas tinggi dan desain menarik')

# #     def test_main_context_structure(self):
# #         response = self.client.get('/main/')
# #         self.assertEqual(response.status_code, 200)
        
# #         # Memeriksa struktur konteks yang diharapkan
# #         expected_context = {
# #             'Name': 'Anindya Maulida Widyatmoko',
# #             'Kelas': 'PBP A',
# #             'Description' : 'Kami menyediakan produk berkualitas tinggi dengan harga terjangkau sesuai kebutuhan Anda',
# #             'Produk': ['Sweater', 'Kaos', 'Jaket', 'Kemeja'],
# #             'Alamat' : 'Jl. Margonda, Depok',
# #             'Email': 'DJShop@tokobagus.com',
# #             'Telepon' : '012345678'

# #         }

# #         actual_context = response.context['Name']  
# #         self.assertEqual(actual_context, expected_context)

# def test_main_context_data(self):
#     # Test if the context data in the 'show_main' view is correct.
#     response = Client().get('/main/')
#     self.assertEqual(response.context['no'], 1)
#     self.assertEqual(response.context['Produk'], 'Sweater')
#     self.assertEqual(response.context['description'], 'Sweater berkualitas tinggi dan desain menarik.')

from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
