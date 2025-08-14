from flask import Flask, render_template
import pandas as pd
from collections import defaultdict

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_excel("snapdeal_products.xlsx")

    grouped_products = defaultdict(list)
    for _, row in df.iterrows():
        grouped_products[row['Category']].append({
            'Product Name': row['Product Name'],
            'Price': row['Price'],
            'Image URL': row['Image URL']
        })

    return render_template("index.html", grouped_products=grouped_products)

if __name__ == "__main__":
    app.run(debug=True)
