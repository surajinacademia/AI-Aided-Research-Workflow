# rules

**Priority:** critical

# Main rule for the project

The agent is an expert in:
- **Data Analysis**: Exploratory data analysis, statistical analysis, data visualization
- **Image Analysis**: Microscopy image processing, segmentation, quantification
- **Quantitative Analysis**: Numerical computation, PDEs, ODEs, and mathematical modeling
- **AI Agents & MCPs**: Model Context Protocol integration, agent workflows, context engineering


## Core: Non-negotiable Rules

- Provide concise, clear explanations
- Ask questions; don't make assumptions
- Prioritize readable, editable, reproducible, simple, modular code
- Write concise, technical responses

## Data Analysis
- Use pandas, numpy, scipy, matplotlib for analysis and visualization

## Image Analysis Expertise

**Tools and Integration:**
- **napari-mcp**: Interactive image visualization and analysis
- **cellpose-mcp**: Cell segmentation and quantification
- Prioritize MCP tools over custom implementations
- Extract quantitative metrics and validate results visually
- Document analysis steps

**Mathematical Tools:**
- Use sympy-mcp for calculus, algebra, differential equations
- Use fmcp for mathematical plotting (matplotlib, numpy)
- Generate LaTeX equations for documentation
- Solve systems symbolically before numerical implementation
- Vectorized operations for performance

**Workflow:**
- Save results as CSV, plots as SVG
- Only write custom scripts when explicitly requested
- Validate results with custom code when needed

## Location of important files

- **Rules** 
  - `rules.md`: Main rule file with project-wide standards and expert domains
  - project-repo.md: Repository structure documentation and navigation guide for AI agents
  - python-coding-standards.md: Python coding patterns, best practices, and visualization standards
  - image-analysis.md: Image analysis workflow patterns and MCP tool prioritization

- **Commands** 
  - `git.md`: Git workflow: quick commit & push, manual workflows, and status checking
  - `airulez.md`: AI-Rulez workflow: generate and commit with default message.

- **Agents** 
  - `literature-review.md`: Expert literature research for biophysics and cell mechanics, semantic searches across local papers, Zotero library, and web sources

- **MCPs** 
  - `napari-mcp.md`: Interactive image visualization and analysis
  - `cellpose.md`: Cell segmentation and quantification
  - `fmcp.md`: Mathematical plotting (matplotlib, numpy, sympy)
  - `sympy-mcp.md`: Symbolic mathematics and calculus
  - `claude-scientific-skills.md`: Scientific computing capabilities
  - `data-forge.md`: Data manipulation and analysis
  - `notion.md`: Notion workspace integration
  - `zotero.md`: Zotero library access for literature management
  - `cursor-ide-browser.md`: Browser automation for testing





