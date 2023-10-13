Link Adaptable: https://djshopdea.adaptable.app/main/

=================Tugas 2================================

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


=================Tugas 3================================

1. Apa perbedaan antara form POST dan form GET dalam Django? Form POST dan form
    GET dalam Django digunakan untuk mengirimkan data dari form HTML ke server. Namun terdapat perbedaan utama antara keduanya adalah cara pengiriman datanya. Form POST mengirimkan data sebagai bagian dari body request, sementara form GET mengirimkan data sebagai query string di URL. kemudian nilai variabel pada form POST tidak ditampilkan pada URL, sedangkan pada form GET nilai variabel ditampilkan pada URL sehingga user dapat memasukkan nilai pada variabel baru. Untuk mengirim data, form POST sering digunakan untuk mengirim data yang sensitif seperti password atau email, sedangkan form GET cocok untuk mengambil data yang tidak sensitif seperti hasil pencarian atau filter. Selain itu, form POST memiliki batasan ukuran data yang lebih besar daripada form GET dimana form GET dibatasi panjang string sampai 2047 karakter karena data dikirim melalui body request, sementara form GET memiliki batasan ukuran data yang lebih kecil karena data dikirim melalui URL.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman sehingga dapat digunakan oleh bahasa pemrograman lain seperti PHP, Python, C++, dan Ruby. JSON dapat menyimpan data dalam bentuk array dan menjadikan transfer data menjadi lebih mudah. Sintaks yang lebih ringan dan berukuran lebih kecil, serta lebih cepat dalam parsing data di sisi server.

    XML adalah bahasa markah yang menyediakan aturan untuk menentukan data apa pun. XML menggunakan tanda untuk membedakan antara atribut data dan data aktual. XML lebih cocok untuk struktur dokumen kompleks yang memerlukan validasi dan pemrosesan yang kompleks.

    HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membangun struktur dan menampilkan konten pada halaman web. Namun, HTML sendiri tidak digunakan secara khusus untuk pengiriman data antar server dan klien. Proses pengiriman data pada halaman web umumnya menggunakan protokol HTTP (Hypertext Transfer Protocol) dengan metode seperti POST atau GET seperti pada penjelasan no 1. 

    Oleh karena itu, dalam pengiriman data JSON menghasilkan ukuran data yang lebih kecil dibandingkan dengan XML sehingga lebih cepat dalam proses transfer data. Namun, XML lebih cocok untuk struktur dokumen kompleks yang memerlukan validasi dan pemrosesan yang kompleks. Sedangkan HTML lebih fokus pada tugas menampilkan data pada halaman web dan bukan digunakan untuk pertukaran data antar aplikasi.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena sintaks JSON yang lebih sederhana dan ringkas dibandingkan XML. JSON juga memiliki dukungan luas dari browser modern dan sebagian besar framework JavaScript, serta didukung oleh banyak teknologi backend seperti PHP, Python, dan Ruby. Selain itu, JSON dapat merepresentasikan struktur data yang lebih kompleks dan fleksibel, seperti objek dalam objek atau array dari objek. Kelebihan-kelebihan ini membuat JSON menjadi format yang efisien dan sering digunakan dalam pertukaran data di antara aplikasi web.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    1. **Mengatur Routing**
    pada step pertama saya mengaktifkan env terlebih dahulu, karena saya menggunakan mac saya menggunakan  ` source env/bin/activate ` .

    2. **membuat kerangka views**
    selanjutnya, saya membuat folder template kemudian membuat file bernama base.html sebagai base untuk halaman web lainnya di dalam proyek. 
    
    ```html
     {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```

    pada fase ini saya mengubah beberapa kode pada main.html yang sebelumnya dibuat pada tugas sebelumnya
    ```html
    {% extends 'base.html' %}

    {% block content %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DJSHOP</title>
        <link rel="stylesheet" href="style.css"> <!-- Hubungkan dengan file CSS Anda -->
        <style>
            .banner > .container > h2{
                display: flex;
                justify-content: center;
            }
        </style>
    </head>
    <body>

        <div class="banner">
            <div class="container">
                <h2>Selamat datang di DJSHOP!</h2>
            </div>
        </div>

        <section class="featured-products">
            <div class="container">
                <h2>Description</h2>
                <p>{{ Description }}</p>
                <h2>Produk Unggulan</h2>
                <ul>
                    {% for product in Produk %}
                        <li>{{ product }}</li>
                    {% endfor %}
                </ul>
            </div>
        </section>
        

        <section class="contact">
            <div class="container">
                <h2>Hubungi Kami</h2>
                <p>Jika Anda memiliki pertanyaan atau masukan, jangan ragu untuk menghubungi kami melalui:</p>
                <address>
                    <p>Alamat: {{ Alamat }}</p>
                    <p>Email: {{ Email }}</p>
                    <p>Telepon: {{ Telepon }}</p>
                </address>
            </div>
        </section>

        <footer>
            <div class="container">
                <h5>Name: {{ Name }}</h5>
                <h5>Class: {{ Kelas }}</h5>
            </div>
        </footer>
    </body>
    </html>
    ```

    3. **Membuat Form Input Data dan Menampilkan Data Produk Pada HTML**
    pada step ini saya membuat file forms.py di direktori main dan mengubah fields sesuai yang saya mau seperti berikut:
    saya menambahkan Name, Jumlah, dan Description
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["Name", "Jumlah", "Description"]
    ```


    kemudian pada step ini, saya juga menambahkan kode pada main.html untuk menambahkan product dan menghitung setiap jumlah product yang saya jumlahkan
    ```html
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Jumlah</th>
                <th>Description</th>
                <th>Date Added</th>
            </tr>
        </thead>
        <tbody>
            {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
            {% for product in products %}
                <tr>
                    <td>{{ product.Name }}</td>
                    <td>{{ product.Jumlah }}</td>
                    <td>{{ product.Description }}</td>
                    <td>{{ product.date_added }}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    

    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    <p>Kamu telah menambahkan {{ products | length }} produk.</p>
    ```
    4. **Mengembalikkan data dalam bentuk XML dan JSON**
    setelah itu, membuat fungsi show_json, show_xml serta fungsi json dan xml yang menggunakan id kemudian sesuaikan import yang dibutuhkan seperti pada tutorial.

    5. **Penggunaan Postman** 
    Setelah step diatas berhasil dijalankan pada server kemudian test menjalankan server di postman dengan method GET

    6. **Push**
    jika semua sudah selesai, tampilan web sudah bagus dan berhasil, serta menambah produk sudah berhasil ditambahkan maka kita bisa push ke github 
    `
    git add .
    git commit -m "<pesan_commit>"
    git push -u origin main
    `



![gambar HTML](Tampilan_HTML.png)
![gambar XML](Tampilan_XML.png)
![gambar JSON](Tampilan_JSON.png)
![gambar XML by ID](Tampilan_XML_ID.png)
![gambar JSON by ID](Tampilan_JSON_ID.png)


referensi: Ramadhan, R. (2016, April 29). Penjelasan Singkat tentang POST & GET Django. Gist. https://gist.github.com/rririanto/442f0590578ca3f8648aeba1e25f8762
M.Kom, S. (2016). DATA COMMUNICATION ANALYSIS WITH XML AND JSON ON WEBSERVICE. Computer Engineering, Science and System Journal, 1(2), 1–6. https://doi.org/10.24114/cess.v1i2.4066 


=================Tugas 4================================

1.  Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    Django UserCreationForm adalah form bawaan Django untuk membuat user baru dengan username dan password. Form ini memiliki validasi dan metode save() yang memudahkan proses pendaftaran. Form ini juga dapat dikustomisasi dengan menambahkan atau mengubah field sesuai kebutuhan. Namun, form ini juga memiliki beberapa kekurangan, seperti tidak cocok untuk user yang lebih kompleks, tidak memiliki fitur email konfirmasi atau lupa password, dan mungkin tidak sesuai dengan standar atau kebiasaan pengguna di negara atau budaya tertentu.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Authentication adalah proses verifikasi identitas pengguna yang ingin mengakses sistem atau layanan. Tujuan utama dari authentication adalah untuk memastikan bahwa entitas tersebut adalah benar-benar orang, perangkat, atau sistem yang mereka klaim sebagai identitasnya. Dalam proses authentication, pengguna akan diminta untuk memasukkan informasi seperti username dan password, token khusus, atau menggunakan autentikasi biometrik seperti sidik jari atau pemindaian wajah1. Dengan menggunakan mekanisme authentication yang tepat, organisasi dapat memastikan bahwa hanya pengguna yang memiliki akses yang valid yang dapat mengakses informasi sensitif atau melakukan tindakan yang mempengaruhi integritas sistem.
    
    Authorization adalah proses memberikan hak akses kepada pengguna setelah berhasil melewati tahap authentication1. etelah pengguna atau entitas terotentikasi, sistem perlu memutuskan apa yang diizinkan atau dilarang untuk diakses oleh entitas tersebut. Dalam hal ini, authorization berfungsi untuk mengendalikan tingkat akses pengguna ke berbagai bagian sistem atau data. Misalnya, admin memiliki akses lebih tinggi dibandingkan dengan pengguna biasa.
    
    Perbedaan utama antara authentication dan authorization adalah bahwa authentication berkaitan dengan proses verifikasi identitas pengguna, sementara authorization berkaitan dengan pemberian hak akses kepada pengguna2. Dengan menggunakan mekanisme authentication dan authorization yang tepat, organisasi dapat menjaga keamanan dan mengendalikan tingkat akses pengguna dengan efektif. Keduanya sangat penting untuk mengamankan data pengguna dan sistem dengan membatasi akses hanya pada pengguna yang sah dan berwenang. Selain itu, mempermudah developer dalam menerapkan fungsionalitas login, logout, registrasi, dan reset password dengan menggunakan alat bawaan Django atau pustaka eksternal.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies diciptakan untuk memungkinkan sebuah situs web untuk melacak dan mengingat aktivitas yang telah dilakukan pengguna pada kunjungan sebelumnya, sehingga situs dapat menyediakan pengalaman yang dipersonalisasi dan lebih sesuai dengan preferensi individu saat pengguna kembali mengunjungi situs tersebut. 
    
    Saat pengguna mengunjungi situs web yang menggunakan Django, sebuah cookie ID sesi yang berisi string acak unik ditempatkan di browser pengguna dan terkirim kembali ke server dalam setiap interaksi. Semua informasi sesi disimpan aman di sisi server, baik di database, filesystem, atau cache sesuai dengan konfigurasi sistem. Django mengaitkan cookie ID sesi dengan data sesi menggunakan sebuah dictionary bernama SESSION_ENGINE. Ketika sesi berakhir, baik karena pengguna menutup browser atau mencapai batas waktu sesi, Django menghapus cookie ID sesi dan data sesi terkait. Hal ini meningkatkan keamanan dan privasi data sesi karena hanya ID sesi yang disimpan di browser pengguna. Selain itu, Django menyediakan kenyamanan bagi pengembang dengan objek request.session, memudahkan penyimpanan dan pengambilan data sesi. Terakhir, penggunaan cookies membantu mempercepat kinerja situs web dengan mengirimkan hanya cookie ID sesi yang ukurannya lebih kecil, mengoptimalkan lalu lintas data dan meningkatkan efisiensi keseluruhan situs."
    

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies dalam pengembangan web membawa aspek keamanan, privasi, dan fungsionalitas yang perlu dipertimbangkan. Meskipun pada umumnya cookies tidak membahayakan dan tidak membawa virus atau malware ke perangkat pengguna, mereka membantu pengguna dalam mengingat kredensial login, preferensi, atau riwayat pencarian di sebuah website. Namun, terdapat risiko potensial yang harus diwaspadai terkait dengan cookies. Pihak ketiga seperti pengiklan atau pelacak dapat menggunakan cookies untuk mengumpulkan dan menganalisis data perilaku pengguna di internet, menimbulkan masalah privasi dan etika. Selain itu, cookies juga dapat dicuri atau dipalsukan oleh pihak yang tidak berwenang, mengakibatkan pencurian identitas, penipuan, atau serangan siber. 
    
    Maka dari itu, penggunaan cookies dalam pengembangan web harus bijak dan bertanggung jawab. Hal-hal yang perlu dilakukan mencakup memberikan informasi kepada pengguna mengenai kebijakan dan tujuan penggunaan cookies di website serta meminta persetujuan mereka sebelum mengirimkan cookies ke browser mereka. Disarankan juga untuk menggunakan cookies sesi yang otomatis terhapus ketika browser ditutup, menghindari cookies pihak ketiga yang tidak relevan atau tidak terpercaya, serta mengenkripsi dan melindungi cookies dengan protokol keamanan yang sesuai, seperti HTTPS atau SSL. Selain itu, membersihkan cookies yang tidak diperlukan atau sudah kedaluwarsa secara berkala juga dianjurkan.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. **Menjalankan virtual environment**
    sebelum memulai, menjalankan virtual environment terlebih dahulu
    2. **Membuat form Registrasi**
    saya menambahkan fungsi registrasi pada view.py untuk mengatur apabila pengguna ingin registrasi atau membuat akun jika belum mempunyai akun dengan menambahkan kode seperti berikut:
    ```python
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```

    kemudian setelah membuat fungsi di views saya membuat file html bernama register.html untuk menampilkan tampilan registrasi di website dengan menambahkan css untuk mengatur tampilan pada website nya agar sesuai dengan yang saya inginkan. 

    setelah membuat register.html, sesuaikan url serta import apa saja yang dibutuhkan untuk fungsi registrasi tersebut pada file urls.py.

    3. **Membuat Fungsi Login**
    Setelah membuat Registrasi, saya membuat fungsi login agar pengguna dapat login dengan akun yang mereka sudah registrasi sebelumnya. saya membuat fungsi login pada file views.py seperti berikut:
    ```python
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```
    dan saya juga menambahkan import login. Setelah itu, sama seperti membuat register, setelah saya membuat fungsi login pada views.py saya membuat file html untuk login bernama login.html pada main seperti berikut:
    ```html
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}

    <div class = "login">

        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Username: </td>
                    <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                </tr>
                        
                <tr>
                    <td>Password: </td>
                    <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                </tr>

                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login"></td>
                </tr>
            </table>
        </form>

        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}     
            
        Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

    </div>

    {% endblock content %} 
    ``` 

    saya juga menambahkan css untuk mempercantik tampilan pada web nya. kemudian menyesuaikan url serta import apa saja yang dibutuhkan untuk fungsi login tersebut pada file urls.py.

    4. **Membuat Fungsi Logout**
    sama seperti fungsi register dan login, pada fungsi logout ini saya menambahkan potongan kode berikut ke views.py
    ```python
    def logout_user(request):
    logout(request)
    return redirect('main:login')
    ``` 
    serta menambahkan import logout. namun pada fungsi Logout ini saya membuat fungsi logout pada html untuk tampilan web nya di main.html seperti berikut:

    ```html
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
    ```
    Setelah itu saya menyesuaikan url serta import apa saja yang dibutuhkan untuk fungsi registrasi tersebut pada file urls.py.

    5. **MMengatur last_login**
    Untuk mengetes apakah fungsi registrasi, login, dan logout sudah berhasil apa belum. saya mencobanya dengan menjalankan server di local host. Setelah berhasil dijalankan saya menambahkan kode berikut pada fungsi show_main:
    ```
    'last_login': request.COOKIES['last_login'],
    ```

    menambahkan kode berikut pada fungsi logout_user
    ```
    response.delete_cookie('last_login')
    ```
    dan pada view.py saya menambahkan kode berikut untuk mengecek kapan terakhir kali pengguna login 
    ```
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```

    yang terakhir untuk menampilan pada web saya menambahkan kode berikut di main.html
    ```
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```

    6. **Menghubungkan Model Product dengan User**
    untuk menghubungkan model product dengan user saya menambahkan kode berikut di models.py dan menambahkan import user
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

    setelah itu saya mengubah fungsi create_product menjadi seperti berikut:
    ```
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
    ```
    serta saya menambahkan kode berikut untuk menampilkan user mana yang sedang login di bagian context show_main
    ```
    'name': request.user.username,
    ```

    7. **Menjalankan server untuk tampilan web**
    setelah semua sudah dilakukan saya makemigration dulu untuk pengaplikasian setelah saya melakukan perubahan di file models.py    kemudian migrate bakal menerapkan perubahan data tersebut ke basis data
    setelah selesai saya melakukan 
    ```
    gitt add.
    git commit -m "<..>"
    git push origin main
    ```
    untuk push ke github. 


referensi:
https://www.javatpoint.com/django-usercreationform
https://glints.com/id/lowongan/cookies-adalah/
https://alan.co.id/mengenal-apa-itu-django-framework-python-yang-populer/
https://mediaindonesia.com/weekend/504274/amankah-mengklik-izinkan-cookies-di-setiap-web-yang-anda-satroni


=================Tugas 5================================
1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    Terdapat 3 jenis selector yaitu Element Selector, ID Selector, dan Class Selector.
    a. Element Selector memberikan gaya pada elemen seperti yang saya gunakan pada kode berikut untuk memberikan beberapa perintah seperti warna, padding, width dan lain lain:
    ``` css
    button {
            padding: 10px 20px;
            background-color: #334f58; 
            color: white; 
            border: none;
            cursor: pointer;
        }
    ```
    b. ID Selector adalah selector CSS yang memilih elemen HTML sesuai dengan nilai atribut ID yang dimilikinya. Atribut ID harus unik dalam suatu halaman web, untuk menerapkan gaya pada css. contoh :

    ```html
    <div class="container">
    ```

    ```css
    .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
    ```

    c. Class Selector adalah selector CSS yang memilih elemen HTML berdasarkan nilai atribut class yang ada pada elemen tersebut untuk mengelompokkan elemen yang mempunyai sifat yang sama. contoh:
    ```html
    <div class="banner">
    ```

    ```css
     .banner {
            background: url('banner-image.jpg') no-repeat center center;
            background-size: cover;
            color: rgb(0, 0, 0);
            text-align: center;
        }
    ```

2. Jelaskan HTML5 Tag yang kamu ketahui.
    <title> adalah elemen yang digunakan untuk menentukan judul dokumen HTML
    <link> adalah elemen yang digunakan untuk memasukkan dokumen HTML dari eksternal, seperti file CSS, ikon favicon, font web, dan lain-lain
    <header> adalah elemen yang digunakan untuk membuat sebuah header untuk dokumen atau bagian HTML.
    <tr> elemen digunakan untuk mengelompokkan dan mendefinisikan baris-baris dalam sebuah tabel HTML.
    <body> elemen yang digunakan sebagai kontainer untuk seluruh konten yang ingin ditampilkan dalam halaman web. Semua elemen yang tampak pada halaman web, seperti teks, gambar, tautan, dan lainnya, ditempatkan di dalam elemen 
    <section>, masing-masing mengelompokkan konten terkait dalam bagian-bagian yang lebih terdefinisi sesuai dengan tema atau subjeknya.

3. Jelaskan perbedaan antara margin dan padding.
    Margin adalah jarak luar elemen, mengatur ruang antara elemen dengan elemen lainnya. Properti margin digunakan untuk menentukan jarak di setiap sisi elemen (atas, kanan, bawah, kiri). Sedangkan, padding adalah jarak di dalam elemen, mengatur ruang antara batas elemen dan kontennya. Properti padding digunakan untuk menentukan jarak di setiap sisi elemen (atas, kanan, bawah, kiri). Perbedaan utama adalah margin tidak termasuk dalam ukuran elemen, sementara padding termasuk. Jadi, jika tambah margin, ukuran elemen tetap, namun jaraknya dengan elemen lain bertambah. Namun, jika tambah padding, ukuran elemen bertambah sesuai dengan padding yang ditambahkan.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    Dalam Tailwind, kita dapat membuat design antarmuka dengan cara menambahkan kelas-kelas ke elemen HTML. Kita juga memiliki kontrol penuh atas design yang kita inginkan sehingga memiliki design yang unik dibandingkan yang lain. Tailwind memerlukan penulisan kelas yang lebih banyak sehingga memungkinkan kita untuk menghindari overhead dari penulisan kode CSS tambahan yang sering tidak digunakan.

    Dalam Bootstrap, kita dapat membuat antarmuka secara cepat dengan memanfaatkan komponen yang ada. namun, bootstrap memiliki kekurangan yaitu memiliki kustomisasi yang lebih terbatas dan potensi tampilan web yang sama dengan banyak situs web lain yang juga menggunakan Bootstrap.

    Jadi kita dapat menggunakan tailwind jika ingin fleksibilitas desain yang lebih besar dan ingin membangun antarmuka kustom sesuai kebutuhan tanpa harus menuliskan CSS tambahan. Sedangkan, bootstrap cocok untuk proyek yang membutuhkan cepat dan mudah, dengan banyak komponen bawaan.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pada Tugas kali ini saya menambahkan beberapa, step-step yang saya lakukan 
1. **Menambahkan Fitur Edit Product**
saya menambahkan fungsi edit_product pada views.py untuk bisa mengedit product yang sudah di tambahkan dengan kode berikut:
```python
def edit_product(request, id):
        # Get product berdasarkan ID
        product = Product.objects.get(pk = id)

        # Set product sebagai instance dari form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context) 
