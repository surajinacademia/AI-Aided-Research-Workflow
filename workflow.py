# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## AI-Aided-Research-Workflow

# %% [markdown]
# - Legal Disclaimer: 
#     - I am not an ML/AI proficient researcher. I don't understand how LLM works. 
#     - Jevons paradox: productivity gains from tools and efficiency tips don't reduce work hours but instead enable taking on more work, leaving work-life balance unchanged or worse.

# %% [markdown]
# Intro
# <img src="images/1.png" width="100%">

# %% [markdown]
# AI in academia
# <img src="images/2.png" width="100%">

# %% [markdown]
# The hype
# <img src="images/3.png" width="100%">

# %% [markdown]
# Prompting basics
#
# **Prompt:** 
# “Can you look at Figure 5 from this paper and tell me what it shows?. I need to extacact the bond lifetime and force data from it. Giv me the data points in an Excel file with two columns—one for bond lifetime and one for force? Yeah? Just get the data points in the figure. Then make a plot from the extracted data so that I can confirm the data looks correct.”
#
# <img src="images/6.png" width="100%">
#

# %% [markdown]
# ROLE
#
# Scientific data analyst specializing in quantitative image analysis and biophysics literature
#
#

# %% [markdown]
# CONSTRAINTS
#
# - Extract data points visible in the figure, no interpolation. Flag any ambiguities in axis scales or units
#
#

# %% [markdown]
# CONTEXT
#
# I'm analyzing Figure 4E from a research paper on cadherin bond mechanics. I need the raw data points for further analysis.
#
#

# %% [markdown]
# TASK
#
# 1. Analyze Figure 4E in the uploaded image
# 2. Create an Excel file (.xlsx) with:
#     - Column 1: "Force" (include units from figure)
#     - Column 2: "Bond Lifetime" (include units from figure)
#
#

# %% [markdown]
# REMINDER
#
# Only extract points you can clearly identify in the figure

# %% [markdown]
# Data analysis Prompt 
#
# I have a dataset on road accidents. 
#
# 1. I want to know which country and region has high number of accidents. I want to see how countries compare based on accidents and resulting fatalitites. 
#
# 2. I want to get answers on some specific questions like if there is any pattern wrt to time, days or dates. 
#
# 3. Get some deeper insight to some questions that i haven't framed yet. 
#
# First create a detalied report on the data structure and then we will analyze the data in depth. 

# %% [markdown]
# The Chef analogy
# <img src="images/4.jpg" width="100%">

# %% [markdown]
# RULES

# %% [markdown]
# PLANS

# %% [markdown]
# SKILLS

# %% [markdown]
# SUB-AGENTS

# %% [markdown]
# DOCS

# %% [markdown]
# MCP
# <img src="images/5.png" width="100%">

# %% [markdown]
#
