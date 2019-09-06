#!/usr/bin/python36
print("content-type: text/html\n")
import cgi
data = cgi.FieldStorage()
id = data.getvalue("id")

print("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
  background-image: url("mediator.jpg");
  margin: 0;
  font-family: "Lato", sans-serif;
  position: fixed;
}

.sidebar {
  margin: 0;
  padding: 0;
  width: 200px;
  background-image: url("mediator.jpg");
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

.sidebar a {
  display: block;
  color: black;
  padding: 16px;
  background-image: url("mediator.jpg");
  text-decoration: none;
}
.rk2{
  padding-left:10000px;
}
 
.sidebar a.active {
  background-color: #4CAF50;
  background-image: url("mediator.jpg");
  color: white;
}

.sidebar a:hover:not(.active) {
  background-color: #555;
  background-image: url("mediator.jpg");
  color: white;
}

div.content {
  margin-left: 200px;
  padding: 1px 16px;
  height: 100px;
}

@media screen and (max-width: 700px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
  .sidebar a {float: left;}
  div.content {margin-left: 0;}
}

@media screen and (max-width: 400px) {
  .sidebar a {
    text-align: center;
    float: none;
  }
}
.rk3
{
 width: 2000px;
}
</style>
 <script>
  
    
  
  </script>
  
</head>
<body>""")

print("""<div class="sidebar">
   <h1 style="font-family:courier;">kaamkaaz</h1>
  <a class="active" href="#home">Home</a>
    <a href="http://192.168.43.124/cgi-bin/reccommend.py">recommend</a>
  <a href="http://192.168.43.124/cgi-bin/list.py?eid={}">Hire</a>
  
</div>
<div class="rk2">


</div>
<div class="content">
<p>WELCOME TO KAAMKAAZ PORTAL<p>
</div>

</body>
</html>
""".format(id, id, id))