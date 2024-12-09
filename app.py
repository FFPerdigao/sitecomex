
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Análise de Documentos</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2rem; }
        .container { max-width: 600px; margin: auto; }
        h1 { text-align: center; color: #333; }
        .upload-form { margin-top: 20px; }
        .result { margin-top: 20px; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Upload de Invoice e Packing List</h1>
      <form class="upload-form" action="/" method="POST" enctype="multipart/form-data">
        <label for="invoice">Invoice (PDF):</label><br>
        <input type="file" name="invoice" required><br><br>
        <label for="packing">Packing List (PDF):</label><br>
        <input type="file" name="packing" required><br><br>
        <button type="submit">Analisar Documentos</button>
      </form>
      {% if analysis %}
      <div class="result">
        <h2>Resultados da Análise</h2>
        <pre>{{ analysis }}</pre>
        <p><strong>By Frederico Perdigão</strong></p>
      </div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_files():
    analysis = None
    if request.method == "POST":
        invoice = request.files.get("invoice")
        packing = request.files.get("packing")
        if invoice and packing:
            analysis = f"Análise dos arquivos enviada com sucesso!\nInvoice: {invoice.filename}\nPacking List: {packing.filename}"
    return render_template_string(HTML_TEMPLATE, analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
