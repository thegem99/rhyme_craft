from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Rhymecraft API (Static URLs)")

# -----------------------------
# 🌐 CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "https://rhymecraft-production.up.railway.app/images/"

# -----------------------------
# 📁 CATEGORIES (STATIC IMAGE URLS)
# -----------------------------
categories = [
    {
        "id": 1,
        "name": "English Poems",
        "image": BASE_URL + "category_1.jpg"
    },
    {
        "id": 2,
        "name": "Hindi Poems",
        "image": BASE_URL + "category_2.jpg"
    },
    {
        "id": 3,
        "name": "English Stories",
        "image": BASE_URL + "category_3.jpg"
    },
    {
        "id": 4,
        "name": "Hindi Stories",
        "image": BASE_URL + "category_4.jpg"
    }
]

# -----------------------------
# 📦 NESTED DATA (STATIC IMAGE URLS)
# -----------------------------
data = {
    1: {
        101: {
            "title": "The Road Not Taken",
            "content": "Two roads diverged in a yellow wood...",
            "image": BASE_URL + "1_101.jpg"
        },
        102: {
            "title": "Daffodils",
            "content": "I wandered lonely as a cloud...",
            "image": BASE_URL + "1_102.jpg"
        }
    },
    2: {
        201: {
            "title": "प्रेरणा",
            "content": "यह एक प्रेरणादायक कविता है...",
            "image": BASE_URL + "2_201.jpg"
        }
    },
    3: {
        301: {
            "title": "The Silent Boy",
            "content": "Once there was a boy who never spoke...",
            "image": BASE_URL + "3_301.jpg"
        }
    },
    4: {
        401: {
            "title": "छोटी कहानी",
            "content": "यह एक छोटी हिंदी कहानी है...",
            "image": BASE_URL + "4_401.jpg"
        }
    }
}

# -----------------------------
# 📌 HOME
# -----------------------------
@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to Rhymecraft API 🚀"
    }

# -----------------------------
# 📂 GET CATEGORIES
# -----------------------------
@app.get("/categories")
def get_categories():
    return {
        "status": "success",
        "data": categories
    }

# -----------------------------
# 📚 GET CATEGORY CONTENT
# -----------------------------
@app.get("/content/{category_id}")
def get_category_content(category_id: int):

    if category_id not in data:
        return {
            "status": "success",
            "category_id": category_id,
            "data": {}
        }

    return {
        "status": "success",
        "category_id": category_id,
        "data": data[category_id]
    }

# -----------------------------
# 📖 GET SINGLE ITEM
# -----------------------------
@app.get("/content/{category_id}/{item_id}")
def get_item(category_id: int, item_id: int):

    if category_id not in data:
        raise HTTPException(status_code=404, detail="Category not found")

    if item_id not in data[category_id]:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "status": "success",
        "data": data[category_id][item_id]
    }
