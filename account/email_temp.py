f"""
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Buyurtma Tafsilotlari</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background:#f4f6f8;
      margin:0; padding:0;
    }}
    .container {{
      max-width:600px;
      margin:20px auto;
      background:#fff;
      border-radius:12px;
      overflow:hidden;
      box-shadow:0 6px 18px rgba(0,0,0,0.1);
    }}
    .header {{
      background:linear-gradient(90deg,#0ea5a4,#7c3aed);
      color:#fff;
      padding:20px;
      text-align:center;
    }}
    .header h1 {{
      margin:0;
      font-size:20px;
    }}
    .content {{
      padding:20px;
    }}
    table {{
      width:100%;
      border-collapse:collapse;
      margin-top:10px;
    }}
    th, td {{
      text-align:left;
      padding:12px;
      border-bottom:1px solid #e5e7eb;
      font-size:15px;
    }}
    th {{
      background:#f9fafb;
      color:#111827;
    }}
    .total {{
      text-align:right;
      font-size:16px;
      font-weight:600;
      padding:14px;
      color:#0f172a;
    }}
    .footer {{
      background:#f9fafb;
      padding:16px;
      text-align:center;
      font-size:13px;
      color:#6b7280;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🛒 Buyurtma Tafsilotlari</h1>
    </div>
    <div class="content">
      <p>Hurmatli mijoz, sizning buyurtmangiz tafsilotlari:</p>
      <table>
        <tr>
          <th>Mahsulot</th>
          <th>Narxi</th>
          <th>Soni</th>
          <th>Jami</th>
        </tr>
        <tr>
          <td>{product_title}</td>
          <td>{product_price} so'm</td>
          <td>{product_qn} dona</td>
          <td>{total_price} so'm</td>
        </tr>
      </table>
      <p class="total">Umumiy summa: {total_price} so'm</p>
    </div>
    <div class="footer">
      © 2025 Sizning Kompaniyangiz. Barcha huquqlar himoyalangan.
    </div>
  </div>
</body>
</html>
"""
