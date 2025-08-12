import customtkinter as ctk
import functools
import requests
import os
from PIL import Image, ImageTk

def time_date():
#time und date
 time = os.popen('echo %TIME%').read().strip()
 date = os.popen('echo %DATE%').read().strip()

def gui():
 app = ctk.CTk()
 app.geometry("650x800")
 app.title("Crypto Tracker")
 app.resizable(False, False)
 ctk.set_appearance_mode("dark")
 ctk.set_default_color_theme("blue")

 bg_image = Image.open(r"D:\desktop\Desktop\py api weather app\crypto_bg.png")
 bg_photo = ImageTk.PhotoImage(bg_image)
 background_label = ctk.CTkLabel(app, image=bg_photo, text="")
 background_label.image = bg_photo
 background_label.place(x=0, y=0, relwidth=1, relheight=1)

 #refresh
 refresh_icon = Image.open(r"D:\desktop\Desktop\py api weather app\refresh.png")
 refresh_icon = refresh_icon.resize((20, 20))
 refresh_icon = ImageTk.PhotoImage(refresh_icon)
 
 return app, refresh_icon


def get_price():
 
 api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
 api_key = 'c3bca26f-7995-40ff-8fa1-dc07e2772c3d'
 headers = {"X-CMC_PRO_API_KEY": "c3bca26f-7995-40ff-8fa1-dc07e2772c3d"}
 params = {"symbol": "BTC", "convert": "USD"}
 response = requests.get(api_url, headers=headers, params=params)
 data = response.json()
 btc_price = data['data']['BTC']['quote']['USD']['price']

 return btc_price




def update_price(label):
    try:
        new_price = get_price()
        label.configure(text=f"BTC Price: ${new_price:.2f}")
    except Exception as e:
        label.configure(text="Error fetching price")
        print(f"Error: {e}")

def update_price_async(label, app):
    label.configure(text="Loading...")
    app.after(100, lambda: update_price(label))



def main():
    app, refresh_icon = gui()

    # Frame für Preis und Button
    price_frame = ctk.CTkFrame(app,fg_color="#1a1a1a")
    price_frame.pack(pady=350)

    new_price = get_price()

    # BTC-Preis-Label
    test_label = ctk.CTkLabel(price_frame, text=f"BTC Price: ${new_price:.2f}", font=("Arial", 24),fg_color="#1a1a1a")
    test_label.pack(side="left", padx=10)

    # Refresh-Button direkt daneben
    refresh_btn = ctk.CTkButton(price_frame, width=40, height=40, image=refresh_icon, text="", command=lambda: update_price_async(test_label,app))
    refresh_btn.image = refresh_icon
    refresh_btn.pack(side="left")

    app.mainloop()

if __name__ == "__main__":
    main()
