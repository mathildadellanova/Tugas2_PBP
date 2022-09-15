Link aplikasi Heroku yang telah di-deploy
tugas2pbpmathilda.herokuapp.com

Bagan request client Django:

Kaitan antara urls.py, views.py, models.py, dan berkas html:
Django bekerja sebagai controller yang mengecek resource tersedia di URL.
GET request dikirim dari client-side menuju server-side (Django). Kemudian
request tersebut diteruskan ke urls.py. urls.py memanggil function di view.py
yang match dengan url-nya. views.py dan models.py saling berinteraksi untuk
mengambil data dari database. Kemudian views.py me-render template dari folder
templates bersamaan dengan data kepada user. Terakhir, views.py merespons kepada
client dan mengirim template sebagai respons.

Mengapa menggunakan virtual environment?
Virtual environment digunakan untuk mengisolasi satu proyek dengan proyek lainnya
serta memastikan bahwa semua developer bekerja dalam environment yang sama. Hal 
ini dapat menghindari terjadinya error karena ada developer yang mengerjakan 
project dengan requirements yang berbeda.

Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan 
virtual environment?
Ya, namun akan rawan terjadi konflik atau error.

Cara mengimplementasikan poin 1 sampai dengan 4 di atas pada soal
1. Membuat class CatalogItem di models.py
2. Membuat function show_catalog di views.py
3. Membuat variabel app_name dan urlpatterns di urls.py
4. Menambahkan path katalog ke urls.py di project_django
5. Menambahkan variabel di models.py ke katalog.html
6. Menjalankan command migrate dan loaddata
7. Membuat app baru di Heroku
8. Membuat 2 secret di Heroku (HEROKU_API_KEY, HEROKU_APP_NAME
9. Add, commit, dan push perubahan ke repositori github
10. Run all job di Action repository github
