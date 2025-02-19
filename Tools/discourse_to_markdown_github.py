import json
import requests
from pathlib import Path
import re
from datetime import datetime
import base62

def process_forum_topics():
    """Process all markdown files in forum_topics directory to fix image links"""
    topics_dir = Path('forum_topics')
    
    # Create images directory if it doesn't exist
    images_dir = Path('images') 
    images_dir.mkdir(exist_ok=True)
    
    # Create attachments directory if it doesn't exist
    attachments_dir = Path('attachments')
    attachments_dir.mkdir(exist_ok=True)
    
    # Process each markdown file
    for md_file in topics_dir.glob('*.md'):
        # Read the file content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Fix image and attachment links
        updated_content = fix_image_links(content)
        
        # Write back the updated content
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
def fix_image_links(markdown_text):
    """Replace Discourse upload links with relative paths to images directory"""
    # Match both image and attachment formats:
    # ![title|dimensions](attachments/hash.ext) 
    # ![title|dimensions](upload://hash.ext)
    # [title|attachment](attachments/hash.ext)
    # [title|attachment](upload://hash.ext)
    # ![[title|dimensions](images/hash.ext)]
    patterns = [
        # Match ![title|dimensions](attachments/hash.ext) and ![title|dimensions](upload://hash.ext)
        r'!\[([^\]]+)\]\((?:attachments|upload:\/\/)\/([a-zA-Z0-9]+)(?:\.(\w+))?\)',
        # Match [title|attachment](attachments/hash.ext) and [title|attachment](upload://hash.ext) 
        r'\[([^\]]+)\]\((?:attachments|upload:\/\/)\/([a-zA-Z0-9]+)(?:\.(\w+))?\)',
        # Match ![title|dimensions](images/hash.ext)
        r'!\[([^\]]+)\]\(images\/([a-zA-Z0-9]+)(?:\.(\w+))?\)',
        # Match [title|attachment](images/hash.ext)
        r'\[([^\]]+)\]\(images\/([a-zA-Z0-9]+)(?:\.(\w+))?\)',
        # Match ![[title|dimensions](images/hash.ext)]
        r'!\[\[([^\]]+)\]\(images\/([a-zA-Z0-9]+)(?:\.(\w+))?\)\]',
        # Match ![[Screenshot title|dimensions](images/hash.jpeg)]
        r'!\[\[Screenshot[^\]]+\]\(images\/([a-zA-Z0-9]+)(?:\.(\w+))?\)\]'
    ]
    
    for pattern in patterns:
        markdown_text = re.sub(pattern, replace_match, markdown_text)
    
    return markdown_text

def replace_match(match):
    # Handle different pattern matches
    if len(match.groups()) == 3:
        title = match.group(1)
        hash_or_path = match.group(2)
        ext = match.group(3) or ''
    else:
        # For Screenshot pattern
        hash_or_path = match.group(1)
        ext = match.group(2) or ''
        title = f'Screenshot'
    
    # If it's already a hex hash, use it directly
    if len(hash_or_path) == 40 and all(c in '0123456789abcdef' for c in hash_or_path.lower()):
        hex_hash = hash_or_path
    else:
        # Convert base62 hash to hex
        hex_hash = hex(base62.decode(hash_or_path))[2:].zfill(40)
    
    # Check if it's an image by looking for image markdown syntax
    is_image = '!' in match.group(0)
    
    if is_image:
        # For images, look in images directory
        return f'![{title}](images/{hex_hash}.{ext})'
    else:
        # For attachments, look in attachments directory
        return f'[{title}](attachments/{hex_hash}.{ext})'

def clean_markdown(text):
    """Clean and format markdown content"""
    # Split into posts by the separator
    posts = text.split('-' * 25)
    cleaned_posts = []
    
    for post in posts:
        # Remove extra whitespace and newlines
        post = post.strip()
        if post:
            cleaned_posts.append(post)
            
    return cleaned_posts

def parse_post_metadata(post):
    """Extract metadata (author, date) from post text"""
    # Look for patterns like "username - February 12, 2023 2:34pm"
    metadata_pattern = r'([^\n-]+)\s*-\s*([^\n]+)$'
    
    lines = post.split('\n')
    metadata_line = lines[0]
    content = '\n'.join(lines[1:])
    
    match = re.search(metadata_pattern, metadata_line)
    if match:
        author = match.group(1).strip()
        date_str = match.group(2).strip()
        return {
            'author': author,
            'date': date_str,
            'content': content.strip()
        }
    return None

def format_github_markdown(topic):
    """Format a topic and its replies into a nice GitHub markdown"""
    response = requests.get(topic['markdownurl'])
    raw_content = response.text
    
    posts = clean_markdown(raw_content)
    
    # Create markdown content
    md_content = f"# {topic['title']}\n\n"
    md_content += f"*Original topic from {topic['date_time']}*\n\n"
    
    for i, post in enumerate(posts):
        metadata = parse_post_metadata(post)
        if metadata:
            if i == 0:
                md_content += f"### Original Post\n"
            else:
                md_content += f"### Reply #{i}\n"
                
            md_content += f"**Author:** {metadata['author']}  \n"
            md_content += f"**Date:** {metadata['date']}  \n\n"
            md_content += f"{metadata['content']}\n\n"
            md_content += "---\n\n"
    
    return md_content

def main():
    # Create output directory
    output_dir = Path('forum_topics')
    output_dir.mkdir(exist_ok=True)
    
    # Read JSON file
    with open('iranunchained_posts.json', 'r') as f:
        topics = json.load(f)
    
    # Process each topic
    for topic in topics:
        # Create a safe filename from the title
        safe_title = re.sub(r'[^\w\-]', '_', topic['title'].lower())
        output_file = output_dir / f"{safe_title}.md"
        
        # Format and save the markdown
        try:
            markdown_content = format_github_markdown(topic)
            output_file.write_text(markdown_content)
            print(f"Processed: {topic['title']}")
        except Exception as e:
            print(f"Error processing {topic['title']}: {str(e)}")

if __name__ == "__main__":
    main()
    
    # uncomment the function below to fix the image names
    # todo: it does not handle all attachments/extensions
    #process_forum_topics()