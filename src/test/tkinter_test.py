import tkinter as tk
import os

def close_window():
    window.destroy()

window = tk.Tk()
window.title("Tkinter 測試視窗")

# 嘗試設定視窗圖示 (icon.ico要放在同資料夾)
try:
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    window.iconbitmap(icon_path)
except Exception as e:
    print("設定圖示失敗:", e)

# 視窗大小
window.geometry("400x300")

# 標籤
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 20))
label.pack(pady=40)

# 關閉按鈕
btn_close = tk.Button(window, text="關閉視窗", command=close_window)
btn_close.pack()

window.mainloop()

