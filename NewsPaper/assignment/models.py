user1 = User.objects.create_user('username1')
user2 = User.objects.create_user('username2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

category1 = Category.objects.create(name='Category 1')
category2 = Category.objects.create(name='Category 2')
category3 = Category.objects.create(name='Category 3')
category4 = Category.objects.create(name='Category 4')

post1 = Post.objects.create(title='Post 1', preview='Preview 1', content='Content 1', author=author1)
post1.categories.add(category1, category2)

post2 = Post.objects.create(title='Post 2', preview='Preview 2', content='Content 2', author=author2)
post2.categories.add(category2, category3)

news1 = Post.objects.create(title='News 1', preview='Preview 3', content='Content 3', author=author1, is_news=True)
news1.categories.add(category3, category4)

comment1 = Comment.objects.create(post=post1, user=user1, content='Comment 1')
comment2 = Comment.objects.create(post=post1, user=user2, content='Comment 2')
comment3 = Comment.objects.create(post=post2, user=user1, content='Comment 3')
comment4 = Comment.objects.create(post=news1, user=user2, content='Comment 4')

post1.like()
post1.dislike()
post2.like()
news1.like()
comment1.like()
comment2.dislike()
comment3.like()
comment4.dislike()

# Обновляем рейтинги авторов
author1.update_rating()
author2.update_rating()

best_author = Author.objects.all().order_by('-rating').values('user__username', 'rating').first()
print(best_author)

best_post = Post.objects.filter(is_news=False).order_by('-rating').values('pub_date', 'author__user__username',
                                                                          'rating', 'title', 'preview').first()
print(best_post)