```

setelah itu saya membuat file html baru dengan nama edit_product.html dengan menambahkan kode berikut:
```html
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

setelah membuat file html tambahkan import edit_product pada file urls.py dan tambahkan path dengan kode berikut:
```python
path('edit-product/<int:id>', edit_product name='edit_product'),
```

serta pada main.html saya menambahkan kode berikut:
```html
<td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
```

2.  **Menambahkan Fitur Delete Product**
Pada penambahan fitur ini sebenarnya saya sudah menambahkan pada tugas sebelumnya, tahapannya sama seperti edit_product namun bedanya ini delet product

3. **Menambahkan Halaman Pricelist.html**
Dalam Custome halaman web saya menambahkan halaman Pricelist dengan menampilkan harga dan barang. 
pertama saya membuat file pricelist.html dengan menambahkan kode untuk menambahkan isi gambar, pricelist dan lain lain. 
setelah itu saya menambahkan kode berikut pada views.py:
```python
def pricelist(request):
    return render(request, 'pricelist.html')
```
kemudian pada file urls.py saya menambahkan path dengan kode berikut dan menambahan import pricelist
```python
path('pricelist.html', pricelist, name='pricelist_html'),
```

Namun pada halama pricelist saya belum menyelesaikan tahapan add to cart jadi masih belum berfungsii

