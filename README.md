 <h1>TUGAS 1</h1>
 

<h2>Implementasi Checklist</h2>

1) Buat directory baru bernama pacil_inventory dengan visibilitas public.
2) Inisiasi repository baru di github bernama pacil_inventory (repository yang digunakan untuk menulis file ini).
3) Hubungkan directory dari langkah 1 (direktori utama) dengan repository github dari langkah 2.
4) Dalam terminal, masuk ke dalam directory utama, lalu buat virtual environment baru, serta aktifkan.
5) Pada direktori utama, buat file requirements.txt dan isi dengan dependencies-dependencies yang perlu di-install:

<pre>
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
</pre>

6) Pasang dependencies dengan perintah: <pre>pip install -r requirements.txt </pre>
7) Buat project Django bernama pacil_inventory dengan perintah: <pre>django-admin startproject pacil_inventory .</pre>
   Bakal muncul beberapa file baru pada directory, salah satunya adalah file manage.py.
9) Tambahkan "*" pada ALLOWED_HOSTS di di file settings.py
10) Pada directory utama, buat file .gitignore yang akan mengabaikan directory venv dan file-file lain saat melakukan commit ke github. (isinya terlalu panjang untuk dimuat di sini, dan sama dengan tutorial 0)
11) add, commit, dan push ke repository yang sudah didaftarkan


12) Masuk ke dalam directory proyek pacil_inventory di dalam directory utama pacil_inventory dan buat aplikasi baru dengan perintah: python manage.py startapp main
13) Dalam directory proyek, buka file settings.py dan cara variable INSTALLED_APPS. Tambahkan 'main' ke dalam list INSTALLED_APPS.
14) Masuk ke directory aplikasi main yang berada dalam directory proyek. Buat directory baru bernama templates.
15) Dalam directory templates, buat file main.html. Di sini kita menentukan apa yang akan ditampilkan di web kita:

  ```html
  <h1>Pacil Inventory Page</h1>
  
  <h5>App name: </h5>
  <p>pacil_inventory</p>
  <h5>Student name: </h5>
  <p>William Joel Matthew Quinn Rompis</p>
  <h5>Class: </h5>
  <p>PBP A</p>
  ```


16) Pada directory aplikasi, buka file models.py dan isi dengan berikut:

```html
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

17) Masuk lagi ke terminal ke dalam directory utama, dan jalankan perintah:

```html
python manage.py makemigrations
python manage.py migrate
```

18) Buka berkas views.py yang terletak di dalam berkas aplikasi main, tambah baris import:
```html
from django.shortcuts import render
```

Lalu di bawah import tambahkan:

```html
def show_main(request):
    context = {
        'app_name': 'pacil-inventory',
        'student_name': 'William Joel Matthew Quinn Rompis',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
```

19) Buka lagi file main.html lalu lakukan modifikasi berikut:
```html
...
<h5>App name: </h5>
<p>{{ app_name }}</p>
<h5>Student name: </h5>
<p>{{ student_name }}</p>
<h5>Class: </h5>
<p>{{ class }}</p>
```

20) pada directory main, buat file urls.py, dan isi dengan:
```html
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

21) Buka file urls.py di directory proyek shopping_list, lalu lakukan import:
```html
...
from django.urls import path, include
...
```
22) Modifikasi variable urlpatterns sebagai berikut:
```html
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
23) add, commit dan push directory utama ke Github.

24) Buat dan deploy app baru di Adaptable bernama pacil-inventory dengan settings sama seperti saat membuat app shopping list.
    Gunakan repository pacil_inventory untuk membuat app.

25) Buat file README ini, lalu lakukan lagi add, commit, dan push.


<h2>Bagan Request Client</h2>
![Django MVT Model](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/767ae810-b5ae-4cc8-b5ec-48e58011bc40)


<h2>Kegunaan Virtual Environment</h2>
Virtual Environment berguna untuk menjaga agar aplikasi tetap dapat digunakan meskipun dalam komputer kita terinstall package/dependencies dengan versi berbeda.
Hal ini bermanfaat untuk dua kasus:

1) Jika salah satu atau beberapa _dependencies_ mengalami update yang cukup signifikan untuk memengaruhi proyek yang sekarang sedang dikerjakan,
   Virtual Environment akan menjaga agar proyek tersebut tidak dipengaruhi oleh update
2) Kita dapat mengerjakan proyek kita di komputer lain yang memiliki dependencies dengan versi yang berbeda (Contoh: python versi lama), tanpa harus menginstall
   versi yang sama dengan ada ada pada komputer kita biasanya.

<h2>MVC, MVT, MVVM</h2>

1) MVC adalah salah satu paradigma pemrograman web, yang merupakan singkatan dari Model, View, Controller. Model adalah bagian yang berisi definisi data yang akan disimpan di database. Controller adalah bagian yang berisi logika utama program, yang mungkin membutuhkan informasi yang terdapat dalam database (dengan perantara Models). View merupakan struktur dasar dari webpage yang isinya akan ditentukan dari hasil pemrosesan oleh Views. Contoh Framework: ASP.NET & Spring

2) MVT adalah salah satu paradigma pemrograman web, yang merupakan singkatan dari Model, View, Template. Pada dasarnya, MVT mirip dengan MVC, hanya saja View pada MVT berbeda dari View pada MVC. View pada MVT mengerjakan hal yang sama dengan Controller pada MVC, sementara Template pada MVT mengerjakan hal yang sama dengan View pada MVC. Models pada kedua paradigma ini mengerjakan hal yang serupa. Contoh Framework: Django.

Perbedaan utama MVC dengan MVT adalah: pada MVC, kita harus mengimplementasikan proses secara spesifik (misal, proses controller mengambil data dari models, atau models mengambil data dari database), sementara pada MVT, implementasi proses sudah dilakukan secara otomatis oleh framework.

3) MVVM adalah salah satu paradigma pemrograman web, yang merupakan singkatan dari Model, View, View-Model. Pada dasarnya, MVVM mirip dengan MVC. Model dan View dari kedua paradigma mengerjakan hal yang sama, sementara View-Model pada MVVM mengerjakan hal yang sama dengan Controller pada MVC. Contoh Framework: Prism, MVVM Light.

Ada 2 perbedaan dasar MVVM dengan MVC. 1. Pada MVVM request user akan ditangkap oleh View, sementara pada MVC request user akan ditangkap oleh Controller. 2. Pada MVVM View memiliki reference terhadap View-Model, sementara pada MVC View tidak memiliki reference (bersifat pasif) terhadap Controller. Karena MVT mirip dengan MVC, maka perbedaan antara MVT dengan MVVM mirip dengan perbedaan MVC dengan MVVM. Hanya saja pada MVT request user ditangkap oleh Controller, dan Template bersifat pasif terhadap View.


