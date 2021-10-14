# Projem
## Ön Hazırlık
- proje klasörü oluşturdum
- proje klasörümde virtualen oluşturdum
    > virtualenv .venv
    ![](https://github.com/mesleki2017/flask-projem/blob/5551c0042297b644b49b655b6288d508db5eee2a/resimler/virtualenv1.png)
- daha önce kullandığım ilgili bir projeden requirements.txt dosyasını aldım ve proje klasörüne kopyaladım
- VScode editöründe projemi açtım
- activate komutunu kullanmak yerine activate1.py kodunu çalıştırdım ve .venv i aktive etmiş oldum
    > ![](https://github.com/mesleki2017/flask-projem/blob/5551c0042297b644b49b655b6288d508db5eee2a/resimler/virtualenv2.png)
-  ```pip install -r requirements.txt ``` komutu ile requirements.txt dosyasındaki kütüphaneleri yükledim
- github repositorie oluşturdum
    > ![](https://github.com/mesleki2017/flask-projem/blob/1dfd5abe11552acde1cc9a6237eb0e9220ec66a4/resimler/github1.png)

## Temel Proje klasör ve kütüphaneler
- static klasörü oluşturuldu
- static klasörü içinde css javascript ve libraries klasörleri oluşturuldu
- css içinde style1.css oluşturuldu
- javascript içinde grafik1.js oluşturuldu
- libraries içine kullanacağım javascipt kütüphaneleri eklendi
    > ![](https://github.com/mesleki2017/flask-projem/blob/9a5e1d25436a6543101e8525ddba9bffae8be256/resimler/static-templates-1.png)

## Demo amaçlı chart.js kullanmı 
- ![](https://github.com/mesleki2017/flask-projem/blob/6ea5f45e985925c9ba07dc44d5e7d05b756310da/resimler/chartjs-1.png)

- ```javascript 
    <script src="{{url_for('static', filename='/libraries/Chart.min.js')}}"></script>
    ````
    > grafik için kullanacağım kütüphane yi index.html ekledim
- ```javascript
    <script src="{{url_for('static', filename='/javascript/grafik1.js')}}"></script>
    ```
    > grafik1.js te oluşturacağım 2 grafigin datalarını ve options larını belirledim
    ve index.html çektim
- ```javascript
    <link rel="stylesheet" href="{{url_for('static', filename='/css/style1.css')}}"> 
    ```
    > index.html deki html kodun style bilgilerini style.1css dosyasında belirledim
- ```html 
    <div class="flex-container">
        <div class="div1">
            <span>Temel Görünüm</span>
        </div>
        <div class="div2">
            <span>1. Grafik</span>
        </div>
        <div class="div3">
            <span>2. Grafik</span>
         </div>
        <div  class="div4">
            <canvas id="grafik1" class="can1" ></canvas>
        </div>
        <div class="div5">
            <canvas id="grafik2" class="can2" ></canvas>
        </div>
    </div>
    ```
    > html de style olarak flex kullancağım
    > o yüzden bir flex-container lı div olusturup diger 5 div onun içine yazdım
    div class ismi illaki flex-container olmak zorunda degil önemli olan css te 
    ***display: flex*** kodunu ilgili class a atamak


