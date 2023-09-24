 <h1>TUGAS 2</h1>
 

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



 <h1>TUGAS 3</h1>
 


<h2>Perbedaan get dengan post</h2>

Pada dasarnya, ```post``` digunakan saat kita ingin mengirimkan sesuatu ke server, sementara ```get``` digunakan saat kita ingin server mengirimkan sesuatu kepada kita. Pada form ```get```, data yang kita input akan diubah ke dalam bentuk string dan dimasukkan ke dalam URL. Pada form ```post```, data input akan di-encode terlebih dahulu lalu dikirimkan ke server.

Penggunaan ```get``` sebaiknya dibatasi pada kasus-kasus di mana data yang di-input tidak sensitif dan tidak berjumlah banyak. Jika data yang di-input merupakan data sensitif seperti password, gunakan ```form``` supaya password tersebut tidak muncul di URL. Jika data yang di-input berjumlah banyak, gunakan ```form``` juga, supaya URL yang terbentuk lebih ringkas. 

<h2>Perbedaan antara XML, JSON, dan HTML</h2>
Analisis perbedaan dapat ditinjau menggunakan dua lapis.

1) ```HTML``` berbeda dengan ```XML``` dan ```JSON``` karena ```HTML``` berurusan dengan bagaimana data akan ditampilkan, sementara ```XML``` dan ```JSON``` berurusan dengan bagaimana data disimpan dan dikirim.

2) ```XML``` dan ```JSON``` mirip dalam hal penggunaan, namun berbeda dalam fitur-fiturnya. ```JSON``` terkenal karena syntax-nya yang lebih mudah dibaca, men-support struktur data array, serta menggunakan memory yang lebih sedikit. ```XML``` banyak digunakan karena lebih mudah dibaca oleh mesin, dan mensupport tipe data yang kompleks. Dalam penggunaannya, semakin kompleks dan banyak data yang ingin disimpan, ```XML``` semakin direkomedasikan dibandingkan ```JSON```. Perbedaan-perbedaan berikutnya antara lain: 
a) ```XML``` menggunakan start dan end tags untuk identifikasi item, sementara ```JSON``` tidak menggunakan tag.
b) ```XML``` adalah ekstensi dari SGML, sementara ```JSON``` adalah ekstensi dari javascript
c) ```JSON``` berorientasi data, sementara ```XML``` berorientasi dokumen.

<h2>Alasan JSON sekarang lebih sering digunakan</h2>

1) ```JSON``` lebih cepat dan hemat space daripada ```XML```, sehingga lebih praktis digunakan.
2) Syntax ```JSON``` lebih mudah dibaca (lebih sederhana) oleh manusia daripada ```XML``` sehingga lebih mudah dipelajari.


<h2>Implementasi Checklist</h2>

1) Di terminal, masuk ke direktori utama pacil_inventory, lalu aktifkan virtual environment dengan command ```env\Scripts\activate.bat```

2) Buka file urls.py di folder pacil_inventory, dan ubah 'math/' menjadi di variable urls pattern:

```
urlpatterns = [
    path('', include(main.urls')),   # perubahan ada di baris ini
    path('admin/', admin.site.urls),
]    
```

3) Di direktori utama, buat foler ```templates``` dan di dalamnya buat file HTML bernama ```base.html``` yang isinya berikut:

```
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

4) Buka file ```settings.py``` pada directory proyek ```pacil_inventory``` dan tambahkan code pada variable ```TEMPLATES```:

```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # perubahan terjadi di baris sini
        'APP_DIRS': True,
        ...
    }
]
...
```

5) Buka file ```main.html``` pada folder ```templates``` di directory ```main```, dan ubah isinya menjadi berikut:

```
{% extends 'base.html' %}

{% block content %}
    <h1>Pacil Inventory Page</h1>

    <h5>App name: </h5>
    <p>{{ app_name }}</p>

    <h5>Student name: </h5>
    <p>{{ student_name }}</p>

    <h5>Class: </h5>
    <p>{{ class }}</p>

{% endblock content %}
```

6) Di directory ```main```, buat file bernama ```forms.py``` yang berisi:

```
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

7) Buka file views.py pada folder main dan tambahkan import-import berikut:
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
```

8) Di file yang sama, buat fungsi ```create_product``` seperti berikut:
```
def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

