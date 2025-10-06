from django.shortcuts import redirect
from django.core.mail import send_mail

# from account.email_temp import data
from config.settings import EMAIL_HOST_USER as from_user
from django.core.mail import EmailMultiAlternatives

def check_user(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request, *args, **kwargs)
    return wrapper


#SENDING EMAIL
def send_simple_email():

    send_mail(

        subject="Xush kelibsiz!!!",

        message="Saytimiz haqida malumot oling",

        from_email=from_user,

        recipient_list=["thefoxblogers@gmail.com",from_user],

        fail_silently=False,

    )







def send_html_email(to_user,product_title,product_price,product_qn,total_price):
    subject = "Forget Password"

    from_email = from_user

    to = [to_user]

    text_content = product_title
    # product_price=product_price
    # product_qn=product_qn
    # total_price=total_price
    html_content = f"""
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


    email = EmailMultiAlternatives(subject, text_content,
                                   from_email, to)

    email.attach_alternative(html_content, "text/html")

    email.send()





def sending_email(to_user, username, code,from_user=from_user):
    subject = "Parolni tiklash"
    from_email = from_user
    to = [to_user]
    reset_link=f"http://127.0.0.1:8000/accounts/forget/done/?name={username}"
    text_content = f"Salom {username},\nParolni tiklash parol:{code}"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="uz">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width,initial-scale=1.0">
      <title>Parolni tiklash</title>
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
          font-size:22px;
        }}
        .content {{
          padding:20px;
          font-size:16px;
          color:#111827;
        }}
        .btn {{
          display:inline-block;
          margin:20px 0;
          padding:14px 28px;
          background:#0ea5a4;
          color:#fff;
          text-decoration:none;
          border-radius:8px;
          font-weight:bold;
          transition:0.3s;
        }}
        .btn:hover {{
          background:#0c8b8a;
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
          <h1>🔐 Parolni Tiklash </h1>
        </div>
        <div class="content">
        <p>{ code }</p>
          <p>Assalomu alaykum, <b>{username}</b>!</p>
          <p>Parolni tiklash uchun quyidagi tugmani bosing:</p>
          <a href="{reset_link}" class="btn">Parolni Tiklash</a>
          <p>Agar tugma ishlamasa, quyidagi linkni brauzeringizga nusxalab o‘tkazing:</p>
          <p><a href="{reset_link}">Sahifaga o'tish</a></p>
        </div>
        <div class="footer">
          © 2025 Sizning Kompaniyangiz. Barcha huquqlar himoyalangan.
        </div>
      </div>
    </body>
    </html>
    """

    email = EmailMultiAlternatives(subject, text_content, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()
