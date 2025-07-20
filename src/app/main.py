import tkinter as tk  # 導入 Tkinter，習慣上簡寫成 tk

# 創建主視窗
window = tk.Tk()

# 給視窗取個名字
window.title("我的第一個 Tkinter 視窗")

# 設置視窗大小（寬 x 高）
window.geometry("300x200")

# 進入主循環，讓視窗顯示出來
window.mainloop()
