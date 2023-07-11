# Automated test.

Tests were run using the red-green-refactor process.
As views were built using **concrete view classes** from drf (i.e ListCreateAPIView, which provieds both, the GET and POST requests), I comment/uncomment out the unnecessary snippet of code in the views for running one test at the time. For instance, for testing the read functionality in the PostListCreateView, I commented out the create function and uncommented out after the test.


## Tests in the posts app

### Any user can retrieve the list of posts

Red phase result:

![test_1](/static/images/test/picture_1.png)

Green phase result (notice that the create function in the view was commented out):

![test_2](/static/images/test/picture_2.png)

### Only authenticated users can create a post

Red phase result (notice that the firs test was commented out):

![test_3](/static/images/test/picture_3.png)

Green phase result:

![test_4](/static/images/test/picture_4.png)

### Unathenticated users can't create a post:

Red phase result:

![test_5](/static/images/test/picture_5.png)

Green phase result:

![test_6](/static/images/test/picture_6.png)

