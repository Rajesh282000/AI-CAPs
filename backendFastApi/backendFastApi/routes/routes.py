from fastapi import APIRouter, HTTPException

from model.model import Blog
from config.config import blogsCollection
from serializer.serializer import convertBlogToDict, convertBlogsToList 
from bson import ObjectId

endPoints = APIRouter()

@endPoints.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@endPoints.post("/new/blog")
def newBlog(blog:Blog):
    blogsCollection.insert_one(dict(blog))
    return {
        "status": "success",
        "message": "Blog created successfully!"
    }

@endPoints.get("/all/blogs")
def allBlogs()-> list:
    blogs = blogsCollection.find()
    convertedBlogs = convertBlogsToList(blogs)
    return convertedBlogs

@endPoints.get("/blog/{blog_id}")
def getBlog(blog_id: str):
    try:
        blog = blogsCollection.find_one({"_id": ObjectId(blog_id)})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid blog ID format")

    if blog:
        return convertBlogToDict(blog)

    raise HTTPException(status_code=404, detail="Blog not found")

# ✅ UPDATE Blog by ID
@endPoints.put("/blog/{blog_id}")
def update_blog(blog_id: str, updated_blog: Blog):
    try:
        # Convert string to ObjectId
        blog_obj_id = ObjectId(blog_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid blog ID format")

    # Convert the incoming Blog model to a dictionary
    updated_data = updated_blog.model_dump()

    result = blogsCollection.update_one({"_id": blog_obj_id}, {"$set": updated_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {
        "status": "success",
        "message": "Blog updated successfully"
    }


# ❌ DELETE Blog by ID
@endPoints.delete("/blog/{blog_id}")
def delete_blog(blog_id: str):
    try:
        blog_obj_id = ObjectId(blog_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid blog ID format")

    result = blogsCollection.delete_one({"_id": blog_obj_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {
        "status": "success",
        "message": "Blog deleted successfully"
    }