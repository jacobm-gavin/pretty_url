from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Assuming we'll store links in memory for simplicity
# In a real app, you'd use a database
links = {}
base_url = 'http://127.0.0.1:5000/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract the original link from form data
        original_link = request.form['full_link']
        # Generate a shortened link (for simplicity, using the link's hash)
        short_link_hash = hash(original_link) % 10000  # Simple hash for demonstration
        short_link = base_url + str(short_link_hash)
        # Store the link mapping
        links[short_link] = original_link
        # Redirect or send back the short link to the user
        return render_template('index.html', short_link=short_link)
    return render_template('index.html', short_link=None)

# Redirect route for shortened links
@app.route('/<int:short_link_hash>')
def redirect_short_link(short_link_hash):
    original_link = links.get(base_url + str(short_link_hash))
    if original_link:
        return redirect(original_link)
    return 'Link not found', 404

if __name__ == "__main__":
    app.run(host='localhost', port=5000)