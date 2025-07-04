import tkinter as tk
from tkinter import ttk

def generate_anchor():
    title = entry.get().strip()
    if not title:
        return

    # Generate GitHub-style anchor
    anchor = title.lower().replace(' ', '-')
    anchor = ''.join(c for c in anchor if c.isalnum() or c == '-')
    toc_line = f"- [{title}](#{anchor})"

    # Display and copy to clipboard
    output_var.set(toc_line)
    root.clipboard_clear()
    root.clipboard_append(toc_line)
    root.update()

    # Select the output for convenience
    output_entry.selection_range(0, tk.END)

# UI setup
root = tk.Tk()
root.title("Markdown TOC Generator")
root.geometry("500x180")
root.resizable(False, False)

# Input
ttk.Label(root, text="Enter section title:").pack(pady=(10, 0))
entry = ttk.Entry(root, width=60)
entry.pack(pady=5)
entry.focus()

# Output
ttk.Label(root, text="Markdown TOC line (auto-copied):").pack()
output_var = tk.StringVar()
output_entry = ttk.Entry(root, textvariable=output_var, width=60, state='readonly')
output_entry.pack(pady=5)

# Button
ttk.Button(root, text="Generate", command=generate_anchor).pack(pady=10)

# Enter key also triggers generation
root.bind('<Return>', lambda event: generate_anchor())

# Start
root.mainloop()
