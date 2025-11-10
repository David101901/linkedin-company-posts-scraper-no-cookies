thonfrom bs4 import BeautifulSoup

def parse_linkedin_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    posts = []
    
    for post in soup.find_all('div', class_='feed-shared-update-v2'):
        post_data = {
            "post_content": post.find('span', class_='break-words').text if post.find('span', class_='break-words') else "",
            "reaction_count": {
                "likes": int(post.find('span', class_='reaction-count').text.strip()) if post.find('span', class_='reaction-count') else 0,
                "comments": int(post.find('span', class_='comment-count').text.strip()) if post.find('span', class_='comment-count') else 0
            },
            "media_attachments": [media['src'] for media in post.find_all('img')] if post.find_all('img') else [],
            "post_url": post.find('a', class_='ember-view')['href'] if post.find('a', class_='ember-view') else "",
            "timestamp": int(post.find('time')['datetime']) if post.find('time') else 0
        }
        posts.append(post_data)
    
    return posts