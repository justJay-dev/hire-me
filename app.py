import os
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    render_template_string,
    request,
)
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs
from flask_mail import Mail, Message

debug = False

app = Flask(__name__)
app.config.from_pyfile("config.py")

blog_name = app.config["BLOG_NAME"]

bootstrap = Bootstrap(app)

pages = FlatPages(app)

mail = Mail(app)

from forms import ContactForm

# some globals and error handling
@app.context_processor
def inject_blog_name():
    return {"blog_name": blog_name}


@app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "error.html",
            error_title="404, page not found.",
            line1="We're having trouble finding that page, try using the navigation menu.",
        ),
        404,
    )


@app.errorhandler(500)
def error_500(e):
    return (
        render_template(
            "error.html",
            error_title="Uhoh, an error!",
            line1="The server is having a bad time,we're working on fixing it!",
        ),
        500,
    )


@app.route("/")
def index():
    contact_form = ContactForm()
    # Articles are pages with a publication date
    articles = (p for p in pages if "published" in p.meta)
    # Show the 2 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta["published"])
    return render_template(
        "index.html",
        articles=latest[:2],
        character_list="ALOT",
        contact_form=contact_form,
    )


# article stuff
@app.route("/pygments.css")
def pygments_css():
    return pygments_style_defs("friendly"), 200, {"Content-Type": "text/css"}


@app.route("/posts")
def posts():
    # Articles are pages with a publication date
    articles = (p for p in pages if "published" in p.meta)
    # Show the 20 most recent articles, most recent first.
    latest = sorted(articles, reverse=True, key=lambda p: p.meta["published"])
    return render_template("posts.html", articles=latest[:20])


@app.route("/posts/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("post.html", page=page)


@app.route("/tags/<string:tag>")
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get("tags", [])]
    return render_template("tag.html", articles=tagged, tag=tag)


@app.route("/system/contact", methods=["POST"])
def system_contact_submit():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        # this is where email sending happens
        # FlaskMail - > SendGrid
        subject = f"Message from {contact_form.email.data}"
        msg = Message(
            subject,
            sender=str(app.config["MAIL_DEFAULT_SENDER"]),
            recipients=[str(app.config["TARGET_MAILBOX"])],
        )
        msg.body = str(contact_form.message.data)
        mail.send(msg)
        return redirect(url_for("index"))
    else:
        title = "Bad Form Submit"
        line1 = "Something was weird with what you sent us."
        line2 = "Please go back and try again. Thanks!"
        return render_template("error.html", title=title, line1=line1, line2=line2)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
