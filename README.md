# Frank Hurst Author

---

Frank’s first book, ‘The Postmistress of Nong Khai’ was the first
of three in his‘Golden Triangle’ series. The second ‘The Chiang
Mai Assignment’ was published in November 2017 and the final book
of the trilogy ‘Mekong Dragon’ was published June 2019. His books,
which have received wide acclaim, are authentic crime thrillers
based in England and Thailand. They follow the adventures of
intelligence officer Mike Rawlin as he tries to capture a dangerous
international drugs trafficker in South East Asia.

Frank was himself a former drugs intelligence officer who
travelled widely during his career and his writing has the ring
of authenticity on every page. The books are about secrets, romance,
and rivalry in the dangerous jungles of the Golden Triangle and the
corridors of power in London where deception and conspiracy loom at
every turn.

---

### Automated Testing

[W3C](https://validator.w3.org/) - All HTML files with their data were directly
    input into the Mark-Up Validation Service.
    The results: All HTML code adheres to validation requirements. Errors for
    Python only.

[WSC](https://jigsaw.w3.org/css-validator/) - CSS data was directly input into
    the CSS Validation Service. The results: `Congratulations! No Error Found.`

[PEP8](http://pep8online.com/) - Python script - `app.py`- was run through PEP8 online
    for PEP8 requirements. Results: `All Right` (Adheres to PEP requirements)

[Markdownlint](https://github.com/Bealby/markdownlint) - Markdownlint was
used to validate README.md file. 'Validation successful'

[Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
A feature in Chrome Developing Tools - Lighthouse Audit - was carried out
on Mobile and Desktop to assess **Performance**, **Accessibility**,
**Best Practices**, **CEO** and **Progressive Web App**.

[Validate Javascript](https://validatejavascript.com/)

[Chrome DevTools - Console](https://developers.google.com/web/tools/chrome-devtools/)

## Technologies Used

---

The following technologies were used in this project:

### IDE

- [GitPod](https://gitpod.io/workspaces/) - A platform used for hard coding
   of Website

### Hosting

- [Heroku](https://id.heroku.com/) - Heroku is a cloud platform as a service
  supporting several programming languages.
- [GitHub](https://github.com/)** - Used to store repository and deploy Website

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language of Website
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used to style
   HTML elements
- [Python](https://www.python.org/) - A programming language that lets you work
   quickly and integrate systems more effectively.
- [JavaScript](https://www.javascript.com/) - Used in collaboration with
   Bootstrap to collapse Navigation Bar for small devices and Google Maps.
   Also used for EmailJS.

### Databases

- [MongoDB](https://www.mongodb.com/) - MongoDB is a general purpose,
  document-based, distributed database built for modern application developers

### Language Validators

- [W3C](https://validator.w3.org/) - Used to validate HTML code
- [WSC](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [Validate Javascript](https://validatejavascript.com//) - Used to validate
   javascript
- [Pep8 online](http://pep8online.com/) - Validator for Python code
- [Markdown Lint](https://github.com/Bealby/markdownlint) - Used for validation
    checks on README.md content

### Libraries

- [Google Fonts](https://fonts.google.com/) - Programme used to import main
   fonts in Website: **Playfair Display** and **Calligraffitti**
- [Font Awesome](https://fontawesome.com/) - Programme used to import icons
   for Footer in Website: **far-envelope** and **fas fa-phone**

### Tools

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/desktop/) - Allowed
   preliminary designs to be drawn up of Website
- [Adobe Photoshop](https://www.adobe.com//) - Fixing size images
- [Adobe Illustrator](https://www.adobe.com//) - Fixing Logo - Magnet Fishing
  Stockholm
- [Sweet Alert](https://sweetalert.js.org/) - Used for alerts in contact form
- [Responsive Design](http://ami.responsivedesign.is/) - Free software
    to generate Mockup of Website on different devices
- [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse/) -
    Helped to improve the quality of Website
- [Chrome Developer Tools](https://www.google.com/chrome/dev/Google) - A useful
   developing tool in Chrome to edit pages and diagnose problems

### Frameworks

- [BOOTSTRAP](https://getbootstrap.com/) - A framework for building responsive
   Websites where the powerful Grid system was used along with styling
- [jQuery](https://jquery.com/) - Used to implement Navigation Collapse feature
   JavaScript Plugin
- [Popper](https://popper.js.org/) - Used to implement Navigation Collapse
   feature JavaScript Plugin
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework
   written in Python
- [Emailjs](https://www.emailjs.com/) - For sending email directly From JavaScript

## Deployment

---

For deployment of Website please follow the below steps:

### Step-1 - Heroku

- Click the following link [Heroku Login](https://id.heroku.com/login) and
  and set-up an account in Heroku

- Click on the icon to `Create New App`

- Input an unique `App Name` and `Choose a Region` and click `Create App`

- Click the link `Settings`and scroll to the button `Reveal Convig Vars`

- In the `Convig Vars` add the following inputs for `Key` and `Value`
  - KEY = `IP`, VALUE = `0.0.0.0`
  - KEY = `PORT`, VALUE = `5000`
  - KEY = `EMAILJS_KEY`, VALUE = `EMAIJS USER ID`
  - KEY = `MONGO_URI`, VALUE = `MONGO USER ID`

- `EMAIJS USER ID` and `MONGO USER ID` can be provided upon request.

### Step-2 - GitHub

- Click the following link [GitHub](https://github.com/) and
  and set up an account in GitHub.

- Click the following GitHub repository [Magnet Fishing](https://github.com/Bealby/Milestone-Project-3)

- On the main page of the repository click the green button **Code**.

- A drop down menu for `Clone with HTTPS` should appear. Copy `URL` link.

- Open terminal in IDE; i.e. [Gitpod](https://gitpod.io/)

- Change the current directory to the local directory

- Type `git clone` plus `URL` in terminal (Copied above). Then `Enter`

- In the terminal install the Flask `requirements.txt` file using the
  command `pip3 freeze --local > requirements.txt`

- For local deployment in GitPod, create the file `env.py` which will contain
  confidential `USER KEYS` that can be provided upon request.

- The app can then be run by typing the command `python3 app.py` in the terminal

### Step-3 - Connecting GitHub to Heroku for deployment

- In the terminal log login into Heroku using the command `heroku login`

- Enter your `Email` and `Password` when prompted

- (`Heroku Apps` created can be viewed using the command `heroku apps`)

- Set up `Heroku` as `Master` branch using the command `heroku git:remote -a app-name`.
  The `app-name` being the name of the `Heroku App` created in Step-1.

- Then in the terminal type the command `echo web: python app.py > Procfile`.

- Then the command `heroku ps:scale web=1`.

- Finally to update:
  - `git init`
  - `git add .`
  - `git commit -m ""`
  - `git push -u heroku master` (Push to heroku)
  - `git push origin master` (Push locally to GitHub)

- When you are ready for `Production` deployment change the
  `debug=True` to `debug=False` in the `app.py`.

- Login into Heroku in your browser window. Click your hero app and then click
 `Open App` to launch Website. i.e. `https://app-name-here.herokuapp.com/`.

[Go to top](#contents)

## Credits

---

### Content

- All content for this Website was provided by Murray Bealby.

### Media

- All photos and video were provided by Murray Bealby.

### Code

- Image Zoom Feature - Books:
  [Image Zoom Feature](https://www.w3schools.com/howto/howto_css_modal_images.asp)
