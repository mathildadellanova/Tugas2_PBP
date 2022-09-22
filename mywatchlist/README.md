Nama: Mathilda Dellanova
NPM: 2106751240
Link: 

Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON = JavaScript Object Notation

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform!
Kita memerlukan data delivery dalam mengimplementasikan sebuah platform karena
sebuah platform dapat mengakses data dari banyak source, sehingga data delivery akan
membuat pengiriman data antar platform semakin mudah

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 dengan
menggunakan python manage.py startapp mywatchlist
2. Menambahkan path mywatchlist ke list INSTALLED_APPS di project_django/settings.py
3. Menambahkan path mywatchlist ke project_django/urls.py
4. Membuat sebuah model MyWatchList di models.py (class MyWatchList)
5. Membuat file bernama initial_mywatchlist_data.json di mywatchlist/fixtures/ 
dan menambahkan 10 data untuk objek MyWatchList
6. Membuat function show_watchlist_html, show_watchlist_json dan show_watchlist_xml
di views.py
7. Menambahkan app_name dan 3 urlpatterns ke mywatchlist/urls.py
8. Membuat file mywatchlist.html di mywatchlist/templates/
9. Melakukan makemigrations, migrate, serta loaddata
9. Membuat test unit di tests.py
10. Menambahkan python manage.py loaddata initial_mywatchlist_data.json ke file
Procifile