4. **Membuat css**
saya mengedit tampilan web menggunakan css di main.html, login.html, pricelist.html, dan register.html 

saya menyesuaikan tampilan web sesuai dengan yang saya inginkan menggunakan css

5. **Memberikan warna yang berbeda baris terakhir dari item**
dalam tahap ini saya memberikan warna yang berbeda pada item terakhir yang ditambahkan jika saya menambahkan product baru untuk menjadi pembeda bahwa item tersebut baru ditambahkan. 
Saya menambahkan kode di main.html dengan kode berikut:
```html
 <tr  {% if forloop.last %}class="latest-item" 
```
sehingga tampilan table pada main.html saya sebagai berikut:

```html
      {% for product in products %}
                <tr  {% if forloop.last %}class="latest-item" style = "background-color: #71c1db"{% endif %}>
                    <td>{{ product.Name }}</td>
                    <td>
                        <div class="product-actions">
                            <form method="POST" action="{% url 'main:reduce_amount' product.id %}">
                                {% csrf_token %}
                                <button type="submit">-</button>
                            </form>
                            {{ product.Jumlah }}
                            
                            <form method="POST" action="{% url 'main:add_amount' product.id %}">
                                {% csrf_token %}
                                <button type="submit">+</button>
                            </form>
                        </div>

                        
                    </td>
                    <td>{{ product.Description }}</td>
                    <td>{{ product.date_added }}</td>
                    <td>
                        <a href="{% url 'main:delete_product' product.pk %}">
                            <button>
                                Delete
                            </button>
                        </a>
                        <a href="{% url 'main:edit_product' product.pk %}">
                            <button>
                                Edit
                            </button>
                        </a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>

```
    
