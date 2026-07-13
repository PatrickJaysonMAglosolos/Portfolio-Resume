from flask import Flask, render_template, jsonify

app = Flask(__name__)


PROFILE = {
    "name": "Your Name",
    "title": "Aspiring Developer",
    "about": "Write a short summary about yourself, your goals, and the kind of work you want to do.",
    "skills": ["Python", "Flask", "HTML", "CSS", "Git"],
    "projects": [
        {
            "name": "Portfolio Resume",
            "description": "A clean personal website to showcase your work and experience.",
        },
        {
            "name": "Project Two",
            "description": "Add a short description of another project here.",
        },
    ],
    "email": "you@example.com",
    "linkedin": "https://www.linkedin.com/in/your-profile",
}


@app.route('/')
def home():
    return render_template('index.html', profile=PROFILE)


@app.route('/open-resume')
def open_resume():
    # Return a URL to the resume in the static folder so it can be loaded in an iframe/modal.
    # Make sure the file exists in /static (e.g. static/Patrick_Aglosolos_Resume.png)
    from flask import url_for
    return jsonify({
        'success': True,
        'url': url_for('static', filename='Patrick_Aglosolos_Resume.png')
    })


if __name__ == '__main__':
    app.run()
