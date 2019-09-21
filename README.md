# Data Visualisation Workshop


### Notes and Slides

- [Introduction](notes/Introduction.pdf): Overall introductions
- [Representation](notes/Representation.pdf): Walk though different chart guidelines
- [Aesthetics](notes/Aesthetics.pdf): Include decoding guidelines, color, chart-junk
- [Interaction](notes/Interaction.pdf): Overview on animation and interation
- [Model Vis](notes/Modelvis.pdf): Concepts on model visualisation
- [Storytelling](notes/Storytelling.pdf): Storytelling and link to data visualisation
- [Dashboards](notes/Dasboard.pdf): Concepts on structuring an interactive dashboard
- [Tools & Resources](notes/Resources.pdf): List of tools and resources for visualisation


### In-Class Notebooks
- [01-Simple](01-Simple.html)
- [02-Telco-Basic](02-Telco-Basic.html)
- [03-Facets](03-Facets.html)
- [04-Interactive](04-Interactive.html)
- [05-Chart-Serving](05-chart.py)


### Additional Resources:

- Visualisation Libraries: 
    - [pyviz.org](http://pyviz.org): Overview on all python libraries got data visualisation
    - [Altair](http://altair-viz.github.io): Python library for Interactive Grammar of Graphics
    - [Vega-lite](http://vega.github.io/vega-lite): JS library for Interactive Grammar of Graphics
- Chart Guidelines e.g. Visual Vocabulary
    - FT Version: [ft.com/vocabulary](http://ft.com/vocabulary)
    - Vega-lite Version: [gramener.github.io/visual-vocabulary-vega/](https://gramener.github.io/visual-vocabulary-vega/)



### Session Plan

**Day 1**

- *Workshop Introduction*
- *Session #1: Value of Data Visualisation*
- *Session #2: Tools & Abstractions for Data Visualisation*
- *Session #3: Theory of Data Visualisation*
- *Session #4: Guidelines for Better Data Visualisation*
- *Day One Summary*
- *Data-Story Group Exercise*

**Day 2**

- *Recap & Questions*
- *Data-Story Presentations*
- *Session #5: Crafting Visual Stories with Data*
- *Data-Story Rework*
- *Session #6: Interactivity*
- *Session #7: Explorable Vis for Business Users*
- *Session #8: Putting together an Interactive Application*
- *Overall Summary & Way Forward*

Detailed session plan can be read at [session.md](session.md)

### Setup & Installation

System Requirements: 

- You need a laptop for hands-on coding during the workshop, with the following minimum specifications:
   - 2 or more CPU Cores
   - 4GB or more RAM
   - 10 GB or more free disk space
   - Running Windows 7+, 64-bit macOS, or Linux
   
Step 1:
- For Python data science libraries, please install the latest Anaconda Python 3 Distribution (currently Python 3.7) for your OS: https://www.anaconda.com/distribution/
- Detailed install instruction & troubleshooting is available at http://docs.anaconda.com/anaconda/install/

Step 2:
- Please download using https://github.com/amitkaps/data-vis-workshop/archive/master.zip or clone the repo from: https://github.com/amitkaps/data-vis-workshop.git

Step 3:
- Once you have Anaconda installed (Step 1) and downloaded or cloned the repo (Step 3), you can use the following conda commands to install all the required packages. 

Please note:
- Do `cd` into the folder and then run these commands.
- If you are on Windows, then please only use the Anaconda Prompt (and not command prompt)

```
conda env create --file vis.yaml
conda activate vis

python install_check.py
>>> All-Set! Packages installed.
```

### Datasets

The list of datasets are available in the `data` folder and you can read about them at [datasets.md](datasets.md)