9) Masih di file views.py, ubah fungsi ```show_main``` menjadi berikut:
```
def show_main(request):
    items = Item.objects.all()
    context = {
        'app_name': 'pacil-inventory',
        'student_name': 'William Joel Matthew Quinn Rompis',
        'class': 'PBP A',
        'items': items
    }

    return render(request, "main.html", context)
```

10) Buka file ```urls.py di folder ```main``` dan tambahkan import berikut:
```
from main.views import show_main, create_product
```

11) Di file yang sama, tambahkan kode berikut pada variable ```urlpatterns```:
```
path('create-item', create_item, name='create_item'),
```

12) Masuk directory ```main/templates```, buat file HTML baru bernama ```create_item.html``` yang berisi:
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

13) Dalam folder yang sama, buka main.html dan tambahkan kode di dalam ```{% block content %}``` seperti berikut:
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_item' %}">
    <button>
        Add New Item
    </button>
</a>

{% endblock content %}
```

14) Buka ```views.py``` di folder main dan tambahkan import-import berikut:
```
from django.http import HttpResponse
from django.core import serializers
```

15) Di file yang sama, buat fungsi-fungsi berikut:
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

16) Buka file ```urls.py``` di folder ```shopping_list``` dan import fungsi-fungsi barusan:
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```

17) Di file yang sama, tambahkan code berikut dalam variable ```urlpatterns```:
```
...
path('xml/', show_xml, name='show_xml'), 
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
...
```



<h2>Screenshot Postman</h2>

HTML:
![html](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/8eeaee43-a0b3-498d-9584-a9a70c28353c)

XML:
![xml](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/c9cbe7c5-d7ed-403c-b011-6e2626eca306)

JSON:
![json](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/9af6cfb5-628d-4b27-8da6-682546d0f8c7)

XML (id = 2):
![xml_id2](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/5a3dbfec-6e7d-42b2-a616-7662c534f0ad)

JSON (id = 2):
![json](https://github.com/DaWanAnOnli/pacil_inventory/assets/124868777/01a4c2c7-37fe-4e65-ad92-e3f391ca1e92)



<h1>TUGAS 4</h1>

<h2>Implementasi Checklist</h2>

1. Pastikan semua step dilakukan dengan menjalankan virtual environment di dalam root directory pacil_inventory.
2. Kita akan membuat halaman untuk register account. Buka views.py dan  import berikut pada bagian atas seperti berikut:
```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
Berikutnya tambahkan fungsi berikut bagian bawah file:
```
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

3. Masuk ke directory main/templates dan buat file baru bernama ```register.html``` berisi berikut:
```
{% extends 'base.html' %}

{% block meta %}
   <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
   
   <h1>Register</h1>  

       <form method="POST" >  
           {% csrf_token %}  
           <table>  
               {{ form.as_table }}  
               <tr>  
                   <td></td>
                   <td><input type="submit" name="submit" value="Daftar"/></td>  
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

</div>  

{% endblock content %}
```

4. Di folder yang sama, buka urls.py dan tambahkan import berikut:
```
from main.views import register
```
Masih di file yang sama, pada variable ```urlpatterns``` tambahkan code berikut:
```
...
path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
...
```
5. Sekarang, kita akan membuat halam untuk login. Buka lagi views.py dan tambah import berikut:
```
from django.contrib.auth import authenticate, login
```
Lalu tambahkan function berikut:
```
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

6. Di directory main/templates, buat file baru bernama ```login.html``` dan isi dengan code berikut:
```
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

7. pada directory main, buka urls.py dan tambahkan import berikut:
```
from main.views import login_user
```
Serta tambahkan path berikut di dalam variable ```urlpatterns```:
```
path('login/', login_user, name='login'),
```

8. Sekarang, kita akan membuat halaman untuk logout. Buka lagi file views.py pada directory main dan tambahkan import berikut:
```
from django.contrib.auth import logout
```
Masih di file yang sama, tambahkan function berikut:
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

9. Buka file ```main.html``` pada directory main/templates dan tambahkan code berikut di bawah tabel:
```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

10. Buka file urls.py pada folder main dan masukkan import berikut:
```
from main.views import logout_user
```
Masih di file yang sama, tambahkan path url berikut ke dalam variable urlpattern.
```
path('logout/', logout_user, name='logout'),
```

