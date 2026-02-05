# The Existential Dread and AI Agents: A Scientific Researcher's Manifesto for Sustainable, Context-Aware AI Integration.

## Abstract

Despite the excitement surrounding AI integration in academic research, a lack of understanding of the capabilities and limitations of Large Language Models (LLMs) often leads to hallucinations, buggy or overengineered code, and data privacy concerns. While AI chatbots have become remarkably powerful (and potentially dangerous), aligning user expectations with model responses can be very frustrating. In this talk/tutorial, I will show examples of context engineering and effective prompting techniques that can help you navigate large codebases and projects. We will discuss agentic capabilities that leverage tools like MCPs, skills, commands, rules, and planning modes. We will explore how custom instructions can guide AI towards giving significantly better results while maintaining your data local and private. Additionally, I will demonstrate how to create custom agents and MCPs for research-specific tasks like data analysis, image analysis, and literature organization. As LLMs consume significant energy in training and inference, understanding their strengths and limitations is essential for sustainable integration.

**Keywords: Agents, Skills, MCPs, Commands, Rules, Image Analysis, Data Analysis, Context Engineering, Custom Workflows**

GitHub Repository: https://github.com/surajinacademia/AI-Aided-Research-Workflow

## Content

This is a framework for AI-aided research using **context engineering** to guide AI agents for coding, data analysis, image analysis, and scientific computing. This repository demonstrates how to move beyond simple prompting to sophisticated agent-based workflows using rules, skills, MCPs, and subagents. The key philosophy is to provide the right structure, rules, and tools so AI agents work autonomously and reliably on complex research tasks.

In this repository you will find information about:

    1. Rules
    2. MCPs: Here is an example of MCP that I created on one fine evening: [napari-mcp](https://github.com/surajinacademia/cellpose_mcp)
    3. Skills
    4. Subagents
    5. Commands

## Example Workflows

### Data Analysis
- Rules define pandas operations and visualization standards for data analysis.
- Provide dataset and high-level analysis goals
- AI creates analysis plan with specific questions
- Generate exploratory analysis, statistics, and visualizations

**Example:** `Data_analysis/road_accident_dataset.csv` - accident patterns by country, region, time, severity

### Image Analysis
- Configure `napari-mcp` and `cellpose-mcp` servers
- Interactive visualization in napari window and segmentation with cellpose-mcp.

**Example:** n
- use prompt: "Can you segment the cells in the image and find the number of cells and the nuclei positions?"
 
## Reference

### Rules

| Rule | Description | When Applied |
|------|-------------|--------------|
| `rules.md` | Main rule file with project-wide standards and expert domains | Always |
| `python-coding-standards.md` | Python coding patterns, best practices, and visualization standards | Always |
| `Image-analysis.md` | Image analysis workflow patterns and MCP tool prioritization | For `.png` files |
| `project-repo.md` | Repository structure documentation and navigation guide for AI agents | Always |

### MCP Servers

| MCP | Capabilities | Use Cases |
|-----|-------------|-----------|
| `napari-mcp` | Interactive image visualization and analysis | Microscopy, 3D imaging, segmentation |
| `cellpose-mcp` | Cell segmentation and quantification | Cell counting, morphology analysis |
| `fmcp` | Mathematical plotting (matplotlib, numpy, sympy) | Scientific plots, numerical computation |
| `sympy-mcp` | Symbolic mathematics and calculus | Calculus, algebra, differential equations |
| `claude-scientific-skills` | Scientific computing capabilities | Research computations |
| `data-forge` | Data manipulation and analysis | Complex data transformations |
| `notion-mcp` | Notion workspace integration | Note-taking, documentation |
| `zotero-mcp` | Zotero library access for literature management | Literature management |
| `cursor-ide-browser` | Browser automation for testing | Web testing, scraping |

### Skills

| Skill | Purpose |
|-------|---------|
| `scientific-writing` | Creates concise, structured scientific documents with LaTeX equations, integrated figures, and clear technical writing |

### Subagents

| Subagent | Purpose |
|----------|---------|
| `literature-review` | Expert literature research for biophysics and cell mechanics, semantic searches across local papers, Zotero library, and web sources |

### Commands

| Command | Purpose |
|----------|---------|
| `git` | Complete GitHub workflow: quick commit & push for small updates, detailed workflow for significant changes with proposed commit messages |
| `airulez` | AI-Rulez workflow: generate and commit with default message. |
 
## Resources

- **Cursor Documentation**: [cursor.sh/docs](https://cursor.sh/docs)
- **Model Context Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **MCP Servers**: [mcpservers.org](https://mcpservers.org)
- **Cursor Rules**: [cursor.directory](https://cursor.directory)

## License

Copyright © 2026 Suraj Kumar Sahu. All rights reserved.

This is a private research repository. All code, data, and documentation are proprietary and must not be shared, published, or made available outside the authorized research group without explicit written permission.

## Contact

**Author:** Suraj Kumar Sahu @[surajinacademia](https://github.com/surajinacademia) (ssahu2@ucmerced.edu)
**Affiliation:** University of California, Merced
