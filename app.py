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
    # Replace 'resume.pdf' with your actual resume filename
    # Make sure your resume file is in the static folder
    return jsonify({
        'success': True,
        'url': 'Patrick_Aglosolos_Resume.docx.pdf'  # or 'resume.html' if it's an HTML file
    })


if __name__ == '__main__':
    app.run()