setelah semua tahapan selesai saya melakukan add, commit, dan push pada github. 


=================Tugas 6================================
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Perbedaan antara synchronous dan asynchronous programming terletak pada cara eksekusi tugas. Synchronous bersifat blocking dan linear, yaitu satu tugas harus menunggu yang sebelumnya selesai sebelum merespons input atau kejadian lain. Sehingga tidak efisien dalam memproses tugas-tugas I/O-intensif karena harus menunggu I/O selesai. Asynchronous bersifat non-blocking, tugas-tugas dapat berjalan bersamaan dan  program dapat merespons kejadian yang terjadi saat tugas lain sedang berjalan. Sehingga efisien dalam memproses tugas-tugas I/O-intensif karena dapat melakukan tugas lain selama menunggu I/O.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven merupakan alur ketika mengeksekusi program tidak ditentukan secara linear, melainkan berdasarkan kejadian atau peristiwa (events) yang terjadi. Program akan merespons kejadian-kejadian ini dengan menjalankan tindakan atau fungsi tertentu yang telah ditetapkan sebelumnya. Dalam paradigma ini, program tidak menunggu tindakan selesai sebelum melanjutkan ke tindakan berikutnya. Sebaliknya, program akan merespons kejadian yang terjadi, seperti klik mouse, input pengguna, atau data yang tiba dari jaringan. Hal ini memungkinkan program untuk tetap responsif terhadap interaksi pengguna atau perubahan keadaan sistem.

