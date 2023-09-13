Link Adaptable: https://djshopdea.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 

    1. Membuat Proyek Django Baru:
    Pertama adalah membuat proyek Django baru
    saya membuat proyek Django untuk membangun toko dengan memberi nama proyek ini "DJShop" untuk membuat direktori baru dengan menggunakan perintah berikut di terminal:
    
    django-admin startproject DJSHOP

    2. Membuat Aplikasi "main":
    Setelah proyek dibuat, saya membuat aplikasi dengan nama "main" untuk membuat direktori "main" yang akan berisi kode aplikasi yang akan dibuat dengan menggunakan perintah berikut:
    ```
    python manage.py startapp main
    ```

    3. Melakukan Routing:
    Untuk menjalankan aplikasi "main", kita perlu mengkonfigurasi routing. Untuk itu buka file `urls.py` pada direktori proyek DJSHOP kemudian tambahkan path untuk "main" ke dalam aplikasi seperti ini dengan tujuan untuk mengarahkan permintaan ke dalam "main":
    ```python
    from django.urls import include, path

    urlpatterns = [
        path('', include('main.urls')),
    ]
    ```
    
    4. Membuat Model "Item":
    Selanjutnya, di dalam direktori "main", buka file `models.py` dan definisikan model "Item" dengan atribut yang diberikan seperti kode berikut untuk mewakilkan entitas "Item" dengan atribut yang telah ditentukan:
    ```python
    from django.db import models

    # Create your models here.
    class Product(models.Model):
        Name = models.CharField(max_length=255)
        Kelas = models.CharField(max_length=255)
        Produk = models.IntegerField()
        Alamat = models.TextField()
        Telepon = models.TextField()
        Description = models.TextField()
        Email = models.TextField()
            
    ```
    

    5. Membuat Fungsi pada views.py:
    Di dalam direktori "main", buka file `views.py` dan tambahkan fungsi `show_main` seperti berikut untuk mengembalikan template HTML "main.html" dengan konteks yang telah didefinisikan

    ```python
    from django.shortcuts import render

        # Create your views here.
        def show_main(request):
            context = {
                'Name': 'Anindya Maulida Widyatmoko',
                'Kelas': 'PBP A',
                'Description' : 'Kami menyediakan produk berkualitas tinggi dengan harga terjangkau sesuai kebutuhan Anda',
                'Produk': ['Sweater', 'Kaos', 'Jaket', 'Kemeja'],
                'Alamat' : 'Jl. Margonda, Depok',
                'Email': 'DJShop@tokobagus.com',
                'Telepon' : '012345678'

            }

            return render(request, "main.html", context)
    ```

    6. **Konfigurasi Routing Aplikasi "main"**:
    Selanjutnya buka file `urls.py` di dalam direktori "main" dan saya menambahkan konfigurasi routing untuk memetakan fungsi yang telah dibuat seperti berikut:
    ```python
    from django.urls import path
    from .views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Ini akan menghubungkan URL akar (`''`) ke fungsi `show_main` dalam aplikasi "main".
    
    Setelah langkah-langkah tersebut diselesaikan, kita akan memiliki proyek Django yang berisi aplikasi "main" dengan model "Item", fungsi views, dan konfigurasi routing yang memungkinkan untuk menampilkan informasi yang ada di dalam template HTML "main.html" saat mengakses URL akar proyek yang dibuat. Selanjutnya jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk membuat tabel database yang sesuai dengan model yang akan dibuat.

    7. Membuat Template HTML
    Setelah itu saya membuat template html pada direktori baru di dalam aplikasi main untuk mengatur tampilan halaman web yang ingin saya tampilkan. 

    8. Melakukan Testing Django
    Setelah membuat template HTML saya membuat testing django untuk melakukan test pada atribut yang ada di dalam proyek.

    9. Melakukan Add, Push, dan Commit ke dalam Repositori GitHub
    Setelah semua selesai dilakukan saya melakukan Add, Push, dan Commit ke dalam Repositori GitHub untuk submit pengu


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![gambar no 2](GambarNo2.png)

Aliran data dalam arsitektur Django dimulai dari peramban web pengguna, yang mengirimkan permintaan ke aplikasi web Django. Django Web Application memanfaatkan konfigurasi routing dalam file `urls.py` untuk menentukan tampilan (view) mana yang akan menangani permintaan tersebut. Tampilan, yang didefinisikan dalam file `views.py`, adalah komponen yang mengelola logika bisnis dan memproses data. Tampilan ini berinteraksi dengan model-model yang didefinisikan dalam file `models.py` untuk mengakses, menyimpan, dan memperbarui data dalam database. Selanjutnya, data yang diproses oleh tampilan disiapkan untuk ditampilkan dalam template HTML, dalam kasus ini, `items.html`. Template ini berperan sebagai wadah yang mengatur tampilan akhir yang akan diberikan kepada pengguna. Selama proses ini, data dari model atau konteks dimasukkan ke dalam template dan diatur agar sesuai dengan tampilan yang diinginkan. Selanjutnya, tampilan HTML ini akan dikirimkan kembali kepada pengguna melalui peramban web, sehingga memungkinkan pengguna melihat halaman web dinamis yang dihasilkan oleh Django Web Application. Ini adalah cara Django mengatur aliran data untuk menyajikan halaman web yang responsif dan interaktif kepada pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Virtual environment sangat berguna dalam pengembangan perangkat lunak untuk mengisolasi proyek-proyek serta menghindari konflik antar-paket dan library yang digunakan dalam proyek yang berbeda. Tanpa Virtual environment, setiap proyek dapat berpotensi menggunakan versi yang berbeda dari paket atau library tertentu, yang dapat menyebabkan konflik dan masalah yang sulit diatasi. Dengan Virtual environment ini, setiap proyek memiliki lingkungan kerja yang terisolasi, yang berarti semua dependensinya terisolasi dari proyek-proyek lain. Hal ini untuk memastikan bahwa setiap proyek dapat berjalan dengan lancar tanpa mengganggu yang lain.

    Meskipun penggunaan Virtual environment sangat disarankan, ada beberapa situasi di mana kita mungkin tidak memerlukannya. Misalnya, jika kita mengembangkan sebuah proyek sederhana yang tidak memiliki dependensi tambahan atau jika kita bekerja di lingkungan yang sangat terkontrol di mana versi perangkat lunak dan dependensi sangat konsisten di seluruh proyek, hal ini memungkinkan untuk kita tidak menggunakan Virtual environment. 

    Namun, pada dasarnya setiap proyek menggunakan penggunaan Virtual environment pada proyek sangat penting untuk menjaga kebersihan dan isolasi antar proyek. Hal ini membantu menghindari masalah potensial yang dapat muncul akibat konflik dependensi dan memastikan proyek-proyek Anda berjalan sesuai yang diharapkan. Sebagai hasilnya, sebagian besar praktisi pengembangan perangkat lunak merekomendasikan penggunaan lingkungan virtual dalam proyek-proyek mereka.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

    MVC (Model-View-Controller) memisahkan logika bisnis dari model, sehingga memungkinkan modifikasi pada satu komponen tanpa mempengaruhi yang lain, dan ini dapat mempercepat proses pengembangan. Namun, kekurangannya adalah controller dapat menjadi terlalu kompleks dan sulit dikelola, dan ini dapat meningkatkan kompleksitas keseluruhan aplikasi.

    Sedangkan, MVP (Model-View-Presenter) memungkinkan komponen View dan Presenter dapat digunakan kembali, sehingga kode menjadi lebih mudah dipahami dan dikelola. Namun, hal ini dapat menyebabkan ukuran kode menjadi lebih besar dan hubungan yang terlalu erat antara View dan Presenter.

    Sementara MVVM (Model-View-ViewModel) menghilangkan antarmuka antara View dan Model, serta menjaga hubungan yang tidak terlalu erat antara View dan ViewModel. Ini membantu menghindari masalah yang mungkin muncul dalam pola lainnya. Namun, kekurangannya adalah kode yang ditulis bisa menjadi lebih banyak.

    Jadi, pemilihan antara MVC, MVP, atau MVVM harus dipertimbangkan berdasarkan kebutuhan proyek dan kompleksitasnya. Setiap pola arsitektur memiliki trade-off antara kelebihan dan kekurangan yang perlu diperhatikan oleh pengembang dalam merancang dan mengelola aplikasi mereka.

Referensi:

Surya, B. R. P., Kharisma, A. P., & Yudistira, N. (2020). Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer. Perbandingan Kinerja Pola Perancangan MVC, MVP, Dan MVVM Pada Aplikasi Berbasis Android, Vol. 4, 4089–4095. 

Wijaya, F., Jacobus, A., & Sambul, A. (2023). Jurnal Teknik Elektro dan Komputer. Implementation Of Web Services On University Library Information Systems, Vol. 12, 1–7. 

FIRDAUS RUSLI. (2021). Jurnal Kajian Teknologi Pendidikan. Analisis Kualitas Virtual Environment Pada Low-Cost Virtual Reality Menggunakan Smartphone Dan Virtual Reality Glass, 20–21. 