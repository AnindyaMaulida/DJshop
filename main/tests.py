
from django.test import TestCase, Client

class MainTest(TestCase):
    def setUp(self):
        Client()


    def test_main_context_data(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        
    def test_main_context_structure(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)
        
        # Memeriksa struktur konteks yang diharapkan
        expected_context = {
            'Name': 'Anindya Maulida Widyatmoko',
            'Kelas': 'PBP A',
            'Description': 'Kami menyediakan produk berkualitas tinggi dengan harga terjangkau sesuai kebutuhan Anda',
            'Produk': ['Sweater', 'Kaos', 'Jaket', 'Kemeja'],
            'Alamat': 'Jl. Margonda, Depok',
            'Email': 'DJShop@tokobagus.com',
            'Telepon': '012345678'
        }

        actual_context = response.context  # Get the entire context dictionary
        
        # Compare individual values in the context dictionary
        self.assertEqual(actual_context['Name'], expected_context['Name'])
        self.assertEqual(actual_context['Kelas'], expected_context['Kelas'])
        self.assertEqual(actual_context['Description'], expected_context['Description'])
        self.assertEqual(actual_context['Produk'], expected_context['Produk'])
        self.assertEqual(actual_context['Alamat'], expected_context['Alamat'])
        self.assertEqual(actual_context['Email'], expected_context['Email'])
        self.assertEqual(actual_context['Telepon'], expected_context['Telepon'])

