from guizero import App, Text, TextBox, PushButton, Picture

un = "username"
pw = "password"

def check_user():
    if un_box.value == un and pw_box.value == pw:
        message = Picture(app, image="C:\\Users\\student\\Pictures\\Saved Pictures\\flower1.png")

    else:
        message = Text(app, text="Access Denied")

app = App(title="Hello GUI", bg=(200,255,200))
Text(app, text="Username", color=(255,150,255))
un_box = TextBox(app)
Text(app, text="Password", color=(255,150,255))
pw_box = TextBox(app)
submit = PushButton(app, command=check_user)
app.display()