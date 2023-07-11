# Automated test.

Tests were run using the red-green-refactor process.

As views were built using **concrete view classes** from drf (i.e ListCreateAPIView, which provides both, the GET and POST requests), I comment/uncomment out the unnecessary snippet of code in the views for running one test at the time. For instance, for testing the read functionality in the PostListCreateView, I commented out the create function and uncommented out after the test.


## Tests in the posts app

### Any user can retrieve the list of posts

Red phase result:

![test_1](/static/images/test/picture_1.png)

Green phase result (notice that the create function in the view was commented out):

![test_2](/static/images/test/picture_2.png)

### Only authenticated users can create a post

Red phase result (notice that the first test was commented out):

![test_3](/static/images/test/picture_3.png)

Green phase result:

![test_4](/static/images/test/picture_4.png)

### Unathenticated users can't create a post:

Red phase result:

![test_5](/static/images/test/picture_5.png)

Green phase result:

![test_6](/static/images/test/picture_6.png)

### Retrieve a post by id:

Red phase result:

![test_7](/static/images/test/picture_7.png)

Green phase result:

![test_8](/static/images/test/picture_8.png)

### Can't retrieve a post by invalid id:

Red phase result:

![test_9](/static/images/test/picture_9.png)

Green phase result:

![test_10](/static/images/test/picture_10.png)

### Can update an owned post:

Red phase result:

![test_11](/static/images/test/picture_11.png)

Green phase result:

![test_12](/static/images/test/picture_12.png)

### Can't update someone else's post:

Red phase result:

![test_13](/static/images/test/picture_13.png)

Green phase result:

![test_14](/static/images/test/picture_14.png)