Contoh penerapannya pada tugas ini adalah saat pengguna mengklik tombol "Add Product" atau tombol "Tambah" pada modal form untuk menambahkan produk baru. Saat tombol ini diklik, event click terpicu, dan fungsi yang telah ditetapkan sebelumnya (seperti addProduct() pada kode JavaScript) akan dijalankan secara otomatis untuk memproses penambahan produk.

3. Jelaskan penerapan asynchronous programming pada AJAX.
penerapan asynchronous programming pada AJAX di mana kode JavaScript dapat mengirim permintaan (request) ke server tanpa harus menunggu respon dari server. Hal ni bertujuan agar halaman web tetap responsif dan dapat diakses oleh pengguna sementara data atau tindakan diproses di latar belakang.

sebagi contoh saya menerapkan asynchronous programming pada AJAX pada fungsi getProducts() dan refreshProducts(), Anda menggunakan await untuk menunggu hasil dari operasi asynchronous seperti fetch, yang membuat kode ini bekerja secara asynchronous.
```JavaScript
 async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
    async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Jumlah</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.jumlah}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }
```
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Kedua teknologi, Fetch API dan jQuery, digunakan untuk melakukan AJAX (Asynchronous JavaScript and XML) requests dalam pengembangan web. F AJAX dan Fetch API merupakan dua teknologi yang digunakan untuk melakukan permintaan asinkron ke server web tanpa harus memuat ulang halaman. Dari segi kompatibilitas dan berat, Fetch API dapat diakses di semua peramban modern dan memiliki ukuran file yang lebih ringan daripada jQuery. Meskipun jQuery AJAX juga kompatibel dengan hampir semua peramban, ukuran file jQuery yang lebih besar dapat mempengaruhi waktu pemuatan halaman jika tidak dikelola dengan baik. Kedua teknologi memiliki kemampuan untuk melakukan request HTTP dan memungkinkan pengiriman serta penerimaan data dalam berbagai format seperti JSON, XML, dan lainnya. Fetch API menjadi pilihan yang sesuai untuk proyek-proyek modern yang berfokus pada performa dan ingin memanfaatkan standar terbaru dalam JavaScript. Di sisi lain, jQuery AJAX masih banyak digunakan terutama dalam proyek-proyek yang sudah menggunakan jQuery secara luas atau memerlukan integrasi dengan library jQuery lainnya. Masing-masing memiliki dukungan yang kuat dari komunitas web dengan Fetch API sebagai bagian dari standar resmi dari W3C dan jQuery AJAX dengan dukungan komunitas yang besar serta dokumentasi dan tutorial yang melimpah. Pemilihan antara Fetch API dan jQuery AJAX akan bergantung pada kebutuhan dan tujuan spesifik proyek pengembangan web. Jika ingin menggunakan teknologi yang lebih stabil, kompatibel, dan teruji, maka Anda dapat menggunakan AJAX. Namun jika ingin menggunakan teknologi yang lebih simpel, elegan, dan modern, kita dapat menggunakan Fetch API



