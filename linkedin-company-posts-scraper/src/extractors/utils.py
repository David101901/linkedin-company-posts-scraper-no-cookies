thondef extract_reaction_counts(post):
likes = int(post.find('span', class_='like-count').text.strip()) if post.find('span', class_='like-count') else 0
comments = int(post.find('span', class_='comment-count').text.strip()) if post.find('span', class_='comment-count') else 0
return {"likes": likes, "comments": comments}