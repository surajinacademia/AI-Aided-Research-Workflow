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
#

# %% [markdown]
# - Legal Disclaimer:
#   - I am not an ML/AI proficient researcher. I don't understand how LLM works.
#   - These tools are not for people without prior basic knowledge in programming and research experience.
#   - Jevons paradox: productivity gains from these tools doesn't lead to reduced workload but instead keeping work-life balance unchanged or worse.
#

# %% [markdown]
# Intro
# <img src="images/1.png" width="100%">
#

# %% [markdown]
# AI in academia
# <img src="images/2.png" width="100%">
#

# %% [markdown]
# The hype
# <img src="images/3.png" width="100%">
#

# %% [markdown]
# IDEs and CLI
#
# 1. Cursor
# 2. VSCode + GitHub Copilot
# 3. Antigravity
# 4. Cline
# 5. Claude Code
# 6. OpenCode
# 7. Windsurf
#
# Which one to choose? - Data analysis: Cursor, Antigravity, VS code, Claude Code
#
# - Inline edit and Predictive Text
#

# %% [markdown]
# Prompting basics
#
# <img src="images/6.png" width="100%">
#

# %% [markdown]
# PROMPT STRUCTURE
#
#         **Prompt:**“Can you look at Figure 5 from this paper and tell me what it shows?. I need to extacact the bond lifetime and force data from it. Giv me the data points in an Excel file with two columns—one for bond lifetime and one for force? Yeah? Just get the data points in the figure. Then make a plot from the extracted data so that I can confirm the data looks correct.”
#
# **Role:** Scientific data analyst specializing in quantitative image analysis and biophysics literature
#
# **Task:** Extract bond lifetime and force data from Figure 4E in the uploaded image
#
# **Constraints:** Extract data points visible in the figure, no interpolation. Flag any ambiguities in axis scales or units
#
# **Reminder:** Only extract points you can clearly identify in the figure
#

# %% [markdown]
# # Context management
#
# [Context Rot Problem](https://research.trychroma.com/context-rot)
#
# <img src="images/8.png" width="100%">
#
# Model maintain performance even when context is compressed or filtered, as long as the relevant information is preserved.
#
# Models can often "reason through" irrelevant context better than they can filter it for pure information retrieval
#
# ### Context management strategies
#
# 1. For retrieval tasks:
#    - keep only information semantically related to the query.
#
#    - Place critical facts at start or end (avoid middle)
#
#    - Remove semantically unrelated content
#
# 2. For reasoning tasks:
#    - Group related information together
#
#    - Keep reasoning chain elements proximate
#
#    - More forgiving of middle placement than retrieval
#
# 3. Claude's approach:
#    - \compact
#
#    - \context
#
# 4. [Understanding Claude Code's Context Window](https://www.damiangalarza.com/posts/2025-12-08-understanding-claude-code-context-window/)
#

# %% [markdown]
# Model Comparison
# <img src="images/7.png" width="100%">
#

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
#

# %% [markdown]
# Image Analysis Prompt
#
# **Prompt:** Extract the cell boundaries in this image using cellpose-mcp and mark the nuclei.
#
# But this is not enough. You also need to verify.
#
# **Prompt**: Extract the cell boundaries in this image using cellpose-mcp and mark the nuclei. Then, write a python script to do the extraction and verification.
#

# %% [markdown]
# The Chef kitchen
# <img src="images/4.jpg" width="100%">
#

# %% [markdown]
# RULES
#

# %% [markdown]
# PLANS
#
# 1. Plan mode allows you to create
#    - Goals
#    - Key references
#    - High-level steps and pseudocode
#    - Step by step instructions with reasoning and algorithmic steps
#    - Optional features to implement
#    - Mermaid flowchart
#    - Example code
#    - Documentation/walkthrough after execution
#    - <span style="color: red;">**To-do list**</span>
#    - Agents, Skills and tools to be used in the bulding process
#    - <span style="color: red;">**Verification and validation steps**</span>
#

# %% [markdown]
# SKILLS
#
# 1. [Scientific writer](/Users/suraj/Documents/AI-Aided-Research-Workflow/.cursor/skills/scientific-writing/SKILL.md)
#
# 2. [Claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills/tree/main)
#

# %% [markdown]
# SUB-AGENTS
#

# %% [markdown]
# DOCS
#
# 1. You can add any repo as docs to cursor.
# 2. You can change any repo to a MCP server. by changing github.com to gitmcp.io
#     Example: https://github.com/anthropics/prompt-eng-interactive-tutorial -> https://gitmcp.io/anthropics/prompt-eng-interactive-tutorial
#

# %% [markdown]
# MCP
# <img src="images/5.png" width="100%">
#

# %% [markdown]
#