5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
     **Menambahkan product menggunakan AJAX**
    pada fiile views.py saya menembahkan kode berikut agar bisa add products menggunakan AJAX:
    ```python 
    ...
    @csrf_exempt
    def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
    ```

    kemudian menambahkan path pada file urls.py 
    ```python
    ...
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
    ```

    **Menambahkan script di main.html**
    saya menambahkan script pada main.html secara asynchronus dengan kode berikut:
    ```JavaScript
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
        async function refreshProducts() {
            document.getElementById("product_table").innerHTML = ""
            const products = await getProducts()
            let htmlString = `<tr>
                <th>Name</th>
                <th>Jumlah</th>
                <th>Description</th>
                <th>Date Added</th>
            </tr>`
            products.forEach((item) => {
                htmlString += `\n<tr>
                <td>${item.fields.name}</td>
                <td>${item.fields.jumlah}</td>
                <td>${item.fields.description}</td>
                <td>${item.fields.date_added}</td>
            </tr>` 
            })
            
            document.getElementById("product_table").innerHTML = htmlString
        }

        refreshProducts()
        async function addProduct() {
            const formData = new FormData(document.querySelector('#form'));
            const response = await fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                const htmlString = `<tr>
                    <td>${data.fields.name}</td>
                    <td>${data.fields.jumlah}</td>
                    <td>${data.fields.description}</td>
                    <td>${data.fields.date_added}</td>
                </tr>`;
                document.getElementById("product_table").insertAdjacentHTML('beforeend', htmlString);
            } else {
                console.error('Failed to add product.');
            }

            document.getElementById("form").reset();
            return false;
        }

        document.getElementById("button_add").onclick = addProduct;

    </script>
    ``` 

    **Setelah itu membuat Button untuk modal**
    ```html
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
    ```

    **Membuat Modal Form**
    ```html
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price:</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description:</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>
    ```

    **Melakukan Perintah collectstatic**
    melakukan collecsa=tatic sebelum melakukan `git add .`, `git commit`, dan `git push` dengan kode berikut pada terminal
    `./manage.py collectstatic -v0 --noinput`