11. Sekarang kita merestriksi akses halaman main. Buka file ```views.py``` pada folder main dan tambahkan import berikut:
```
from django.contrib.auth.decorators import login_required
```
Lalu, di atas function show_main, tambahkan baris code berikut:
```
...
@login_required(login_url='/login')
def show_main(request):
...
```

12. Sekarang kita akan menggunakan data dari cookies. Buka views.py pada folder main dan tambahkan import berikut:
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
Lalu, pada function ```login_user```, kita ganti code pada blok ```if user is None``` sebagai berikut:
```
if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
```
Masih di file yang sama, pada fungsi show_main, tambahkan code berikut pada variable context:
```
context: {
 ...
 'last_login': request.COOKIES['last_login'],
}
```
Lalu, ubah function logout_user seperti berikut:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

13. Buka file main.html lalu tambahkan code berikut di antara tabel dan tombol logout:
```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

14. Pada bagian terakhir, kita akan menghubungkan model product dengan user. Pada directory main, buka file ```models.py``` dan tambahkan code berikut:
```
...
from django.contrib.auth.models import User
...
```
Masih di file yang sama, pada model Item, tambahkan code berikut:
```
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

15. Pada directory main, buka ```views.py``` dan ubah function ```create_item``` menjadi berikut:
```
def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))
```
Ubah juga function ```show_main``` menjadi berikut:
```
def show_main(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
    ...
...
```

16. Save semua file yang telah dilakukan modifikasi, lalu buka terminal di dalam root directory pacil_inventory. Masukkan command ```python manage.py makemigrations'''. Akan muncul prompt, respons dengan angka 1. Setelah itu, akan muncul prompt lagi, respons dengan angka 1 lagi.
17. Masukkan command ```python manage.py migrate```


<h2>Django UserCreationForm</h2>

UserCreationForm adalah module built-in dari Django yang berfungsi membuat user baru yang memiliki passwordnya sendiri. Form ini menyediakan tiga field. Satu untuk username, 1 password, 1 untuk mengetik ulang password. Keuntungan dari module ini adalah module ini memastikan kedua password yang dimasukkan sama. Modul ini juga akan menolak registrasi user yang usernamnya sudah ada di dalam sistem, secara case-insensitive. Kelemahan modul ini yakni tidak adanya support untuk two-step verification melalui email atau pun SMS. Untuk mengatasinya, kita harus memodifikasi classnya secara langsung, atau membuat implementasi user creations sendiri dari nol.


<h2>Authentication & Authorization di Django</h2>

Secara singkat, authentication merujuk pada proses untuk memastikan bahwa aktivitas yang dilakukan atas nama pengguna tertentu benar-benar dilakukan oleh pengguna tersebut dan bukan oleh orang lain. Authorization merujuk pada apa saja yang dapat dilakukan oleh user tertentu dalam sistem. Kedua hal ini sangat berkaitan dan penting. Jika tidak ada authorization, siapa pun bisa melakukan apa saja dalam sistem. Tentu ini tidak diinginkan, karena mungkin ada data-data sensitif yang tidak baik jika diakses semua orang. Dalam hal ini, authentication berperan untuk memastikan seseorang hanya memperoleh hak-hak yang dipercayakan kepadanya saja, dan bukan hak-hak orang lain yang mungkin berbeda dengannya. Selain itu authentication juga memastikan kerahasiaan data pribadi, karena mungkin dalam akun tersebut terdapat informasi personal yang tidak ingin diakses oleh orang lain.

<h2>Cookies</h2>

Cookies adalah data yang dibuat oleh server dan dikirm ke browser pengguna sebagai ID bagi pengguna. Cookies akan disimpan pada periode waktu tertentu dan digunakan agar server dapat mengetahui siapa yang sedang mengaksesnya tanpa melalukan authentication terus-menerus. Contoh, saat kita login ke website tertentu, kita tidak perlu lagi memasukkan username dan password setiap kali kita berpindah-pindah halaman pada website tersebut, karena browser sudah menyimpan cookies untuk website tersebut.

Django menerapkan cookies dengan cara menyimpan session-id pada browser, dan bukan menyimpan data itu sendiri. Hal ini baik untuk security, karena data sensitif tidak akan disimpan di dalam browser kita yang mungkin rentan terhadap serangan. Sementara itu, data user sebenarnya akan disimpan di server.

<h2>Keamanan dalam menggunakan Cookies</h2>
