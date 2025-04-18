import tkinter as tk
from tkinter import scrolledtext
import wikipedia

# Wikipedia summary function
def get_summary(topic):
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(topic, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"⚠️ Too many results. Try being more specific.\nSuggestions: {', '.join(e.options[:3])}"
    except wikipedia.exceptions.PageError:
        return "❌ No page found for that topic."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Handle sending a message
def send_message(event=None):
    user_message = entry.get().strip()
    if not user_message:
        return

    # Show user message
    chat_box.configure(state='normal')
    chat_box.insert(tk.END, f"You: {user_message}\n", "user")
    chat_box.tag_add("user_bg", "end-2l", "end-1l")
    chat_box.see(tk.END)

    # Get bot response
    bot_response = get_summary(user_message)

    # Show bot response
    chat_box.insert(tk.END, f"Bot: {bot_response}\n\n", "bot")
    chat_box.tag_add("bot_bg", "end-3l", "end-1l")
    chat_box.see(tk.END)

    entry.delete(0, tk.END)
    chat_box.configure(state='disabled')

# GUI setup
window = tk.Tk()
window.title("WikiChat Bot")
window.geometry("500x600")
window.config(bg="#ece5dd")

# Chat display
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Segoe UI", 11), bg="#ffffff", fg="#000000", bd=0)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.insert(tk.END, "Bot: 👋 Hello! Type any topic and I’ll give you a summary from Wikipedia.\n\n", "bot")
chat_box.tag_config("user", foreground="#ffffff", font=("Segoe UI", 11, "bold"))
chat_box.tag_config("user_bg", background="#25d366")
chat_box.tag_config("bot", foreground="#000000", font=("Segoe UI", 11))
chat_box.tag_config("bot_bg", background="#e0e0e0")
chat_box.config(state='disabled')

# Entry field
entry_frame = tk.Frame(window, bg="#f0f0f0")
entry_frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(entry_frame, font=("Segoe UI", 12), width=40)
entry.pack(side=tk.LEFT, padx=(0, 10), pady=5, ipady=6, expand=True, fill=tk.X)
entry.bind("<Return>", send_message)

send_button = tk.Button(entry_frame, text="Send", font=("Segoe UI", 11), bg="#25d366", fg="white", command=send_message)
send_button.pack(side=tk.RIGHT, pady=5)

# Start the app
entry.focus()
window.mainloop()
