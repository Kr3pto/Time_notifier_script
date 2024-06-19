from django.core.management.base import BaseCommand
from plyer import notification
from datetime import datetime
import tkinter as tk



class Command(BaseCommand):
    help = 'Display the current time in a Tkinter window'

    def handle(self, *args, **options):
        # Create the Tkinter window
        root = tk.Tk()
        root.title('Current Time Display')

        # Create a label to display the time
        time_label = tk.Label(root, text='', font=('Helvetica', 48))
        time_label.pack(padx=10, pady=10)

        # Function to update the time label
        def update_time():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time correctly
            time_label.config(text=current_time)
            root.after(1000, update_time)  # Update time every 1000 milliseconds (1 second)

        # Call update_time initially to set the label
        update_time()

        # Run the Tkinter main loop
        root.mainloop()