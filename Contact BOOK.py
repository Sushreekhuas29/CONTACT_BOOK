import tkinter as tk

# Create a list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    clear_entries()
    update_contact_list()

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    update_search_results(found_contacts)

# Function to update the search results
def update_search_results(results):
    search_list.delete(0, tk.END)
    for contact in results:
        search_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Function to delete a contact
def delete_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        del contacts[selected_contact_index[0]]
        update_contact_list()

# Create the main window
root = tk.Tk()
root.title("Contact Management System")

# Create and place input fields
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons for adding and deleting contacts
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

# Listbox to display contacts and search results
contact_list = tk.Listbox(root)
contact_list.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

search_list = tk.Listbox(root)
search_list.pack()

# Start the main loop
root.mainloop()