# Automated test.

Tests were run using the red-green-refactor methodology.

## The posts app

In the post app, I built the views using concrete generic views from drf:

- ListCreateAPIView: retrieves a list of the existing posts **AND** let an authenticated user create a post.

### Any user can retrieve the list of posts

For this test I commented out the create function in the PostListCreate view:

![test_1](/static/images/test/picture_1.png)

![test_2](/static/images/test/picture_2.png)

### Only authenticated users can create a post

For this test, I uncommented out the create function in the PostListCreate view and commented out the first test:

![test_3](/static/images/test/picture_3.png)
![test_4](/static/images/test/picture_4.png)

### Unathenticated users can't create a post:

![test_5](/static/images/test/picture_5.png)
![test_6](/static/images/test/picture_6.png)

