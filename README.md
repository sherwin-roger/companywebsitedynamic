# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:
# people.html
```
{% extends "website/base.html" %}

{% block content %}

<div class="productcontent">    
    <h1>Company people</h1>
    <div class="productitems">
        {% for company in companies %}
        <div class="productitem"> 
            <div class="itemimage">
            <img class="itemimage" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR23DQLxw3PaI3pGMak2zjv-6WHE7Ahl_AZg&usqp=CAU"  alt="product image">
            </div>
            <div class="itemname">{{company.peoplename}}</div>
        </div>
       {% endfor %}
    </div>
</div>
{% endblock  %}
```

# products.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="productcontent">    
    <h1>Our Premium Products</h1>
    <div class="productitems">
        {% for product in products %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtchrtmeXHEk3TcC-JA7aaLa9EW9TZRCwR8oi2FKOrCz1TA2bZlE-H4Zpt-o0z4E61mkONwCI&usqp=CAc" alt="product image">
            </div>
            <div class="itemname">{{product.itemname}}</div>
            <div class="itemprice">{{product.itemprice}} </div>
        </div>
        {% endfor %}
    </div>
    </div>
{% endblock  %}
```

## RESULT:
```
Thus a website is designed for the chip manufacturing company using database and is hosted in the URL http://sherwin.student.saveetha.in:8000/. HTML code is validated.