# Agile

## Week 1
- Setup repo
- Create Django project
- Install basic dependancies and add to requirements
- Create procfile to deploy to Heroku
- Create app on Heroku
- Link GitHub repo to Heroku app
- Test to deploy working project ASAP

- Document project creation and deployment
- Perform design thinking exercise for features to include in project
- Add user stories to readme
- Add wireframes to readme
- Identify a colour schema to use in the site
- Mock up initial database design and document in readme
- List and link technologies used in readme

- Learn to use Github projects. Create user stories and drop onto kanban board

### Reflections

Several false starts.
Got more comfortable using an Agile tool to plan functionality.  Applied retrospectively to 1st week objectives to practice how it works.

This was effectively the first iteration for the project before any real coding took place.

In a way I'll already started categorising user stories by area such as navigation or account management.  This gives an idea to the separate apps what will need to be created.

I found I was jumping from one task to the next with no real direction.  Best to plan each future iteration to make it easier to track what still needs to be done.

![01](docs/readme/agile/week-1-kanban.png "01")

## Week 2
- Setup base.html
- create separate components for site such as head, navbar, scripts and footer in a subfolder to inject into base.html
- Setup index page in home app
- Build navigation

### Reflections

This week I focused on building out part of the frontend.  The `home` app will contain the index page for the site.
The templates folder in the root directory contains the base.html *et al* templates.  From what I've learned so far different webpage components should be injected into each template.  Follow a modular/reusable/extension approach.  

In the background I continued researching models as I want to try to get these right 1st time.

Also it's useful to have some templates to link to models via views when the time comes.

TWIL (This week I learned) after creating a new project, cards can be dragged across from the add card area.  Also helps to use checkboxes to tick off smaller tasks relating to a larger one.


![01](docs/readme/agile/week-2-subtasks.png "01")

![02](docs/readme/agile/week-2-kanban-use.png "02")

Use bootstrap for speed.  Copy their [code](https://getbootstrap.com/docs/5.0/components/navs-tabs/) rather than start from scratch.

![03](docs/readme/agile/03-week-2-bootstrap-use.png "03")

Start to tailor the bootstrap code to something more site specific.

![basic-menu-setup](docs/readme/agile/week-2-basic-menu-setup.png "basic-menu-setup")