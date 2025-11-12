def convertBlogToDict(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "description": blog["description"],
        "author": blog["author"],
        "content": blog["content"],
        
    }

def convertBlogsToList(blogs) -> list:
    return [convertBlogToDict(blog) for blog in blogs]