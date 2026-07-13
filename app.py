from flask import Flask, render_template, jsonify, request
import random

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
    from flask import url_for
    return jsonify({
        'success': True,
        'url': url_for('static', filename='Patrick_Aglosolos_Resume.png')
    })


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get('message') or '').strip()

    greetings = [
        "Good day. How may I assist you?",
        "Hello. How can I be of service?",
        "Greetings. What information do you require?"
    ]

    resume_responses = [
        "The résumé may be accessed via the 'View Resume' button at the top of the page.",
        "Please consult the 'View Resume' control at the page header to review the résumé."
    ]

    skills_responses = [
        "Proficient in Python, Flask, HTML, CSS, and Git.",
        "Skills include Python, Flask, HTML, CSS, and Git; experienced in web development and version control."
    ]

    projects_responses = [
        "Notable projects include 'Portfolio Resume' (personal website). Additional projects are listed on the profile.",
        "Projects include a portfolio website and further work; details available upon request."
    ]

    contact_responses = [
        f"Contact via email: {PROFILE.get('email', 'N/A')}.",
        f"For inquiries, please email: {PROFILE.get('email', 'N/A')}."
    ]

    achievements_responses = [
        "Gold medalist — Bataan Provincial Skills Competition, Mechanical Engineering CAD (2026).",
        "Gold medalist — Central Luzon Regional Skills Competition, Mechanical Engineering CAD (2026).",
        "Currently competing at the Philippine National Skills Competition in Mechanical Engineering CAD (2026).",
        "Recipient of provincial and regional gold medals in Mechanical Engineering CAD (2026).",
        "Awarded provincial and regional gold medals in Mechanical Engineering CAD; presently competing at the national level (2026)."
    ]

    fallback_responses = [
        "Apologies — that information is not available. Please ask about résumé, skills, projects, achievements, or contact.",
        "I am unable to assist with that request. Try asking about résumé, skills, projects, achievements, or contact."
    ]

    if not message:
        reply = "Please provide a message so I may assist you."
    else:
        lower = message.lower()
        if any(k in lower for k in ['achiev', 'achievement', 'achievements', 'award', 'awards', 'medal', 'medals', 'winner', 'won']):
            reply = random.choice(achievements_responses)
        elif any(g in lower for g in ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']):
            reply = random.choice(greetings)
        elif 'resume' in lower or 'résumé' in lower:
            reply = random.choice(resume_responses)
        elif 'skill' in lower or 'skills' in lower:
            reply = random.choice(skills_responses)
        elif 'project' in lower or 'projects' in lower:
            reply = random.choice(projects_responses)
        elif 'email' in lower or 'contact' in lower or 'reach' in lower:
            reply = random.choice(contact_responses)
        else:
            reply = random.choice(fallback_responses)

    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run()
