from flask import Flask, render_template
import pandas as pd
from collections import defaultdict
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Load product data from Excel file
    df = pd.read_excel("snapdeal_products.xlsx")

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
    app.run(debug=True, host="0.0.0.0", port=5000)
