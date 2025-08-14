from flask import Flask, render_template
import pandas as pd
from collections import defaultdict
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Base directory of the app
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(BASE_DIR, "snapdeal_products.xlsx")

    # Load product data from Excel file
    df = pd.read_excel(excel_path)

    # Group products by category
    grouped_products = defaultdict(list)
    for _, row in df.iterrows():
        grouped_products[row['Category']].append({
            'Product Name': row['Product Name'],
            'Price': row['Price'],
            'Image URL': row['Image URL']
        })

    return render_template("index.html", grouped_products=grouped_products)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port
    app.run(debug=False, host="0.0.0.0", port=port)
